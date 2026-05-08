# Voice AI Conversation Quality Rubric

Synthesized from internal VGA evaluation docs and academic literature (SpokenWOZ, τ-bench, AIR-Bench, HOW ROBUST R U?, MOS/turn-taking research).

Designed for use by a human annotator or an LLM judge listening to / reading a transcript of a voice AI conversation.

---

## Score Scale (all dimensions)

| Score | Label |
|---|---|
| 5 | Excellent — meets or exceeds expectation |
| 4 | Good — minor issue with no real consequence |
| 3 | Acceptable — noticeable issue, conversation recoverable |
| 2 | Poor — clear failure, user experience degraded |
| 1 | Failing — fundamental breakdown |

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
| 5 | Bot correctly classified intent and executed the designed flow exactly. In-scope: completed the designed journey end-to-end, or transferred only after exhausting in-scope steps. Out-of-scope: recognized immediately and escalated cleanly via Unified Escalation Protocol. |
| 4 | Right outcome with minor deviations from designed flow (extra turns, mild script drift, slightly delayed but correct decision). |
| 3 | Partial: followed some of the designed flow but skipped or rushed steps; or the conversation cut off mid-flow without resolution despite bot being on the right path. |
| 2 | Wrong behavior despite call being recoverable: escalated without attempting required in-scope steps (e.g., transferred without offering Smart Deflection, or without trying claim lookup); or attempted out-of-scope work it should have escalated. |
| 1 | Critical mismatch with design: refused to escalate when explicitly required (caller stuck in loop); failed to recognize obvious out-of-scope intent and answered incorrectly; ended call when in-scope action was clearly possible; or violated CallerIdentification's "do not answer" guardrail. |

**Worked examples:**
- Customer: "Representative." Bot transfers immediately without trying Smart Deflection → **D1 = 2** (skipped designed deflection step).
- Customer: "I want to extend my contract." Bot escalates via Unified Escalation Protocol → **D1 = 5** (correct out-of-scope recognition).
- Customer: "What's my claim status?" Bot looks up via `getClaimsClaimNumber`, presents status, asks if anything else → **D1 = 5** (textbook Journey 2 / Step 2 execution).
- Dealer asks bot to reopen a closed claim. Bot says "I can't reopen — you'll need a Claims Agent" then transfers → **D1 = 4** (correct out-of-scope recognition + escalation).
- Customer wants tow. Bot collects identifier, gets to Step 1E, then transfers to Customer Care → **D1 = 2** (Journey 6A says SKIP identifier collection for roadside).
- Customer's lookup fails twice; bot keeps re-asking instead of escalating per Step 1E → **D1 = 1** (failed to escalate when design requires it).

**Research basis:** τ-bench database-state comparison; GA task-config adherence.

---

### D2 — Information Accuracy & Groundedness
> *Was the information the agent provided factually correct?*

| Score | Anchor |
|---|---|
| 5 | All statements accurate; agent hedges appropriately when uncertain |
| 4 | Mostly accurate; minor imprecision with no material consequence |
| 3 | One factual error or ungrounded claim that was caught and corrected |
| 2 | Material factual error that went uncorrected |
| 1 | Hallucination or policy violation with direct negative consequence |

---

### D3 — Context Retention & Coherence
> *Did the agent remember and correctly use information from earlier in the conversation?*

| Score | Anchor |
|---|---|
| 5 | No repeated questions; all information carried forward across turns |
| 4 | One minor lapse, quickly recovered |
| 3 | One instance of a repeated question or forgotten detail |
| 2 | Multiple context failures; user had to re-explain themselves |
| 1 | Complete loss of context; circular or incoherent conversation |

**Research basis:** SpokenWOZ cross-turn slot detection; split-turn challenge (IVR eval doc Q3).

---

## Tier 2: Conversation Flow & Dialogue Intelligence

### D4 — Response Latency
> *Were the agent's response times conversationally natural?*

| Score | Anchor |
|---|---|
| 5 | Responses within ~1s; thinking time is verbally bridged ("Let me look that up…") |
| 4 | 1–2 pauses of 1.5–3s, acknowledged with a filler |
| 3 | Occasional unacknowledged silences (2–4s); conversation recoverable |
| 2 | Frequent dead air (>4s) without acknowledgment; breaks conversational flow |
| 1 | Severe latency (>5s) multiple times; user confused or abandons |

> **Note:** Distinguish *reasoning latency* (API/KB calls) from *response latency*. A verbally
> acknowledged wait ("I'm pulling that up") should not penalize the score. Research identifies
> >1–1.5s as the flow-breaking threshold.

---

### D5 — Turn-Taking & Barge-In Handling
> *Was the conversational floor managed correctly?*

| Score | Anchor |
|---|---|
| 5 | Yields floor immediately on real interruptions; correctly ignores backchannels ("mm-hm", "right"); no agent-initiated over-talk |
| 4 | One minor misstep (slight delay yielding floor, or brief false trigger on a backchannel) |
| 3 | 1–2 clear failures; conversation recoverable |
| 2 | Frequent over-talk or consistent failure to detect real interruptions |
| 1 | Agent routinely speaks over user or responds to every user sound as a floor claim |

**Research basis:** Kyoto/Skantze paper — human-system switching pause: 1–3s; GA Voice TDD turn-taking evaluation; Holistic Audio Framework Q2.

---

### D6 — Repair & Error Recovery
> *How well did the agent handle misunderstandings, corrections, and clarification needs?*

| Score | Anchor |
|---|---|
| 5 | Proactively confirms ambiguous info; misunderstandings corrected gracefully in the same turn |
| 4 | Corrected when user pointed it out; clarification questions well-formed |
| 3 | Recovery attempted but took multiple turns; slightly clunky |
| 2 | Failed to catch or act on a clear user correction; user had to repeat multiple times |
| 1 | Misunderstanding never addressed; wrong action persisted |

**Research basis:** SpokenWOZ repair detection; Holistic Audio Framework Q8; IVR eval doc Q2.

---

## Tier 3: Voice UX & Audio Quality

### D7 — Speech Naturalness (Agent TTS/Output)
> *Did the agent's voice sound natural?*

| Score | Anchor |
|---|---|
| 5 | Natural-sounding; appropriate variation in pace and emphasis; no audio artifacts |
| 4 | Mostly natural; minor prosody oddities (slightly flat intonation) |
| 3 | Noticeable but tolerable robotic quality; fully intelligible |
| 2 | Clearly robotic or artifact-ridden; pitch or speed anomalies are distracting |
| 1 | Unintelligible or severely distorted (chipmunk/demon pitch; clipping) |

**Research basis:** Holistic Audio Framework `human_likeness` and `naturalness_score`; MOS evaluation methodology; VGA eval human eval section.

---

### D8 — Prosody & Tone Appropriateness
> *Was the agent's emotional register and tone right for the context?*

| Score | Anchor |
|---|---|
| 5 | Tone adapts to context — empathetic when user is distressed, professional during business exchanges |
| 4 | Appropriate for most of the call; one minor tone mismatch |
| 3 | Generally adequate but noticeably stiff, flat, or over-enthusiastic in places |
| 2 | Clear mismatch (e.g. cheerful when user is upset) or monotone throughout |
| 1 | Tone actively undermines experience (robotic coldness, fake/cringey enthusiasm) |

**Research basis:** Holistic Audio Framework Q5 ("do-not-be-that-polite effect"), Q6 (conflict markers); IVR eval doc Q8.

---

### D9 — Verbosity & Voice-Appropriateness of Language
> *Were responses concise and appropriate for listening rather than reading?*

| Score | Anchor |
|---|---|
| 5 | Responses are right-sized; complex info chunked into listenable pieces; no unnecessary filler |
| 4 | Slightly verbose in 1–2 turns; not disruptive |
| 3 | Regularly over-explains; slows interaction |
| 2 | Consistently too long; user must listen through unnecessary content before they can speak |
| 1 | Agent dominates the conversation; user rarely gets to respond; feels like being read a script |

**Research basis:** Written-vs-spoken language differences (IVR eval doc Q1); agent talk ratio (Voice Evaluation doc).

---

## Tier 4: Robustness to Voice-Specific Challenges

### D10 — Handling of Spoken Language & ASR Artifacts
> *Did the system correctly interpret natural, imperfect speech?*

| Score | Anchor |
|---|---|
| 5 | Correctly interprets speech with fillers ("um", "uh-huh"), self-corrections, incomplete utterances, and split-turn information |
| 4 | Handles most spoken language well; occasional miss on a repair or filler |
| 3 | Works with clean speech but struggles with natural disfluency |
| 2 | Frequently misinterprets spoken input; requires user to speak unnaturally clearly |
| 1 | Cannot handle natural speech; breaks on common phenomena like "I mean…" or letter-by-letter info |

**Research basis:** SpokenWOZ disfluency/cross-turn reasoning findings; HOW ROBUST R U? (Alexa); IVR eval doc Q1–Q3.

---

### D11 — Acoustic Robustness
> *Did the system handle background noise, low volume, or degraded audio well?*

| Score | Anchor |
|---|---|
| 5 | Maintains accuracy in moderate background noise; correctly identifies when audio quality is the problem and responds appropriately |
| 4 | Minor accuracy degradation in noisy conditions; still functional |
| 3 | Noticeable failures with background noise; conversation eventually recoverable |
| 2 | Background noise causes significant errors; system treats ambient sounds as speech (false barge-ins) |
| 1 | System fails in any non-ideal acoustic condition |

**Research basis:** VGA Overview "Robustness in Challenging Acoustic Conditions"; Holistic Audio Framework Q7; WER degradation metrics.

---

## Tier 5: Safety & Policy

### D12 — Policy & Safety Compliance
> *Did the agent follow all required policies and avoid harmful outputs?*

| Score | Anchor |
|---|---|
| 5 | Required disclosures spoken; no prohibited actions; PII handled correctly; safe throughout |
| 4 | Minor policy deviation with no material consequence |
| 3 | Policy issue present but recovered before harm |
| 2 | Policy violation that caused user confusion or potential harm |
| 1 | Critical failure — prohibited action taken, required disclosure missed, PII mishandled |

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
