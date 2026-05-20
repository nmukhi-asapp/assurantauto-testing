"""LLM-judge scoring under the re-anchored voice quality rubric, via LiteLLM proxy.

For each conversation:
  - Parse production transcript (voice_assistant sender filter)
  - Skip if not scoreable (<3 turns or 0 customer turns)
  - Send rubric + transcript to Claude Opus 4.7 via LiteLLM
  - Parse JSON scoring response
  - Save to per-conv JSON in data/scores/

Reads LITELLM_URL and LITELLM_API_KEY from .env in the repo root.
Run from the repo root or anywhere — paths are resolved relative to this file.
"""
import json, os, sys, glob, re, time, argparse, traceback
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

REPO = Path(__file__).parent.parent
DATA = REPO / 'data' / 'conversations' / 'CallerIdentification'
RUBRIC_PATH = REPO / 'voice_quality_rubric.md'
ENV_PATH = REPO / '.env'
OUT_DIR = REPO / 'data' / 'scores'
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL = os.environ.get('JUDGE_MODEL', 'vertex-claude-4.7-opus')


def load_env():
    url, key = None, None
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            v = v.strip().strip('"').strip("'")
            if k.strip() == 'LITELLM_URL':
                url = v
            elif k.strip() == 'LITELLM_API_KEY':
                key = v
    return url, key


def load_rubric():
    with open(RUBRIC_PATH) as f:
        return f.read()


def parse_transcript(actions):
    SYNTHETIC_PREFIXES = (
        "the caller", "the customer", "i told", "i let the customer",
        "caller identified", "customer identified",
    )
    NEXT_STEPS_MARKER = "what are the next steps"
    turns = []
    for a in actions:
        if a.get('type') != 'message':
            continue
        m = a.get('message') or {}
        sp = m.get('speaker') or m.get('sender')
        src = a.get('source_system')
        if src != 'voice_assistant':
            continue
        text = (m.get('text') or '').strip()
        if not text:
            continue
        if sp == 'customer':
            tl = text.lower()
            if any(tl.startswith(p) for p in SYNTHETIC_PREFIXES):
                continue
            if NEXT_STEPS_MARKER in tl:
                continue
            turns.append(('Customer', text))
        elif sp == 'bot':
            turns.append(('Talker', text))
    return turns


def tasks_chain(actions):
    return [a.get('task_name') for a in actions if a.get('type') == 'enter_task']


def is_scoreable(turns):
    if len(turns) < 3:
        return False
    return sum(1 for s, _ in turns if s == 'Customer') >= 1


def format_transcript(turns, max_chars=15000):
    out = []
    total = 0
    for sp, t in turns:
        line = f'  {sp}: {t}'
        if total + len(line) > max_chars:
            out.append('  [transcript truncated]')
            break
        out.append(line)
        total += len(line) + 1
    return '\n'.join(out)


JUDGE_SYSTEM_PREFIX = """You are an expert voice-AI quality evaluator. Your job is to score a production voice-AI conversation against the rubric below.

CRITICAL CALIBRATION INSTRUCTIONS:
- This rubric was re-anchored on 2026-05-13. A score of 3 means the dimension had a CLEAR, NOTICEABLE PROBLEM — it would fail an internal QA review. Do NOT use 3 as "OK/acceptable."
- 5 = no observable defects on this dimension. Rare.
- 4 = trivial deviation only, zero impact on caller experience or outcome.
- 3 = noticeable issue that affected the caller experience. Most calls with any real problem land here.
- 2 = wrong outcome or significant failure of the dimension.
- 1 = critical breakdown.
- Be willing to give 2s and 3s freely when warranted. Avoid central-tendency bias.

Return ONLY a JSON object with this schema (no markdown, no prose outside the JSON):
{
  "D1": <1-5>, "D2": <1-5>, "D3": <1-5>, "D4": <1-5>, "D5": <1-5>, "D6": <1-5>,
  "D8": <1-5>, "D9": <1-5>, "D10": <1-5>, "D12": <1-5>,
  "flags": [<"SAFETY_VIOLATION" | "CRITICAL_HALLUCINATION" | "ABANDONED">, ...],
  "notes": "<2-3 sentences explaining the key issues and the lowest-scoring dimension(s)>"
}

D7 (Speech Naturalness) and D11 (Acoustic Robustness) are not scored — they require audio.

D4 (Response Latency) and D5 (Turn-Taking) cannot be observed in a transcript without timestamps. Score these dimensions as 4 unless the transcript itself shows clear evidence of latency issues (e.g. customer reprompts the bot, "are you there?", filler not bridged) or turn-taking issues (bot talks over user, false barge-ins). Default 4 when no signal.

DESIGNED FLOW — DO NOT PENALIZE:
- Pre-transfer identifier collection: The bot is designed to ask for identifiers TWICE before transferring to a human agent. The first ask is a standalone request; the second ask expands the options ("contract number, claim number, or last 8 of your VIN") and is framed as "before I transfer you." A bot that performs both asks and then transfers on the second refusal is following the design correctly. Do NOT treat the second ask as a context-retention failure (D3) or a repair failure (D6), and do NOT lower D1 for it.
- Smart Deflection before escalation: The bot is designed to deflect the first agent-transfer request by asking what the caller needs help with. This is intentional and correct — do NOT penalize it as failing to honor the transfer request. Only the second explicit insistence on speaking to a human triggers the transfer obligation.
- Dealer claim funneling: For dealer callers asking about claims, the bot is designed to ask TWO funneling questions before collecting an identifier: (1) existing claim vs. new claim vs. other, and (2) what the issue is with the existing claim (e.g. payment status, claim status, modification). This two-step triage is correct by design — do NOT penalize it as over-funneling or a D1 deviation.
- Evaluate D1 against the DESIGNED FLOW, not against a frictionless ideal. Some friction is by design.

D2 (Information Accuracy) anchors:
- 5 = information directly and fully addresses the caller's specific question.
- 4 = information is relevant to the question and broadly correct, but does not directly address the caller's specific need (e.g. a generic status response to a specific sub-question). No wrong facts.
- 3 = information is partially relevant but clearly incomplete or misleading in a way that affects the caller.
- 2 = wrong or significantly inaccurate information provided.
- 1 = critical misinformation.

D9 (Verbosity): score based on response length and listenability — long script-y monologues are 2-3, right-sized chunked responses are 5.

D10 (ASR Quality): score ONLY on recognition fidelity — did the speech recognizer accurately transcribe what the caller said? A misrecognition (e.g. "agent" heard as "Asian") is a D10 failure regardless of how the bot responded. How the bot handles or recovers from an ASR error belongs in D6 (repair) and D1 (design adherence) — do NOT factor the bot's response into D10.

ABANDONED flag: set when the caller hung up or abandoned the call due to frustration before reaching their goal. Calls that ended normally (after the bot transferred or completed the task) are NOT abandoned.

The RUBRIC follows:

---

"""


def build_user_message(conv_id, tasks, transcript_text):
    return f"""Conversation ID: {conv_id}
Task chain: {tasks}

Transcript:
```
{transcript_text}
```

Score this conversation per the rubric. Return ONLY the JSON object."""


def score_one(client, conv_id, transcript_text, tasks, rubric):
    system = JUDGE_SYSTEM_PREFIX + rubric
    user = build_user_message(conv_id, ', '.join(tasks), transcript_text)
    last_err = None
    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                max_tokens=1500,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            text = resp.choices[0].message.content.strip()
            m = re.search(r'\{.*\}', text, re.S)
            if not m:
                raise ValueError(f'No JSON found in response: {text[:300]}')
            data = json.loads(m.group(0))
            usage = resp.usage
            return {
                'conv_id': conv_id,
                'tasks': tasks,
                'scores': data,
                'usage': {
                    'input_tokens': getattr(usage, 'prompt_tokens', 0),
                    'output_tokens': getattr(usage, 'completion_tokens', 0),
                },
            }
        except Exception as e:
            last_err = e
            time.sleep(2 ** attempt)
    raise last_err


def already_scored(conv_id):
    return (OUT_DIR / f'{conv_id}.json').exists()


def save_score(result):
    fp = OUT_DIR / f"{result['conv_id']}.json"
    with open(fp, 'w') as f:
        json.dump(result, f, indent=1)


def load_conv_data(conv_id):
    fp = DATA / f'platform::assurantauto::{conv_id}::.json'
    with open(fp) as f:
        d = json.load(f)
    return d['model_input']['actions']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ids', nargs='+', required=True, help='conversation IDs (or "-" for stdin)')
    ap.add_argument('--workers', type=int, default=5)
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    if args.ids == ['-']:
        ids = [l.strip() for l in sys.stdin if l.strip()]
    else:
        ids = args.ids
    if args.limit:
        ids = ids[:args.limit]

    url, key = load_env()
    if not url or not key:
        print(f'ERROR: missing LITELLM_URL or LITELLM_API_KEY in {ENV_PATH}', file=sys.stderr)
        sys.exit(1)
    print(f'LiteLLM URL: {url}')
    print(f'Model: {MODEL}')
    print(f'IDs to score: {len(ids)}')

    base_url = url.rstrip('/') + '/v1' if not url.rstrip('/').endswith('/v1') else url.rstrip('/')
    client = OpenAI(api_key=key, base_url=base_url)
    rubric = load_rubric()

    work = []
    skipped = 0
    already = 0
    for cid in ids:
        if already_scored(cid):
            already += 1
            continue
        try:
            actions = load_conv_data(cid)
        except FileNotFoundError:
            print(f'  MISSING: {cid}')
            continue
        turns = parse_transcript(actions)
        if not is_scoreable(turns):
            save_score({'conv_id': cid, 'tasks': tasks_chain(actions), 'scores': None,
                        'force_skip': True,
                        'reason': f'turns={len(turns)}, customer={sum(1 for s,_ in turns if s=="Customer")}'})
            skipped += 1
            continue
        text = format_transcript(turns)
        work.append((cid, text, tasks_chain(actions)))
    print(f'Scoreable to send: {len(work)}, force-skipped (new): {skipped}, already-scored: {already}')

    if not work:
        return

    done = 0
    fails = []
    started = time.time()
    total_in_tok = 0
    total_out_tok = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(score_one, client, cid, txt, ts, rubric): cid for cid, txt, ts in work}
        for f in as_completed(futures):
            cid = futures[f]
            try:
                result = f.result()
                save_score(result)
                done += 1
                total_in_tok += result['usage']['input_tokens']
                total_out_tok += result['usage']['output_tokens']
                if done % 5 == 0 or done == len(work):
                    elapsed = time.time() - started
                    rate = done / elapsed
                    eta = (len(work) - done) / max(rate, 0.01)
                    print(f'  [{done}/{len(work)}] {elapsed:.0f}s elapsed, {rate:.2f}/s, ETA {eta:.0f}s; tokens in={total_in_tok} out={total_out_tok}')
            except Exception as e:
                fails.append((cid, str(e)[:200]))
                print(f'  FAIL {cid}: {str(e)[:200]}')

    print(f'\nDone. scored={done}, failed={len(fails)}, tokens in={total_in_tok} out={total_out_tok}')
    if fails:
        for cid, err in fails[:5]:
            print(f'  {cid}: {err}')


if __name__ == '__main__':
    main()
