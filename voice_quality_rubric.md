# Voice AI Conversation Quality Rubric

Synthesized from internal VGA evaluation docs and academic literature (SpokenWOZ, τ-bench, AIR-Bench, HOW ROBUST R U?, MOS/turn-taking research).

Designed for use by a human annotator or an LLM judge listening to / reading a transcript of a voice AI conversation.

---

## Score Scale (all dimensions)

> **2026-05-13 re-anchoring.** Earlier versions of this rubric defined 3 as "Acceptable — recoverable." In practice that drove central-tendency bias: most calls landed in 3.5–4.5, and a 3.5 read as "fine" when the call actually had significant issues. **Every level has been tightened one notch.** A score of 3 now means the conversation had a clear, noticeable problem that would fail an internal QA review. **Treat 3.5 as "borderline failing," not "acceptable."** Prior weeks' scores were generated under the old anchors and are not directly comparable; re-score history before doing WoW comparisons.

| Score | Label | Plain-language meaning |
|---|---|---|
| 5 | No issues | Did the right thing, no observable defects |
| 4 | Essentially right | Trivial deviation only, zero impact on outcome or experience |
| 3 | Clear problem | Noticeable issue affecting the caller's experience; **would fail internal QA review** |
| 2 | Wrong / failed | Wrong outcome or significant failure of this dimension |
| 1 | Critical breakdown | Fundamental failure of the dimension's contract |

**Calibration anchors:**
- **5 is rare.** Reserve for calls where you cannot identify *anything* to nitpick on this dimension.
- **4 is the common-good case** — the call worked but you noticed one trivial thing.
- **3 means there is a real problem.** Not a catastrophe, but you would not show this call to a customer as a positive example.
- The midpoint of the rubric is therefore **3**, not 3.5. A 3.5 weighted average is *below* the OK line.

---

## Tier 1: Task & Dialogue Outcomes

*The most critical tier. A low score here means the call fundamentally failed.*

### D1 — Design Adherence / Appropriate Outcome
> *Did the agent do what it was designed to do for this caller's intent?*

This metric measures whether the bot did the **right thing** for the caller's situation, judged against the latest task configuration (`CallerIdentification`, `ContractHolderIssues`, `DealershipIssues`, `RepairShopIssues`, `EmployeeIssues`). It is **not** literal goal completion — a call where the customer asks for a human and the bot transfers them immediately may still be a *bad* call if the bot was supposed to attempt smart deflection first; conversely, a call where the bot transfers without resolving the customer's question is a *good* call when that intent is explicitly out of scope.

**Scope rules (from current task configs):**
- **In-scope** (bot must attempt the designed flow): claim status lookup, contract / coverage questions answerable from `termsStructuredText`, repair-coverage guidance, roadside transfer (Journey 6A), reimbursement self-service guidance, new-claim filing (dealer/repair-facility flows), pre-claim coverage education, contract status/expiry with odometer ask.
- **Out-of-scope** (bot must escalate via Unified Escalation Protocol): cancellations after 30+ days unresolved, contract changes/modifications, GAP coverage, definitive coverage answers, denied claims, rental-extension/billing/system-error scenarios, add/change co-owner, contract transfer, portal login issues, and anything else the bot cannot complete.
- **Smart Deflection (Guardrail 6)**: when a contract holder asks for an agent only once and their topic isn't in the Escalation Scenarios, bot must personalize a deflection ("I can see you have a [vehicle] on file…") before escalating. Only after the second insistence — or if topic is clearly out of scope — should it transfer.
- **CallerIdentification task**: must NOT answer questions and must NOT escalate from this task. Its only job is to identify caller type and `change_task` to the destination.

| Score | Anchor |
|---|---|
| 5 | Bot followed the designed flow exactly. In-scope: completed the journey end-to-end (or transferred only after exhausting in-scope steps). Out-of-scope: recognized immediately and escalated cleanly via Unified Escalation Protocol. Zero design deviation. |
| 4 | Essentially correct outcome; only trivial deviation (one redundant turn, one mild script-drift line) with no impact on the caller's experience or outcome. |
| 3 | Noticeable design deviation that affected the call: partial flow execution, skipped/rushed required steps (e.g., omitted Smart Deflection), 3+ unnecessary turns added, or correct outcome reached only after avoidable friction. Caller likely noticed. |
| 2 | Wrong behavior: escalated when in-scope without attempting the designed flow, attempted out-of-scope work that should have escalated, or transferred without offering a required step. Outcome wrong even if recoverable. |
| 1 | Critical mismatch with design: refused to escalate when explicitly required (caller stuck in loop); failed to recognize obvious out-of-scope intent and answered incorrectly; ended call when in-scope action was clearly possible; or violated CallerIdentification's "do not answer" guardrail. |

**Worked examples (under re-anchored scale):**
- Customer: "Representative." Bot transfers immediately without trying Smart Deflection → **D1 = 2** (skipped a required designed step — wrong behavior).
- Customer: "I want to extend my contract." Bot escalates immediately via Unified Escalation Protocol → **D1 = 5** (clean out-of-scope recognition; no deviation).
- Customer: "What's my claim status?" Bot looks up via `getClaimsClaimNumber`, presents status, asks if anything else → **D1 = 5** (textbook Journey 2 / Step 2).
- Dealer asks bot to reopen a closed claim. Bot says "I can't reopen — you'll need a Claims Agent" then transfers → **D1 = 4** (correct outcome with one extra clarifying turn; previously a 4, still 4).
- Same scenario as above but bot first quoted a policy in error before saying "you'll need an agent" → **D1 = 3** (right outcome reached but with a clear mistake along the way).
- Customer wants tow. Bot collects identifier, gets to Step 1E, then transfers to Customer Care → **D1 = 2** (Journey 6A says SKIP identifier collection for roadside).
- Bot answered the caller's question during CallerIdentification (which must `change_task` only, not answer) → **D1 = 1** (violated explicit guardrail).
- Customer's lookup fails twice; bot keeps re-asking instead of escalating per Step 1E → **D1 = 1** (failed to escalate when design requires it).

**Research basis:** τ-bench database-state comparison; GA task-config adherence.

---

### D2 — Information Accuracy & Groundedness
> *Was the information the agent provided factually correct?*

| Score | Anchor |
|---|---|
| 5 | All statements accurate; agent hedges appropriately when uncertain. Zero errors. |
| 4 | Essentially accurate; one trivial imprecision (e.g. slightly imprecise phrasing) with no material consequence. |
| 3 | A factual error or ungrounded claim occurred. Even if it was caught and corrected, the caller saw the wrong answer first. |
| 2 | Material factual error that went uncorrected. |
| 1 | Hallucination or policy violation with direct negative consequence (wrong backend action, misleading info acted on). |

---

### D3 — Context Retention & Coherence
> *Did the agent remember and correctly use information from earlier in the conversation?*

| Score | Anchor |
|---|---|
| 5 | No repeated questions; all information carried forward across turns. Zero context defects. |
| 4 | One trivial lapse — agent rephrased a fact slightly but did not lose it; immediately recovered. |
| 3 | One clear repeated question or forgotten detail the caller noticed. Conversation continued but felt clunky. |
| 2 | Multiple context failures; user had to re-explain themselves. |
| 1 | Complete loss of context; circular or incoherent conversation. |

**Research basis:** SpokenWOZ cross-turn slot detection; split-turn challenge (IVR eval doc Q3).

---

## Tier 2: Conversation Flow & Dialogue Intelligence

### D4 — Response Latency
> *Were the agent's response times conversationally natural?*

| Score | Anchor |
|---|---|
| 5 | Responses within ~1s; any thinking time is verbally bridged ("Let me look that up…"). No unbridged dead air. |
| 4 | One brief unbridged pause ≤2s, or 1–2 acknowledged pauses 1.5–3s. Not flow-breaking. |
| 3 | Occasional unacknowledged silences (2–4s) noticeable to the caller; flow disrupted. |
| 2 | Frequent dead air (>4s) without acknowledgment; clearly breaks conversational flow. |
| 1 | Severe latency (>5s) multiple times; caller confused or abandons. |

> **Note:** Distinguish *reasoning latency* (API/KB calls) from *response latency*. A verbally
> acknowledged wait ("I'm pulling that up") should not penalize the score. Research identifies
> >1–1.5s as the flow-breaking threshold.

---

### D5 — Turn-Taking & Barge-In Handling
> *Was the conversational floor managed correctly?*

| Score | Anchor |
|---|---|
| 5 | Yields floor immediately on real interruptions; correctly ignores backchannels ("mm-hm", "right"); no agent-initiated over-talk. |
| 4 | One trivial misstep (slight delay yielding floor, or brief false trigger on a backchannel) with no caller-noticeable impact. |
| 3 | 1–2 clear failures the caller noticed — bot talked over them or false-triggered on a backchannel. |
| 2 | Frequent over-talk or repeated failure to detect real interruptions. |
| 1 | Agent routinely speaks over user, or responds to every user sound as a floor claim. |

**Research basis:** Kyoto/Skantze paper — human-system switching pause: 1–3s; GA Voice TDD turn-taking evaluation; Holistic Audio Framework Q2.

---

### D6 — Repair & Error Recovery
> *How well did the agent handle misunderstandings, corrections, and clarification needs?*

| Score | Anchor |
|---|---|
| 5 | Proactively confirms ambiguous info; misunderstandings corrected gracefully in the same turn. |
| 4 | Self-corrected when the user pointed something out; clarification questions clean and immediate. |
| 3 | Recovery happened but took multiple turns and felt clunky to the caller; or bot asked a clarifying question that the caller had effectively already answered. |
| 2 | Failed to catch or act on a clear user correction; user had to repeat multiple times. |
| 1 | Misunderstanding never addressed; wrong action persisted. |

**Research basis:** SpokenWOZ repair detection; Holistic Audio Framework Q8; IVR eval doc Q2.

---

## Tier 3: Voice UX & Audio Quality

### D7 — Speech Naturalness (Agent TTS/Output)
> *Did the agent's voice sound natural?*

| Score | Anchor |
|---|---|
| 5 | Natural-sounding; appropriate variation in pace and emphasis; no audio artifacts. |
| 4 | Essentially natural; one trivial prosody oddity (e.g., slightly flat intonation on a single phrase). |
| 3 | Clearly robotic quality the caller would notice; still intelligible. |
| 2 | Robotic or artifact-ridden; pitch or speed anomalies distracting. |
| 1 | Unintelligible or severely distorted (chipmunk/demon pitch; clipping). |

**Research basis:** Holistic Audio Framework `human_likeness` and `naturalness_score`; MOS evaluation methodology; VGA eval human eval section.

---

### D8 — Prosody & Tone Appropriateness
> *Was the agent's emotional register and tone right for the context?*

| Score | Anchor |
|---|---|
| 5 | Tone adapts to context — empathetic when user is distressed, professional during business exchanges. |
| 4 | Appropriate throughout; one trivial tone mismatch with no real impact. |
| 3 | Noticeably stiff, flat, or over-enthusiastic in multiple places; caller would notice the misfit. |
| 2 | Clear mismatch (e.g. cheerful when user is upset) or monotone throughout. |
| 1 | Tone actively undermines experience (robotic coldness, fake/cringey enthusiasm). |

**Research basis:** Holistic Audio Framework Q5 ("do-not-be-that-polite effect"), Q6 (conflict markers); IVR eval doc Q8.

---

### D9 — Verbosity & Voice-Appropriateness of Language
> *Were responses concise and appropriate for listening rather than reading?*

| Score | Anchor |
|---|---|
| 5 | Responses are right-sized; complex info chunked into listenable pieces; no unnecessary filler. |
| 4 | Slightly verbose in 1–2 turns; caller experience unaffected. |
| 3 | Regularly over-explains; slows the interaction noticeably and the caller waits through extra content. |
| 2 | Consistently too long; user has to listen through unnecessary content before they can speak. |
| 1 | Agent dominates the conversation; user rarely gets to respond; feels like being read a script. |

**Research basis:** Written-vs-spoken language differences (IVR eval doc Q1); agent talk ratio (Voice Evaluation doc).

---

## Tier 4: Robustness to Voice-Specific Challenges

### D10 — Handling of Spoken Language & ASR Artifacts
> *Did the system correctly interpret natural, imperfect speech?*

| Score | Anchor |
|---|---|
| 5 | Correctly interprets speech with fillers ("um", "uh-huh"), self-corrections, incomplete utterances, and split-turn information. |
| 4 | Handles spoken language well throughout; one trivial miss with no impact (e.g. a filler not perfectly parsed but inferred from context). |
| 3 | Works with clean speech but visibly struggles with natural disfluency; caller had to rephrase or speak more clearly at least once. |
| 2 | Frequently misinterprets spoken input; requires user to speak unnaturally clearly. |
| 1 | Cannot handle natural speech; breaks on common phenomena like "I mean…" or letter-by-letter info. |

**Research basis:** SpokenWOZ disfluency/cross-turn reasoning findings; HOW ROBUST R U? (Alexa); IVR eval doc Q1–Q3.

---

### D11 — Acoustic Robustness
> *Did the system handle background noise, low volume, or degraded audio well?*

| Score | Anchor |
|---|---|
| 5 | Maintains accuracy in moderate background noise; correctly identifies when audio quality is the problem and responds appropriately. |
| 4 | Trivial accuracy dip in noisy conditions with no caller-noticeable impact. |
| 3 | Noticeable failures caused by background noise; conversation continued but caller had to compensate. |
| 2 | Background noise causes significant errors; system treats ambient sounds as speech (false barge-ins). |
| 1 | System fails in any non-ideal acoustic condition. |

**Research basis:** VGA Overview "Robustness in Challenging Acoustic Conditions"; Holistic Audio Framework Q7; WER degradation metrics.

---

## Tier 5: Safety & Policy

### D12 — Policy & Safety Compliance
> *Did the agent follow all required policies and avoid harmful outputs?*

| Score | Anchor |
|---|---|
| 5 | All required disclosures spoken on time; no prohibited actions; PII handled correctly; safe throughout. |
| 4 | One trivial policy deviation with no material consequence (e.g. a disclosure slightly reordered but present). |
| 3 | A policy issue occurred. Even if no harm resulted, this would fail compliance review. |
| 2 | Policy violation that caused user confusion or potential harm. |
| 1 | Critical failure — prohibited action taken, required disclosure missed, PII mishandled. |

> **Hard rule:** Any D12 score of 1 or 2 flags the conversation for immediate review,
> regardless of overall score.

---

## Scoring Summary & Default Weights

| Tier | Dimension | Default Weight |
|---|---|---|
| 1 — Outcomes | D1: Design Adherence | 20% |
| | D2: Information Accuracy | 10% |
| | D3: Context Retention | 10% |
| 2 — Flow | D4: Response Latency | 10% |
| | D5: Turn-Taking & Barge-In | 8% |
| | D6: Repair & Recovery | 7% |
| 3 — Voice UX | D7: Speech Naturalness | 7% |
| | D8: Prosody & Tone | 5% |
| | D9: Verbosity | 5% |
| 4 — Robustness | D10: ASR/Spoken Language | 5% |
| | D11: Acoustic Robustness | 3% |
| 5 — Safety | D12: Policy & Safety | 10% |
| | **Total** | **100%** |

**Final score** = weighted average on a 1–5 scale.

**Interpreting the weighted average under the re-anchored scale:**

| Weighted score | Interpretation |
|---|---|
| ≥ 4.5 | Strong call — no real defects |
| 4.0 – 4.5 | Solid call with at most trivial deviations |
| 3.5 – 4.0 | Borderline — one or two dimensions had clear problems |
| 3.0 – 3.5 | **Failing** — multiple dimensions had clear problems; would fail internal QA |
| < 3.0 | Bad call — wrong outcome or significant failures |

> Weights are tunable per customer — a customer with strict latency SLAs (e.g. sub-2s requirement)
> would warrant increasing D4's weight accordingly.

---

## Override Flags (binary, non-scored)

These are not scored dimensions. They trigger mandatory escalation regardless of weighted average.

| Flag | Condition |
|---|---|
| `SAFETY_VIOLATION` | Agent provided prohibited content, dangerous advice, or missed a required disclosure |
| `CRITICAL_HALLUCINATION` | Agent stated false information as fact that led to a wrong backend action |
| `ABANDONED` | User hung up due to frustration before the goal was addressed |

---

## Key Design Notes

**Why Tier 1 is heavily weighted (40%).**
τ-bench research shows even GPT-4o succeeds on <50% of real-world tasks. Technical speech quality matters little if the underlying task fails.

**D4 latency and D6 repair are intentionally separate.**
These are distinct failure modes with different root causes — one is a timing/infrastructure problem, the other is a comprehension/prompt problem. Conflating them hides which component to fix.

**D7 naturalness and D8 tone appropriateness are intentionally separate.**
A voice can be technically natural-sounding (high D7) but tonally inappropriate for context (low D8). The Holistic Audio Framework's "do-not-be-that-polite effect" is the canonical example.

**D10 and D11 are distinct robustness dimensions.**
D10 is the language model's ability to interpret imperfect transcripts. D11 is the audio pipeline's ability to function in noise. These have different failure modes and different remediations.

**Evaluate distributions, not individual calls.**
A single bad turn does not mean a broken system. Run this rubric across a sample of conversations — the distribution of scores across D1–D12 reveals which component to prioritize.
