## Batch Quality Report — CallerIdentification
*Updated 2026-05-09 (v2): April 17 conversations excluded entirely (15 convs removed: 9 scored + 6 force-skip). Total now 218 convs / 140 scored. All other content (D1 = 'Design Adherence', proper voice_assistant filter, May 6-9 data) retained from prior version.*
Conversations analyzed: 218  |  Scored: 140  |  Skipped (no customer turns): 78  |  Date: 2026-05-09

| Metric | Value |
|---|---|
| Mean overall score (scored convs) | 3.99 / 5 (75/100) |
| **Pass rate** | **69/140 = 49%** |
| Conversations scoring < 3.0 | 6 (4%) |
| Safety / policy flags | 1 |
| Critical hallucination flags | 1 |
| Abandoned calls | 11 (8%) |
| Human transfers (all 218) | 145 (67%) |

---

---

## Section 1.5: Pass / Fail
*Binary metric per conversation:*
- **PASS** = (call contained by GenAgent AND caller not frustrated) **OR** (call transferred AND intent was out-of-scope by design AND caller not frustrated)
- **FAIL** = anything else (bot wrongly transferred an in-scope intent, bot wrongly contained an out-of-scope intent, or caller expressed frustration)

Derived from existing scores: PASS iff D1 ≥ 4 (bot followed designed flow) AND no frustration indicators (ABANDONED flag, D1=1, or notes containing patterns like 'looped', 'never escalated', 'kept asking', 'stuck', etc.).

| Metric | Value |
|---|---|
| **Pass rate** | **69/140 = 49.3%** |
| Pass — contained + not frustrated | 3 (2%) |
| Pass — out-of-scope transfer + not frustrated | 66 (47%) |
| Fail — caller frustrated | 26 (19%) |
| Fail — bot wrong action (no explicit frustration) | 45 (32%) |

### Pass/Fail Daily Trend

| Date | Total | Pass | % Pass | Trend |
|------|-------|------|--------|-------|
| 2026-04-18 | 2 | 0 | 0% | ························· |
| 2026-04-20 | 10 | 4 | 40% | ██████████··············· |
| 2026-04-21 | 12 | 8 | 67% | ████████████████········· |
| 2026-04-22 | 9 | 1 | 11% | ██······················· |
| 2026-04-23 | 9 | 3 | 33% | ████████················· |
| 2026-04-24 | 3 | 2 | 67% | ████████████████········· |
| 2026-04-27 | 5 | 1 | 20% | █████···················· |
| 2026-04-28 | 9 | 5 | 56% | █████████████············ |
| 2026-04-29 | 6 | 2 | 33% | ████████················· |
| 2026-04-30 | 3 | 1 | 33% | ████████················· |
| 2026-05-01 | 4 | 3 | 75% | ██████████████████······· |
| 2026-05-04 | 9 | 3 | 33% | ████████················· |
| 2026-05-05 | 22 | 8 | 36% | █████████················ |
| 2026-05-06 | 15 | 13 | 87% | █████████████████████···· |
| 2026-05-07 | 8 | 6 | 75% | ██████████████████······· |
| 2026-05-08 | 13 | 8 | 62% | ███████████████·········· |
| 2026-05-09 | 1 | 1 | 100% | █████████████████████████ |

**Observations:**
- Overall pass rate is **49%**.
- Best day: **May 6 (87%, 13/15)** — most calls were clean denied-claim escalations and claim-status flows.
- Worst day: **Apr 22 (11%, 1/9)** — concentration of bot failures (transfer-intent loops, Spanish caller, hallucination).
- Most recent days show improvement: May 6–9 averages **28/37 = 76%** vs. April average of **27/68 = 40%**.

---

## Section 2: Week-over-Week Trend
*ISO weeks. Scored conversations only. Single-turn calls with no customer transcript excluded.*

| Week | Dates | Scored | Mean Score | Score /100 | % < 3.0 | Abandoned | D1 Mean | D10 Mean |
|------|-------|--------|------------|------------|---------|-----------|---------|----------|
| Wk 16 (Apr 14–18) | 2026-04-18 – 2026-04-18 | 2 | 3.51 / 5 | 63 | 0 (0%) | 0 | 2.00 | 3.50 |
| Wk 17 (Apr 21–27) | 2026-04-20 – 2026-04-24 | 43 | 3.81 / 5 | 70 | 5 (12%) | 6 | 2.79 | 3.84 |
| Wk 18 (Apr 28–May 4) | 2026-04-27 – 2026-05-01 | 27 | 4.08 / 5 | 77 | 0 (0%) | 2 | 3.00 | 3.89 |
| Wk 19 (May 5–11) | 2026-05-04 – 2026-05-09 | 68 | 4.09 / 5 | 77 | 1 (1%) | 3 | 3.72 | 3.99 |

---

## Section 2.5: Daily Score Trend
*Mean weighted score per day (scored conversations only). Single-turn calls excluded. April 17 excluded from analysis.*

| Date | N | Mean /5 | /100 | Trend |
|------|---|---------|------|-------|
| 2026-04-18 | 2 | 3.51 | 63 | ██████████████████············ |
| 2026-04-20 | 10 | 3.74 | 69 | ████████████████████·········· |
| 2026-04-21 | 12 | 4.20 | 80 | ███████████████████████······· |
| 2026-04-22 | 9 | 3.34 | 59 | █████████████████············· |
| 2026-04-23 | 9 | 3.71 | 68 | ████████████████████·········· |
| 2026-04-24 | 3 | 4.22 | 80 | ████████████████████████······ |
| 2026-04-27 | 5 | 3.77 | 69 | ████████████████████·········· |
| 2026-04-28 | 9 | 4.10 | 77 | ███████████████████████······· |
| 2026-04-29 | 6 | 4.04 | 76 | ██████████████████████········ |
| 2026-04-30 | 3 | 4.17 | 79 | ███████████████████████······· |
| 2026-05-01 | 4 | 4.44 | 86 | █████████████████████████····· |
| 2026-05-04 | 9 | 4.01 | 75 | ██████████████████████········ |
| 2026-05-05 | 22 | 4.01 | 75 | ██████████████████████········ |
| 2026-05-06 | 15 | 4.20 | 80 | ███████████████████████······· |
| 2026-05-07 | 8 | 4.21 | 80 | ████████████████████████······ |
| 2026-05-08 | 13 | 4.06 | 76 | ██████████████████████········ |
| 2026-05-09 | 1 | 4.28 | 82 | ████████████████████████······ |

**Observations:**
- The lowest-scoring day is **Apr 22 (3.34/5)**, driven by 5 of the 8 transfer-intent failures plus the only Spanish-speaker abandonment, the only false-transfer hallucination, and a "failed 6+ rep requests" case.
- The highest-scoring day is **May 1 (4.44/5)**, driven by clean denied-claim escalations and roadside transfers.
- Day-by-day variance (3.34 to 4.44) is wider than the week-level variance.
- May 5 is the largest single day (N=22) and sits at the population mean — recent volume may reflect a launch ramp.
- May 9 is partial (N=1) and not yet stable.

## Section 3: Dimension Heatmap
*Sorted by % scoring ≤ 2 (worst first). D7 and D11 require audio — N/A.*

| Dim | Name | Weight | Mean | Std | Min | Max | % ≤ 2 |
|-----|------|--------|------|-----|-----|-----|-------|
| D1 | Design Adherence | 20% | 3.27 | 1.36 | 1 | 5 | 29% |
| D6 | Repair & Recovery | 7% | 3.65 | 0.87 | 1 | 5 | 9% |
| D8 | Tone Appropriateness | 5% | 3.66 | 0.71 | 1 | 5 | 6% |
| D10 | ASR/Spoken Language | 5% | 3.91 | 0.76 | 2 | 5 | 3% |
| D2 | Information Accuracy | 10% | 4.31 | 0.69 | 1 | 5 | 2% |
| D4 | Response Latency | 10% | 4.16 | 0.74 | 2 | 5 | 2% |
| D3 | Context Retention | 10% | 3.95 | 0.69 | 2 | 5 | 1% |
| D12 | Policy & Safety | 10% | 4.69 | 0.51 | 2 | 5 | 1% |
| D5 | Turn-Taking | 8% | 4.34 | 0.61 | 3 | 5 | 0% |
| D9 | Verbosity | 5% | 4.96 | 0.22 | 3 | 5 | 0% |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 4: Per-Conversation Scores
*All 140 conversations with substantive transcripts. Single-turn calls excluded.*
*D4 and D9 are auto-computed from timestamps/word counts. D7 and D11 require audio.*

| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | Flags | Pass/Fail |
|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-------|-----------|
| [CONV 1](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0008094092-1111757297-2660275256-0825805307?organization=assurantauto) | Apr 28 | 29 | 3 | 5 | 4 | 3 | 4 | 4 | 4 | 5 | 3 | 5 | 3.89 (72) | — | ✗ FAIL |
| [CONV 4](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0115003615-1207964145-2886329601-1638018563?organization=assurantauto) | May 05 | 4 | 4 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.92 (73) | — | ✓ PASS |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | Apr 27 | 19 | 1 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 3.64 (66) | — | ✗ FAIL |
| [CONV 6](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0195488489-1011028465-3000800312-0825805307?organization=assurantauto) | Apr 20 | 17 | 3 | 5 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 3.94 (74) | — | ✗ FAIL |
| [CONV 7](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0200416497-1049760241-2169995754-2917985560?organization=assurantauto) | Apr 23 | 16 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | May 05 | 4 | 2 | 5 | 3 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.73 (68) | — | ✗ FAIL |
| [CONV 11](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | Apr 22 | 27 | 1 | 3 | 4 | 4 | 3 | 3 | 3 | 5 | 3 | 5 | 3.11 (53) | — | ✗ FAIL |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0332358522-1233523185-2987848121-1659749027?organization=assurantauto) | May 07 | 15 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 16](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0333763583-1193415153-2807464426-2917985560?organization=assurantauto) | May 04 | 9 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4.00 (75) | — | ✓ PASS |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | Apr 22 | 13 | 1 | 2 | 4 | 5 | 5 | 3 | 3 | 5 | 3 | 4 | 3.18 (54) | ⚠ HALLUC | ✗ FAIL |
| [CONV 19](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0396067837-1216549361-2959729921-1638018563?organization=assurantauto) | May 06 | 23 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 20](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0441985862-1246302705-2759910657-1638018563?organization=assurantauto) | May 08 | 32 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.17 (79) | — | ✓ PASS |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | May 04 | 4 | 2 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4.33 (83) | — | ✗ FAIL |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0478963028-1245516273-2936336825-1659749027?organization=assurantauto) | May 08 | 7 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.61 (90) | — | ✓ PASS |
| [CONV 24](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0482211455-1150947825-2550392065-1638018563?organization=assurantauto) | May 01 | 27 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — | ✓ PASS |
| [CONV 26](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0490543454-1024004593-2737237860-1336708325?organization=assurantauto) | Apr 21 | 19 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — | ✓ PASS |
| [CONV 27](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0502877744-1219695089-2243555769-1659749027?organization=assurantauto) | May 06 | 28 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 4.00 (75) | — | ✓ PASS |
| [CONV 29](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | May 01 | 7 | 2 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4.13 (78) | — | ✗ FAIL |
| [CONV 30](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0729601212-1231163889-2430788865-1638018563?organization=assurantauto) | May 07 | 23 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 33](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0769152030-1195315697-2760631553-1638018563?organization=assurantauto) | May 04 | 25 | 3 | 5 | 3 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 3.92 (73) | — | ✗ FAIL |
| [CONV 36](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0776533978-1143017969-2437280185-1659749027?organization=assurantauto) | Apr 30 | 19 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 4.37 (84) | — | ✓ PASS |
| [CONV 37](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0795050560-1204490737-3136061930-2917985560?organization=assurantauto) | May 05 | 19 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4.37 (84) | — | ✓ PASS |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0797214453-1234637297-3210670521-1659749027?organization=assurantauto) | May 07 | 35 | 2 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | — | ✗ FAIL |
| [CONV 40](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0839037409-1112805873-2891284970-2917985560?organization=assurantauto) | Apr 28 | 18 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — | ✓ PASS |
| [CONV 41](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0859768425-1207112177-2833442049-1638018563?organization=assurantauto) | May 05 | 16 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (78) | — | ✓ PASS |
| [CONV 43](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0878025181-1209209329-2674651577-1659749027?organization=assurantauto) | May 05 | 22 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — | ✗ FAIL |
| [CONV 44](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0906932620-1045303793-2487850040-0825805307?organization=assurantauto) | Apr 23 | 29 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.31 (83) | — | ✓ PASS |
| [CONV 49](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0990410271-1233326577-2952914177-1638018563?organization=assurantauto) | May 07 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | — | ✗ FAIL |
| [CONV 51](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1015743628-1207964145-2279928249-1659749027?organization=assurantauto) | May 05 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — | ✓ PASS |
| [CONV 53](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1041970917-1216614897-3028021689-1659749027?organization=assurantauto) | May 06 | 33 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 57](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1096837356-1243681265-3071996345-1659749027?organization=assurantauto) | May 08 | 22 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | — | ✓ PASS |
| [CONV 58](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1102387425-1221136881-2885415353-1659749027?organization=assurantauto) | May 06 | 26 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4.76 (94) | — | ✓ PASS |
| [CONV 59](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1112326957-1194463729-2387469569-1638018563?organization=assurantauto) | May 04 | 25 | 3 | 5 | 4 | 5 | 4 | 3 | 4 | 5 | 3 | 5 | 4.03 (76) | — | ✗ FAIL |
| [CONV 60](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1122006560-1209733617-2927224065-1638018563?organization=assurantauto) | May 06 | 16 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 63](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | Apr 20 | 22 | 1 | 4 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 4 | 3.03 (51) | 🚫 ABAND | ✗ FAIL |
| [CONV 64](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1199529522-1020989937-2582831627-1489170986?organization=assurantauto) | Apr 21 | 14 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — | ✓ PASS |
| [CONV 67](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1230494786-1215500785-2331767225-1659749027?organization=assurantauto) | May 06 | 16 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 69](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1253761027-1007948273-2591744523-1489170986?organization=assurantauto) | Apr 20 | 16 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4.37 (84) | — | ✓ PASS |
| [CONV 71](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1287515376-1220612593-2861032705-1638018563?organization=assurantauto) | May 06 | 28 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.17 (79) | — | ✓ PASS |
| [CONV 75](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | Apr 23 | 36 | 1 | 1 | 3 | 4 | 5 | 1 | 2 | 5 | 4 | 2 | 2.47 (37) | ⚠ SAFETY 🚫 ABAND | ✗ FAIL |
| [CONV 76](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1336807331-1215566321-2726028545-1638018563?organization=assurantauto) | May 06 | 15 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 77](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1372466417-1113985521-3101349281-0188171332?organization=assurantauto) | Apr 28 | 21 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 3 | 5 | 4.13 (78) | — | ✓ PASS |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | May 05 | 7 | 2 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.84 (71) | — | ✗ FAIL |
| [CONV 79](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | Apr 20 | 11 | 2 | 5 | 4 | 3 | 3 | 3 | 3 | 5 | 3 | 5 | 3.44 (61) | — | ✗ FAIL |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | May 05 | 7 | 2 | 5 | 2 | 5 | 5 | 2 | 3 | 5 | 5 | 5 | 3.66 (66) | — | ✗ FAIL |
| [CONV 84](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1549426158-1019941361-2830079032-0825805307?organization=assurantauto) | Apr 21 | 12 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.52 (88) | — | ✓ PASS |
| [CONV 85](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | Apr 21 | 21 | 1 | 4 | 4 | 3 | 5 | 4 | 4 | 5 | 4 | 5 | 3.48 (62) | — | ✗ FAIL |
| [CONV 86](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1598912222-1124798961-2387575274-2917985560?organization=assurantauto) | Apr 29 | 28 | 4 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 3 | 5 | 4.34 (84) | — | ✓ PASS |
| [CONV 87](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | May 05 | 4 | 2 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 3.81 (70) | — | ✗ FAIL |
| [CONV 88](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1616841208-1205473777-2344019201-1638018563?organization=assurantauto) | May 05 | 9 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.94 (74) | — | ✗ FAIL |
| [CONV 89](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1623904775-1046090225-2752442212-1336708325?organization=assurantauto) | Apr 23 | 23 | 3 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 2 | 5 | 3.87 (72) | — | ✗ FAIL |
| [CONV 90](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1656572716-1246237169-2481513729-1638018563?organization=assurantauto) | May 08 | 8 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 3.94 (74) | — | ✗ FAIL |
| [CONV 93](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1716235639-1217466865-2253907201-1638018563?organization=assurantauto) | May 06 | 22 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (78) | — | ✓ PASS |
| [CONV 94](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | Apr 28 | 19 | 2 | 5 | 3 | 4 | 5 | 3 | 3 | 5 | 4 | 4 | 3.57 (64) | — | ✗ FAIL |
| [CONV 95](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1777324209-1009717745-2750672740-1336708325?organization=assurantauto) | Apr 20 | 31 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 4 | 3.78 (69) | — | ✗ FAIL |
| [CONV 96](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | Apr 20 | 25 | 1 | 3 | 2 | 4 | 4 | 2 | 3 | 5 | 3 | 4 | 2.79 (45) | 🚫 ABAND | ✗ FAIL |
| [CONV 97](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1805304062-1245778417-2511466937-1659749027?organization=assurantauto) | May 08 | 17 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 98](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | Apr 22 | 9 | 1 | 4 | 4 | 5 | 4 | 2 | 3 | 5 | 3 | 4 | 3.23 (56) | 🚫 ABAND | ✗ FAIL |
| [CONV 100](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | Apr 28 | 18 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.62 (66) | — | ✗ FAIL |
| [CONV 101](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1899557711-1005195761-2954617355-1489170986?organization=assurantauto) | Apr 20 | 18 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — | ✓ PASS |
| [CONV 102](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1906412126-1230705137-3065570561-1638018563?organization=assurantauto) | May 07 | 22 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 106](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2013978248-1061687793-2688282468-1336708325?organization=assurantauto) | Apr 24 | 22 | 5 | 4 | 4 | 3 | 5 | 4 | 4 | 5 | 4 | 4 | 4.26 (81) | — | ✓ PASS |
| [CONV 107](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2018973679-1018434033-2801856356-1336708325?organization=assurantauto) | Apr 21 | 26 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 5 | 3 | 5 | 3.63 (66) | — | ✗ FAIL |
| [CONV 109](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2114974978-1150554609-2847773752-0825805307?organization=assurantauto) | May 01 | 16 | 4 | 5 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — | ✓ PASS |
| [CONV 110](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2131156183-1256985073-2414510570-2917985560?organization=assurantauto) | May 09 | 7 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 117](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2254763531-1101795825-2898957368-0825805307?organization=assurantauto) | Apr 27 | 15 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 4.48 (87) | — | ✓ PASS |
| [CONV 118](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | Apr 20 | 9 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3.42 (61) | — | ✗ FAIL |
| [CONV 120](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2303899210-1205670385-2694767873-1638018563?organization=assurantauto) | May 05 | 7 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4.44 (86) | — | ✗ FAIL |
| [CONV 121](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | Apr 23 | 26 | 1 | 4 | 3 | 4 | 3 | 2 | 2 | 5 | 4 | 4 | 2.92 (48) | 🚫 ABAND | ✗ FAIL |
| [CONV 122](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | Apr 28 | 16 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.62 (66) | — | ✗ FAIL |
| [CONV 123](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2349230954-1218318833-3154375097-1659749027?organization=assurantauto) | May 06 | 16 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 124](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2355214065-1153438193-2467140664-0825805307?organization=assurantauto) | May 01 | 18 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4.67 (92) | — | ✓ PASS |
| [CONV 125](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2364445645-1128272369-2147587128-0825805307?organization=assurantauto) | Apr 29 | 25 | 3 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 2 | 5 | 4.07 (77) | — | ✗ FAIL |
| [CONV 126](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2404003558-1221530097-2781406465-1638018563?organization=assurantauto) | May 06 | 29 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 127](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | Apr 22 | 22 | 1 | 5 | 3 | 5 | 3 | 1 | 2 | 5 | 2 | 4 | 2.96 (49) | 🚫 ABAND | ✗ FAIL |
| [CONV 128](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | Apr 18 | 10 | 1 | 5 | 3 | 4 | 3 | 2 | 2 | 5 | 3 | 5 | 3.09 (52) | — | ✗ FAIL |
| [CONV 129](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2503337876-1216549361-2839540153-1659749027?organization=assurantauto) | May 06 | 33 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 3.70 (67) | — | ✗ FAIL |
| [CONV 131](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | May 04 | 7 | 2 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 3.48 (62) | — | ✗ FAIL |
| [CONV 132](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2532578405-1207833073-2362893569-1638018563?organization=assurantauto) | May 05 | 10 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | — | ✗ FAIL |
| [CONV 135](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2566368638-1207112177-2240410041-1659749027?organization=assurantauto) | May 05 | 19 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.70 (67) | — | ✗ FAIL |
| [CONV 136](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2576713574-1126765041-2597093866-2917985560?organization=assurantauto) | Apr 29 | 23 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 3 | 5 | 4.53 (88) | — | ✓ PASS |
| [CONV 137](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2578512181-1220284913-3076973825-1638018563?organization=assurantauto) | May 06 | 17 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 138](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2590829860-1242763761-2835801345-1638018563?organization=assurantauto) | May 08 | 15 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 3.70 (67) | — | ✗ FAIL |
| [CONV 141](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2759451159-1230442993-2469654969-1659749027?organization=assurantauto) | May 07 | 26 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 142](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2761588534-1020727793-3067208203-1489170986?organization=assurantauto) | Apr 21 | 23 | 3 | 5 | 4 | 2 | 4 | 3 | 4 | 5 | 3 | 5 | 3.70 (67) | — | ✗ FAIL |
| [CONV 143](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2813330473-1022956017-2503729675-1489170986?organization=assurantauto) | Apr 21 | 18 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.17 (79) | — | ✓ PASS |
| [CONV 144](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | Apr 22 | 23 | 1 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 3.14 (54) | — | ✗ FAIL |
| [CONV 145](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | May 05 | 11 | 2 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 3.80 (70) | — | ✗ FAIL |
| [CONV 146](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2853825887-1207046641-2872111545-1659749027?organization=assurantauto) | May 05 | 11 | 3 | 4 | 3 | 4 | 4 | 2 | 3 | 5 | 4 | 4 | 3.51 (63) | — | ✗ FAIL |
| [CONV 147](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | Apr 29 | 19 | 1 | 5 | 3 | 5 | 5 | 2 | 2 | 5 | 2 | 5 | 3.32 (58) | 🚫 ABAND | ✗ FAIL |
| [CONV 148](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | Apr 21 | 21 | 1 | 3 | 4 | 3 | 5 | 4 | 3 | 5 | 5 | 4 | 3.26 (56) | — | ✗ FAIL |
| [CONV 149](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2980862308-1111953905-2636836708-1336708325?organization=assurantauto) | Apr 28 | 20 | 4 | 5 | 4 | 3 | 5 | 3 | 3 | 5 | 3 | 5 | 4.07 (77) | — | ✓ PASS |
| [CONV 150](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2998791010-1207898609-3150836153-1659749027?organization=assurantauto) | May 05 | 10 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.39 (85) | — | ✓ PASS |
| [CONV 151](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto) | May 06 | 15 | 1 | 3 | 3 | 5 | 4 | 2 | 2 | 5 | 3 | 4 | 2.96 (49) | 🚫 ABAND | ✗ FAIL |
| [CONV 153](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | Apr 22 | 21 | 2 | 3 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.51 (63) | — | ✗ FAIL |
| [CONV 155](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3073493438-1104220657-3090842090-2917985560?organization=assurantauto) | Apr 28 | 28 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — | ✓ PASS |
| [CONV 156](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3131072886-1018892785-2536825355-1489170986?organization=assurantauto) | Apr 21 | 25 | 4 | 5 | 5 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 4.50 (87) | — | ✓ PASS |
| [CONV 157](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3133496441-1192038897-2808607161-1659749027?organization=assurantauto) | May 04 | 16 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.83 (96) | — | ✓ PASS |
| [CONV 158](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | Apr 23 | 15 | 1 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 3.56 (64) | — | ✗ FAIL |
| [CONV 160](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3178654791-1243615729-2298209537-1638018563?organization=assurantauto) | May 08 | 18 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | 🚫 ABAND | ✗ FAIL |
| [CONV 161](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | Apr 27 | 22 | 1 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.51 (63) | — | ✗ FAIL |
| [CONV 162](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | Apr 22 | 13 | 1 | 4 | 3 | 3 | 3 | 2 | 2 | 5 | 4 | 4 | 2.81 (45) | — | ✗ FAIL |
| [CONV 163](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto) | May 08 | 7 | 1 | 4 | 3 | 5 | 3 | 2 | 3 | 5 | 3 | 4 | 3.03 (51) | — | ✗ FAIL |
| [CONV 165](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3244475956-1010242033-3188490730-2917985560?organization=assurantauto) | Apr 20 | 33 | 5 | 4 | 3 | 4 | 4 | 4 | 3 | 5 | 3 | 4 | 4.06 (76) | — | ✓ PASS |
| [CONV 166](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | May 05 | 30 | 3 | 2 | 3 | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 3.31 (58) | — | ✗ FAIL |
| [CONV 167](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3276343573-1207964145-3163874561-1638018563?organization=assurantauto) | May 05 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — | ✓ PASS |
| [CONV 168](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3299653061-1246237169-2277503417-1659749027?organization=assurantauto) | May 08 | 19 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | — | ✓ PASS |
| [CONV 169](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3315304968-1114444273-2240713784-0825805307?organization=assurantauto) | Apr 28 | 10 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4.56 (89) | — | ✓ PASS |
| [CONV 170](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3332361473-1008931313-2596204388-1336708325?organization=assurantauto) | Apr 20 | 20 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4.28 (82) | — | ✓ PASS |
| [CONV 175](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3417925909-0981406193-2828435946-2917985560?organization=assurantauto) | Apr 18 | 7 | 3 | 5 | 4 | 2 | 5 | 4 | 4 | 5 | 4 | 5 | 3.92 (73) | — | ✗ FAIL |
| [CONV 177](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3456065548-1018237425-3168961002-2917985560?organization=assurantauto) | Apr 21 | 25 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — | ✓ PASS |
| [CONV 179](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3468960017-1036521969-2878636522-2917985560?organization=assurantauto) | Apr 22 | 23 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — | ✓ PASS |
| [CONV 181](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3476134448-1215500785-2689000705-1638018563?organization=assurantauto) | May 06 | 12 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | — | ✓ PASS |
| [CONV 183](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | Apr 29 | 6 | 2 | 5 | 4 | 4 | 5 | 3 | 4 | 5 | 4 | 5 | 3.84 (71) | — | ✗ FAIL |
| [CONV 185](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3515729398-1124733425-3166999608-0825805307?organization=assurantauto) | Apr 29 | 14 | 3 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 3 | 5 | 4.12 (78) | — | ✗ FAIL |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3520813528-1242370545-3215585721-1659749027?organization=assurantauto) | May 08 | 12 | 2 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 5 | 3.59 (65) | 🚫 ABAND | ✗ FAIL |
| [CONV 187](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | May 04 | 7 | 2 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.72 (68) | — | ✗ FAIL |
| [CONV 189](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3592956096-1019941361-3199787531-1489170986?organization=assurantauto) | Apr 21 | 11 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — | ✓ PASS |
| [CONV 190](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3603763621-1246499313-3194807553-1638018563?organization=assurantauto) | May 08 | 20 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | — | ✓ PASS |
| [CONV 191](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3604895532-1046352369-2534506986-2917985560?organization=assurantauto) | Apr 23 | 18 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 4.44 (86) | — | ✓ PASS |
| [CONV 192](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3647451624-1047466481-2824721825-0188171332?organization=assurantauto) | Apr 23 | 20 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — | ✗ FAIL |
| [CONV 193](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3672476677-1207308785-2694705593-1659749027?organization=assurantauto) | May 05 | 20 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | — | ✓ PASS |
| [CONV 194](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3676613368-1139610097-2890826218-2917985560?organization=assurantauto) | Apr 30 | 19 | 3 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4.30 (82) | — | ✗ FAIL |
| [CONV 195](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3699588305-1100943857-2799342648-0825805307?organization=assurantauto) | Apr 27 | 20 | 3 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 4 | 4 | 3.90 (72) | — | ✗ FAIL |
| [CONV 196](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3723634684-1195381233-2170810809-1659749027?organization=assurantauto) | May 04 | 42 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 3 | 4 | 3.64 (66) | — | ✗ FAIL |
| [CONV 197](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3729246480-1020924401-2402083339-1489170986?organization=assurantauto) | Apr 21 | 11 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.83 (96) | — | ✓ PASS |
| [CONV 200](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3796968132-1207833073-2477712641-1638018563?organization=assurantauto) | May 05 | 23 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.17 (79) | — | ✓ PASS |
| [CONV 202](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | Apr 23 | 16 | 1 | 5 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 5 | 3.28 (57) | — | ✗ FAIL |
| [CONV 204](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3871431063-1195053553-2645066218-2917985560?organization=assurantauto) | May 04 | 20 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4.11 (78) | — | ✓ PASS |
| [CONV 205](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3877927423-1141641713-2624881130-2917985560?organization=assurantauto) | Apr 30 | 31 | 3 | 4 | 3 | 5 | 5 | 3 | 3 | 5 | 3 | 5 | 3.84 (71) | — | ✗ FAIL |
| [CONV 208](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4029491569-1232146929-2212357377-1638018563?organization=assurantauto) | May 07 | 19 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 209](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4055395116-1247023601-2881286585-1659749027?organization=assurantauto) | May 08 | 21 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | — | ✓ PASS |
| [CONV 210](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4080665955-1207046641-3021074873-1659749027?organization=assurantauto) | May 05 | 7 | 3 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 4 | 5 | 4.01 (75) | — | ✗ FAIL |
| [CONV 212](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | Apr 22 | 40 | 2 | 4 | 3 | 4 | 5 | 3 | 3 | 5 | 3 | 5 | 3.51 (63) | — | ✗ FAIL |
| [CONV 213](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4148517809-1232540145-2605376769-1638018563?organization=assurantauto) | May 07 | 21 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — | ✓ PASS |
| [CONV 214](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4156083984-1245057521-3139233025-1638018563?organization=assurantauto) | May 08 | 18 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | — | ✓ PASS |
| [CONV 215](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4179586080-1206325745-3092374785-1638018563?organization=assurantauto) | May 05 | 9 | 3 | 4 | 4 | 2 | 4 | 4 | 4 | 5 | 4 | 4 | 3.61 (65) | — | ✗ FAIL |
| [CONV 216](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4182611759-1059590641-3188888632-0825805307?organization=assurantauto) | Apr 24 | 20 | 3 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.09 (77) | — | ✗ FAIL |
| [CONV 217](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | Apr 27 | 7 | 1 | 5 | 5 | 4 | 5 | 1 | 1 | 5 | 4 | 4 | 3.30 (57) | 🚫 ABAND | ✗ FAIL |
| [CONV 218](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4272166275-1059459569-2422309354-2917985560?organization=assurantauto) | Apr 24 | 17 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — | ✓ PASS |

---

## Section 5: Flagged Conversations
*Criteria: any override flag, overall score < 2.5/5, D1 ≤ 2, or D12 ≤ 2*

| Conv | Date | Conv ID | Score | D1 | D12 | Flags | Note |
|------|------|---------|-------|----|-----|-------|------|
| [CONV 75](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | Apr 23 | [`1328754597-1046811121-2704338788-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | 2.47 (37/100) | 1 | 2 | SAFETY, ABANDONED | CRITICAL: Bot leaked internal queue-status prompt to customer — fundamental… |
| [CONV 96](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | Apr 20 | [`1794270454-1005261297-2430042602-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | 2.79 (45/100) | 1 | 4 | ABANDONED | Customer never authenticated; bot repeated 'I wasn't able to find a record'… |
| [CONV 162](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | Apr 22 | [`3218327297-1031606769-2176380772-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | 2.81 (45/100) | 1 | 4 | — | Bot responded to opening 'Representative' with 'I'm unable to assist furthe… |
| [CONV 121](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | Apr 23 | [`2307801813-1045041649-2903409130-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | 2.92 (48/100) | 1 | 4 | ABANDONED | Agent queue unavailable: repair facility stuck in loop; bot offered email/p… |
| [CONV 127](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | Apr 22 | [`2425241405-1034621425-2596859748-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | 2.96 (49/100) | 1 | 4 | ABANDONED | Bot failed 6+ 'speak with representative' requests; 'rep' heard as 'rent'; … |
| [CONV 151](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto) | May 06 | [`3014101863-1221005809-2288644537-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto) | 2.96 (49/100) | 1 | 4 | ABANDONED | CRITICAL: 'Insurance' caller type unclassified; bot said 'unable to assist'… |
| [CONV 63](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | Apr 20 | [`1198705778-1010242033-2904588778-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | 3.03 (51/100) | 1 | 4 | ABANDONED | Dealer wanted phone agent; bot ended call with farewell despite explicit ph… |
| [CONV 163](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto) | May 08 | [`3223725281-1247023601-2808738233-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto) | 3.03 (51/100) | 1 | 4 | — | Repair facility repeatedly asked for representative; bot kept asking to cla… |
| [CONV 128](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | Apr 18 | [`2438618780-0981471729-2907041636-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | 3.09 (52/100) | 1 | 5 | — | Bot said goodbye while customer actively requesting an operator; transcript… |
| [CONV 11](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | Apr 22 | [`0251497861-1035014641-2786717540-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | 3.11 (53/100) | 1 | 5 | — | Bot failed to recognize repeated 'representative' requests; likely failed t… |
| [CONV 144](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | Apr 22 | [`2817014493-1031541233-3068695608-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | 3.14 (54/100) | 1 | 4 | — | Bot initially stated it couldn't connect to a representative (incorrect); C… |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | Apr 22 | [`0348917324-1031606769-3098931044-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | 3.18 (54/100) | 1 | 4 | HALLUCINATION | Bot falsely told customer 'you're already being connected to a representati… |
| [CONV 98](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | Apr 22 | [`1851846244-1034490353-2169410616-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | 3.23 (56/100) | 1 | 4 | ABANDONED | Spanish-speaking caller unable to get service; bot just repeated English-on… |
| [CONV 148](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | Apr 21 | [`2914676966-1017778673-2571366244-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | 3.26 (56/100) | 1 | 4 | — | Bot told customer to 'call 1-800-621-2130' while already on the phone; cust… |
| [CONV 202](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | Apr 23 | [`3822848610-1045697009-3058598378-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | 3.28 (57/100) | 1 | 5 | — | Dealer repeatedly said 'speak with rep'; bot kept asking for purpose; trans… |
| [CONV 217](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | Apr 27 | [`4223284239-1103761905-2187063140-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | 3.30 (57/100) | 1 | 4 | ABANDONED | Customer asked for representative; bot offered chat, customer declined, bot… |
| [CONV 166](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | May 05 | [`3260951102-1205473777-2699620793-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | 3.31 (58/100) | 3 | 4 | — | Long complex call with garbled customer responses; eventually escalated. Mu… |
| [CONV 147](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | Apr 29 | [`2883648572-1128337905-2480247864-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | 3.32 (58/100) | 1 | 5 | ABANDONED | 'Plain number' ASR; 'Customer service' repeated transfer intent not recogni… |
| [CONV 118](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | Apr 20 | [`2266244334-1008996849-2518802955-1489170986`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | 3.42 (61/100) | 2 | 4 | — | Coverage question redirected to portal text; call ended without coverage an… |
| [CONV 79](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | Apr 20 | [`1461535746-1010962929-2700776504-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | 3.44 (61/100) | 2 | 5 | — | Customer confused after contract selection; bot offered website before iden… |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0797214453-1234637297-3210670521-1659749027?organization=assurantauto) | May 07 | [`0797214453-1234637297-3210670521-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0797214453-1234637297-3210670521-1659749027?organization=assurantauto) | 3.48 (62/100) | 2 | 4 | — | Repair facility repeatedly asked for agent ('please don't give me a hard ti… |
| [CONV 85](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | Apr 21 | [`1588261601-1022497265-2402279947-1489170986`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | 3.48 (62/100) | 1 | 5 | — | Dealer's VIN not found in system; call ended without resolution or alternat… |
| [CONV 131](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | May 04 | [`2521437428-1192301041-2215965113-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | 3.48 (62/100) | 2 | 5 | — | Broken-down car customer received scripted dealer info but no roadside tran… |
| [CONV 132](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2532578405-1207833073-2362893569-1638018563?organization=assurantauto) | May 05 | [`2532578405-1207833073-2362893569-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2532578405-1207833073-2362893569-1638018563?organization=assurantauto) | 3.48 (62/100) | 3 | 4 | — | Contract number lookup failed; bot fell back to VIN; call ended mid-collect… |
| [CONV 160](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3178654791-1243615729-2298209537-1638018563?organization=assurantauto) | May 08 | [`3178654791-1243615729-2298209537-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3178654791-1243615729-2298209537-1638018563?organization=assurantauto) | 3.48 (62/100) | 2 | 4 | ABANDONED | Customer indicated answer didn't help ('No') but bot ended call instead of … |
| [CONV 153](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | Apr 22 | [`3035186604-1033048561-2998768696-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | 3.51 (63/100) | 2 | 4 | — | Repair facility sent RO email but never received case number; bot's '2-minu… |
| [CONV 161](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | Apr 27 | [`3186447997-1100943857-2550001508-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | 3.51 (63/100) | 1 | 5 | — | VIN not found; bot said goodbye while dealer still needed help. |
| [CONV 212](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | Apr 22 | [`4141745400-1034949105-2328794168-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | 3.51 (63/100) | 2 | 5 | — | Multiple lookup failures; coverage question unanswered; bot confused by cal… |
| [CONV 158](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | Apr 23 | [`3165613731-1049694705-2283639864-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | 3.56 (64/100) | 1 | 5 | — | 'Viewership' ASR artifact for 'dealership'; customer declined to provide id… |
| [CONV 94](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | Apr 28 | [`1761050634-1111429617-2851139428-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | 3.57 (64/100) | 2 | 4 | — | Call ended mid-collection; bot idled with 'I am still here'. |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3520813528-1242370545-3215585721-1659749027?organization=assurantauto) | May 08 | [`3520813528-1242370545-3215585721-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3520813528-1242370545-3215585721-1659749027?organization=assurantauto) | 3.59 (65/100) | 2 | 5 | ABANDONED | Customer asked for rep but bot answered specific question instead; customer… |
| [CONV 100](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | Apr 28 | [`1894537135-1114247665-2518254058-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | 3.62 (66/100) | 2 | 4 | — | Same email-RO dead-end as CONV 110; call ended waiting for case number. |
| [CONV 122](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | Apr 28 | [`2335431778-1111691761-2532938808-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | 3.62 (66/100) | 2 | 4 | — | Same pattern as CONV 70; email RO dead-end; claim not started. |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | Apr 27 | [`0140238296-1100943857-2505086008-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | 3.64 (66/100) | 1 | 5 | — | Dealer VIN not found; no alternative offered; call ended without resolution… |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | May 05 | [`1484095264-1208488433-2566382849-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | 3.66 (66/100) | 2 | 5 | — | Bot claimed account was pulled up then asked for caller type; coverage ques… |
| [CONV 187](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | May 04 | [`3542794834-1192235505-2815923256-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | 3.72 (68/100) | 2 | 4 | — | Customer requested rep up front; bot quickly identified caller type and tra… |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | May 05 | [`0212455871-1207046641-2586046905-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | 3.73 (68/100) | 2 | 5 | — | Bot claimed account was pulled up but then asked for caller type; no transf… |
| [CONV 145](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | May 05 | [`2838792712-1209143793-2204820737-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | 3.80 (70/100) | 2 | 4 | — | Tow request mid-flow; bot handled S→F contract number correction well; conv… |
| [CONV 87](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | May 05 | [`1601360915-1207898609-2646140161-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | 3.81 (70/100) | 2 | 5 | — | Bot immediately provided claim-filing instructions without gathering identi… |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | May 05 | [`1391865844-1207046641-2711220665-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | 3.84 (71/100) | 2 | 5 | — | Call ended mid-identification after phone lookup failed; customer's stated … |
| [CONV 183](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | Apr 29 | [`3498885050-1127289329-3031209016-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | 3.84 (71/100) | 2 | 5 | — | Call ended prematurely during CallerID after dealer identified; goal not ac… |
| [CONV 29](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | May 01 | [`0612002884-1154617841-2360316984-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | 4.13 (78/100) | 2 | 5 | — | Very clean — immediate transfer upon agent request with no friction. |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | May 04 | [`0445586395-1192759793-3072623082-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | 4.33 (83/100) | 2 | 5 | — | Immediate clean transfer upon rep request. |

---

## Section 6: Representative Examples

### Highest scorer: CONV 40 — 5.00/5 (100/100)
**Conv ID:** [`0839037409-1112805873-2891284970-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0839037409-1112805873-2891284970-2917985560?organization=assurantauto)  
**Date:** 2026-04-28  |  **Tasks:** CallerIdentification, DealershipIssues  
**Assessment:** Excellent: payment status provided; smooth efficient transfer.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! How can I help you today?
  Customer: Speak to representative.
  Talker: Understood, please hold.
  Talker: To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Dealer calling about claim payment.
  Talker: One moment please.
  Talker: Can you provide the claim number, contract number, or the last eight characters of the vehicle's Vin?
  Customer: Claim number.
  Talker: Please provide the claim number.
  Customer: Four nine two one six three five seven
  Talker: Let me check on that.
  Talker: Just to be sure, you gave me four, nine, two. one, six, three. five, seven as your claim number. Is that correct?
  Customer: Yes.
  Talker: Great! One moment please.
  Talker: This claim was paid via credit card and sent to the email address or fax associated with the claim submission. Does that answer your question, or is there something else I can help with?
  Customer: Speak to representative.
  Talker: Understood, please hold.
  Talker: Hold on while I transfer you to an Agent.
```

### Most notable failure: CONV 124 — 4.67/5 (92/100)
**Conv ID:** [`2355214065-1153438193-2467140664-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2355214065-1153438193-2467140664-0825805307?organization=assurantauto)  
**Date:** 2026-05-01  |  **Tasks:** CallerIdentification, ContractHolderIssues  
**Assessment:** Smooth flow: VIN-based lookup, vehicle identified, claim payment status provided, contract number disclosure on request.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Customer.
  Talker: One moment please.
  Talker: I wasn't able to find a record with your phone number. Can you provide the claim number, contract number, or the last eight characters of the vehicle's V, I, N?
  Customer: Yeah. Looks like the the VIN is g r three one three zero three three.
  Talker: Perfect! One moment please.
  Talker: Just to be sure, you gave me g, r, three, one, three, zero, three, three as your V, I, {pii_immediate_genagent_persistence.PERSON:**} Is that correct?
  Customer: Yes.
  Talker: Great! One moment please.
  Talker: I'm checking any contracts or claims you may have with us
  Talker: I can see you have a two thousand sixteen Dodge Grand Caravan on file. What specific help do you need today? For example, is it about a mechanical repair, claim status, contract questions, coverage, roadside assistance, rental car, or something else?
  Customer: Yeah. I think I have a claim on this contract.
  Talker: Thanks! Let me check on that for you.
  Talker: A payment was issued to your repair facility. If you need additional information, you may contact your repair facility. Does that answer your question?
  Customer: No. What's my contract number?
  Talker: Understood, let me check on that.
  Talker: Your contract number for the two thousand sixteen Dodge Grand Caravan is A U A 6 A 1 1 1 6 6 E. Is there anything else I can assist with?
  Customer: No. That's all.
```

### Lowest scorer: CONV 75 — 2.47/5 (37/100)
**Conv ID:** [`1328754597-1046811121-2704338788-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto)  
**Date:** 2026-04-23  |  **Tasks:** CallerIdentification, RepairShopIssues  
**Flags:** SAFETY_VIOLATION, ABANDONED  
**Assessment:** CRITICAL: Bot leaked internal queue-status prompt to customer — fundamental system failure.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! How can I help you today?
  Customer: Checking status on existing claim.
  Talker: One moment please.
  Talker: To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Independent repair facility.
  Talker: Let me check on that.
  Talker: Before we get started, there is an online portal where independent repair facilities like yours can file claims, check claim status, provide documentation, and check payment status. The portal website is auto claims dot com. If you don't want to use that option, I'm here to help — what can I do for you today?
  Customer: Checking status of existing claim.
  Talker: Just a second.
  Talker: Can you provide the claim number, contract number, or the last eight characters of the vehicle's Vin?
  Customer: Claim number is four nine two four two two six
  Talker: Let me check on that.
  Talker: Thank you. Is that your claim number, your contract number, or the last eight characters of your Vin?
  Customer: Claim number
  Talker: One moment please.
  Talker: Just to be sure, you gave me four, nine, two, four, two, two, six as your claim number. Is that correct?
  Customer: No.
  Talker: Could you please confirm the correct claim number?
  Customer: Four nine two four two two six six
  Talker: Let me check on that.
  Talker: Just to be sure, you gave me four, nine, two, four, two, two, six, six as your claim number. Is that correct?
  Customer: Yes.
  Talker: Perfect! One moment please.
  Talker: This claim is under review and will be adjudicated in the order received. Does that answer your question, or is there something else I can help with?
  Customer: No. need to speak with an adjuster.
  Talker: Let me check on that.
  Talker: All of our websites have chat available, and our agents are ready to assist you with no wait. Would you like to try our online chat support first?
  Customer: No.
  Talker: Hold on please.
  Talker: Could you please confirm if the following queues are currently open: customer service, claims, payment, premium, and R V?
  Customer: claims
  Talker: Let me check on that.
  Talker: Could you please confirm if the following queues are open: customer service, payment, premium, and R V?
  Customer: Adjuster.
  Talker: Let me check on that.
  Talker: I still need to know if the customer service, payment, premium, and R V queues are currently open. Can you confirm the status for each?
```

---

## Section 7: Systemic Issues Identified

The following patterns recur across multiple conversations and represent systemic rather than isolated failures.

### Issue 1 — 'Claim' / 'VIN' ASR Failures *(High Severity)*
*Weekly distribution (excluding Apr 17): Wk16=0, Wk17=3, Wk18=4, Wk19=2 — **persistent in Wk17–19**, no improvement trend.*
Core vocabulary is consistently misheard:
- **'claim'** → 'flame', 'lame', 'plain', 'piece', 'plane' (CONV 89, 102, 158, 177, 180 and others)
- **'VIN'** / **'VIN number'** → **'thin'** (CONV 85, 102, 151) — repeating artifact affecting VIN collection
- **'repair facility'** → 'Repurfacin' (CONV 117) — understood from context but ASR artifact
For a service whose primary function is claim handling and caller identification, failure to reliably transcribe these core vocabulary terms is a critical ASR gap.

### Issue 2 — Agent Queue Unavailability With No Fallback *(High Severity)*
*Weekly distribution (excluding Apr 17): Wk16=0, Wk17=1, Wk18=0, Wk19=0 — **single instance in retained data**, may have stopped recurring.*
When agent queues are closed, the bot has no graceful fallback beyond business hours info. In CONV 121 this produced an infinite loop offering email/portal options the caller had already refused. A callback scheduling option or clearer escalation path is needed. *(Two earlier Apr 17 instances of queue-closed handling were excluded along with the rest of that day.)*

### Issue 3 — Transfer Intent Not Recognized *(Medium-High Severity)*
*Weekly distribution: Wk16=1, Wk17=5, Wk18=2, Wk19=0 — **peaked in Wk17 (Apr 20-26)**, declining since.*
Callers requesting 'representative', 'agent', or 'operator' were repeatedly asked to clarify intent first (CONV 11, 103, 104, 121, 127, 162, 163). In CONV 117 the bot explicitly said it couldn't connect to a representative directly. Callers voicing an explicit transfer request should trigger a transfer, not a disambiguation prompt.

### Issue 4 — Chat Upsell Before Phone Transfer *(Low-Medium Severity)*
*Weekly distribution: present in **all weeks** — systemic Portal Self-Service Nudge applied even when caller has already requested phone agent.*
In ~60% of phone-transfer flows the bot offered website/chat alternatives before transferring. Callers who have already said 'phone agent' or 'representative' are not a good chat upsell audience; this pattern adds turns and creates friction.

### Issue 5 — Email RO Dead-End for Repair Facilities *(Medium Severity)*
*Weekly distribution: Wk17=1, Wk18=2, Wk19=0 — **clustered in Wk17-18**.*
Repair facilities that submitted an RO via email but have not yet received a case number (CONV 100, 122, 153) are sent into a dead-end: the bot asks for the case number, they don't have it, and the call ends unresolved. An alternative lookup path (by RO number, shop phone, or date) is needed.

### Issue 6 — Internal Prompt Leakage *(Critical — CONV 75 only)*
*Weekly distribution: Wk17 only (1 instance, Apr 23) — **single occurrence**, severity critical.*
CONV 75 exhibits a fundamental system failure: the bot asked the customer to confirm the status of internal agent queues ('Could you please confirm if customer service, claims, payment, premium, and RV queues are currently open?'). This internal routing instruction was exposed directly to the caller. Requires immediate root-cause investigation.

### Issue 7 — PII Template Tags *(Not an issue — post-conversation database artifact)*
Tags such as `{pii_immediate_genagent_persistence.PERSON:**}` appear in the database transcript only — they are applied during post-conversation redaction and are NOT what the caller heard. Previously flagged conversations (CONV 41, 106, 111, 143, 167) have been re-scored.

### Issue 8 — False Transfer Confirmation *(Critical — CONV 17 only)*
*Weekly distribution: Wk17 only (1 instance, Apr 22) — **single occurrence**, severity critical.*
Bot told the customer 'You're already being connected to a representative' when no transfer occurred. The call ended with a farewell greeting — a trust-breaking hallucination that leaves the caller without a callback.

### Issue 9 — No Spanish Language Support or Escalation Path *(Medium Severity — CONV 98 only so far)*
*Weekly distribution: Wk17 only (1 instance, Apr 22) — **single sample**, indicative of a population gap.*
A Spanish-speaking caller (CONV 98, Apr 22) was unable to get service. The bot repeated 'I'm here to assist you in English' with no offer to escalate to a Spanish-speaking agent. If the caller population includes Spanish speakers, an escalation path or language detection handoff is needed.

### Issue 10 — 'Account Pulled Up' Greeting Then Re-Asks for Caller Type *(Low Severity)*
*Weekly distribution: Wk19 only (2 instances, May 5) — **new pattern emerging in latest week**, may indicate a recent prompt change.*
When the bot uses the personalized greeting 'I have your account information pulled up' (recognized phone number), it then re-asks for caller type (customer/dealer/repair facility), creating a confusing inconsistency (CONV 9, 84). If the account is known, the caller type should be inferred or skipped.
