## Batch Quality Report — CallerIdentification
*Updated 2026-05-07 (v2): D1 redefined as 'Design Adherence' against task configs. PII redaction tags treated as post-conversation database artifacts (not real PII leaks) — 5 conversations re-scored. Added daily-trend chart and per-issue weekly distribution.*
Conversations analyzed: 191  |  Scored: 112  |  Skipped (no customer turns): 79  |  Date: 2026-05-07

| Metric | Value |
|---|---|
| Mean overall score (scored convs) | 3.99 / 5 (75/100) |
| Conversations scoring < 3.0 | 5 (4%) |
| Safety / policy flags | 1 |
| Critical hallucination flags | 1 |
| Abandoned calls | 8 (7%) |
| Human transfers (all 191) | 123 (64%) |

---

## Section 2: Week-over-Week Trend
*ISO weeks. Scored conversations only. Single-turn calls with no customer transcript excluded.*

| Week | Dates | Scored | Mean Score | Score /100 | % < 3.0 | Abandoned | D1 Mean | D10 Mean |
|------|-------|--------|------------|------------|---------|-----------|---------|----------|
| Wk 16 (Apr 14–18) | 2026-04-17 – 2026-04-18 | 11 | 4.25 / 5 | 81 | 0 (0%) | 0 | 4.09 | 4.00 |
| Wk 17 (Apr 21–27) | 2026-04-20 – 2026-04-24 | 43 | 3.84 / 5 | 71 | 5 (12%) | 6 | 2.79 | 3.84 |
| Wk 18 (Apr 28–May 4) | 2026-04-27 – 2026-05-01 | 27 | 4.08 / 5 | 77 | 0 (0%) | 2 | 3.00 | 3.89 |
| Wk 19 (May 5–11) | 2026-05-04 – 2026-05-05 | 31 | 4.04 / 5 | 76 | 0 (0%) | 0 | 3.26 | 4.10 |

---

## Section 2.5: Daily Score Trend
*Mean weighted score per day (scored conversations only). Single-turn calls excluded.*

| Date | N | Mean /5 | /100 | Trend |
|------|---|---------|------|-------|
| 2026-04-17 | 9 | 4.42 | 85 | █████████████████████████ |
| 2026-04-18 | 2 | 3.51 | 63 | ██████████████████ |
| 2026-04-20 | 10 | 3.83 | 71 | █████████████████████ |
| 2026-04-21 | 12 | 4.20 | 80 | ███████████████████████ |
| 2026-04-22 | 9 | 3.34 | 59 | █████████████████ |
| 2026-04-23 | 9 | 3.71 | 68 | ████████████████████ |
| 2026-04-24 | 3 | 4.29 | 82 | ████████████████████████ |
| 2026-04-27 | 5 | 3.77 | 69 | ████████████████████ |
| 2026-04-28 | 9 | 4.10 | 77 | ███████████████████████ |
| 2026-04-29 | 6 | 4.04 | 76 | ██████████████████████ |
| 2026-04-30 | 3 | 4.17 | 79 | ███████████████████████ |
| 2026-05-01 | 4 | 4.44 | 86 | █████████████████████████ |
| 2026-05-04 | 9 | 4.01 | 75 | ██████████████████████ |
| 2026-05-05 | 22 | 4.05 | 76 | ██████████████████████ |

**Observations:**
- The lowest-scoring day is **Apr 22 (3.34/5)**, driven by 5 of the 8 transfer-intent failures plus the only Spanish-speaker abandonment (CONV 81), the only false-transfer hallucination (CONV 15), and CONV 108 (failed 6+ rep requests).
- The highest-scoring days are **Apr 17 (4.42)** and **May 1 (4.44)**, driven by clean denied-claim escalations and roadside transfers.
- Day-by-day variance is high (3.34 to 4.44); daily traffic mix matters more than any week-level trend.
- May 5 is the largest single day (N=22) and sits at the population mean — recent volume may reflect a launch ramp.

## Section 3: Dimension Heatmap
*Sorted by % scoring ≤ 2 (worst first). D7 and D11 require audio — N/A.*

| Dim | Name | Weight | Mean | Std | Min | Max | % ≤ 2 |
|-----|------|--------|------|-----|-----|-----|-------|
| D1 | Design Adherence | 20% | 3.10 | 1.31 | 1 | 5 | 32% |
| D6 | Repair & Recovery | 7% | 3.66 | 0.94 | 1 | 5 | 10% |
| D8 | Tone Appropriateness | 5% | 3.64 | 0.75 | 1 | 5 | 6% |
| D10 | ASR/Spoken Language | 5% | 3.94 | 0.85 | 2 | 5 | 4% |
| D2 | Information Accuracy | 10% | 4.45 | 0.75 | 1 | 5 | 3% |
| D3 | Context Retention | 10% | 4.04 | 0.75 | 2 | 5 | 2% |
| D4 | Response Latency | 10% | 4.29 | 0.74 | 2 | 5 | 2% |
| D12 | Policy & Safety | 10% | 4.61 | 0.54 | 2 | 5 | 1% |
| D5 | Turn-Taking | 8% | 4.44 | 0.67 | 3 | 5 | 0% |
| D9 | Verbosity | 5% | 4.90 | 0.35 | 3 | 5 | 0% |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 4: Per-Conversation Scores
*All 112 conversations with substantive transcripts. Single-turn calls excluded.*
*D4 and D9 are auto-computed from timestamps/word counts. D7 and D11 require audio.*

| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | Flags |
|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-------|
| [CONV 1](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0008094092-1111757297-2660275256-0825805307?organization=assurantauto) | Apr 28 | 30 | 3 | 5 | 4 | 3 | 4 | 4 | 4 | 5 | 3 | 5 | 3.89 (72) | — |
| [CONV 4](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0115003615-1207964145-2886329601-1638018563?organization=assurantauto) | May 05 | 6 | 4 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.92 (73) | — |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | Apr 27 | 20 | 1 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 3.64 (66) | — |
| [CONV 6](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0195488489-1011028465-3000800312-0825805307?organization=assurantauto) | Apr 20 | 18 | 3 | 5 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 3.94 (74) | — |
| [CONV 7](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0200416497-1049760241-2169995754-2917985560?organization=assurantauto) | Apr 23 | 17 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | — |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | May 05 | 5 | 2 | 5 | 3 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.73 (68) | — |
| [CONV 10](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | Apr 22 | 28 | 1 | 3 | 4 | 4 | 3 | 3 | 3 | 5 | 3 | 5 | 3.11 (53) | — |
| [CONV 14](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0333763583-1193415153-2807464426-2917985560?organization=assurantauto) | May 04 | 13 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4.00 (75) | — |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | Apr 22 | 14 | 1 | 2 | 4 | 5 | 5 | 3 | 3 | 5 | 3 | 4 | 3.18 (54) | ⚠ HALLUC |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | May 04 | 5 | 2 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4.33 (83) | — |
| [CONV 19](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0482211455-1150947825-2550392065-1638018563?organization=assurantauto) | May 01 | 28 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0490543454-1024004593-2737237860-1336708325?organization=assurantauto) | Apr 21 | 20 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | May 01 | 8 | 2 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4.13 (78) | — |
| [CONV 26](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0769152030-1195315697-2760631553-1638018563?organization=assurantauto) | May 04 | 26 | 3 | 5 | 3 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 3.92 (73) | — |
| [CONV 29](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0776533978-1143017969-2437280185-1659749027?organization=assurantauto) | Apr 30 | 20 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 4.37 (84) | — |
| [CONV 30](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0795050560-1204490737-3136061930-2917985560?organization=assurantauto) | May 05 | 31 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4.48 (87) | — |
| [CONV 32](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0839037409-1112805873-2891284970-2917985560?organization=assurantauto) | Apr 28 | 19 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — |
| [CONV 33](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0859768425-1207112177-2833442049-1638018563?organization=assurantauto) | May 05 | 24 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (78) | — |
| [CONV 35](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0878025181-1209209329-2674651577-1659749027?organization=assurantauto) | May 05 | 23 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — |
| [CONV 36](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0906932620-1045303793-2487850040-0825805307?organization=assurantauto) | Apr 23 | 30 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.31 (83) | — |
| [CONV 41](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1015743628-1207964145-2279928249-1659749027?organization=assurantauto) | May 05 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — |
| [CONV 42](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1031176323-0970985969-2332418571-1489170986?organization=assurantauto) | Apr 17 | 16 | 5 | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 4 | 5 | 4.60 (90) | — |
| [CONV 44](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1047909769-0960172529-2723779640-0825805307?organization=assurantauto) | Apr 17 | 25 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4.37 (84) | — |
| [CONV 48](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1112326957-1194463729-2387469569-1638018563?organization=assurantauto) | May 04 | 26 | 3 | 5 | 4 | 5 | 4 | 3 | 4 | 5 | 3 | 5 | 4.03 (76) | — |
| [CONV 51](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | Apr 20 | 36 | 1 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.26 (56) | 🚫 ABAND |
| [CONV 52](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1199529522-1020989937-2582831627-1489170986?organization=assurantauto) | Apr 21 | 15 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — |
| [CONV 53](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1203740802-0968430065-2656862698-2917985560?organization=assurantauto) | Apr 17 | 33 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4.48 (87) | — |
| [CONV 57](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1253761027-1007948273-2591744523-1489170986?organization=assurantauto) | Apr 20 | 26 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4.48 (87) | — |
| [CONV 61](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | Apr 23 | 37 | 1 | 1 | 3 | 4 | 5 | 1 | 2 | 5 | 4 | 2 | 2.47 (37) | ⚠ SAFETY 🚫 ABAND |
| [CONV 62](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1372466417-1113985521-3101349281-0188171332?organization=assurantauto) | Apr 28 | 22 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 3 | 5 | 4.13 (78) | — |
| [CONV 63](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | May 05 | 8 | 2 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.84 (71) | — |
| [CONV 64](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | Apr 20 | 12 | 2 | 5 | 4 | 3 | 3 | 3 | 3 | 5 | 3 | 5 | 3.44 (61) | — |
| [CONV 65](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | May 05 | 8 | 2 | 5 | 2 | 5 | 5 | 2 | 3 | 5 | 5 | 5 | 3.66 (66) | — |
| [CONV 69](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1549426158-1019941361-2830079032-0825805307?organization=assurantauto) | Apr 21 | 13 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.52 (88) | — |
| [CONV 70](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | Apr 21 | 22 | 1 | 4 | 4 | 3 | 5 | 4 | 4 | 5 | 4 | 5 | 3.48 (62) | — |
| [CONV 71](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1598912222-1124798961-2387575274-2917985560?organization=assurantauto) | Apr 29 | 29 | 4 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 3 | 5 | 4.34 (84) | — |
| [CONV 72](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | May 05 | 5 | 2 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 3.81 (70) | — |
| [CONV 73](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1616841208-1205473777-2344019201-1638018563?organization=assurantauto) | May 05 | 14 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.94 (74) | — |
| [CONV 74](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1623904775-1046090225-2752442212-1336708325?organization=assurantauto) | Apr 23 | 24 | 3 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 2 | 5 | 3.87 (72) | — |
| [CONV 75](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1654575390-0960303601-3055346187-1489170986?organization=assurantauto) | Apr 17 | 20 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4.80 (95) | — |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | Apr 28 | 20 | 2 | 5 | 3 | 4 | 5 | 3 | 3 | 5 | 4 | 4 | 3.57 (64) | — |
| [CONV 79](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1777324209-1009717745-2750672740-1336708325?organization=assurantauto) | Apr 20 | 45 | 3 | 4 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | 4 | 3.89 (72) | — |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | Apr 20 | 31 | 1 | 3 | 2 | 5 | 4 | 2 | 3 | 5 | 3 | 4 | 2.90 (47) | 🚫 ABAND |
| [CONV 81](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | Apr 22 | 10 | 1 | 4 | 4 | 5 | 4 | 2 | 3 | 5 | 3 | 4 | 3.23 (56) | 🚫 ABAND |
| [CONV 83](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | Apr 28 | 19 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.62 (66) | — |
| [CONV 84](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1899557711-1005195761-2954617355-1489170986?organization=assurantauto) | Apr 20 | 19 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — |
| [CONV 89](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2013978248-1061687793-2688282468-1336708325?organization=assurantauto) | Apr 24 | 34 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4.48 (87) | — |
| [CONV 90](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2018973679-1018434033-2801856356-1336708325?organization=assurantauto) | Apr 21 | 27 | 3 | 4 | 3 | 4 | 3 | 4 | 3 | 5 | 3 | 5 | 3.63 (66) | — |
| [CONV 92](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2088980478-0960434673-2441408356-1336708325?organization=assurantauto) | Apr 17 | 25 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4.42 (86) | — |
| [CONV 93](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2114974978-1150554609-2847773752-0825805307?organization=assurantauto) | May 01 | 17 | 4 | 5 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — |
| [CONV 100](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2254763531-1101795825-2898957368-0825805307?organization=assurantauto) | Apr 27 | 16 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 4.48 (87) | — |
| [CONV 101](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | Apr 20 | 14 | 2 | 4 | 4 | 5 | 4 | 3 | 3 | 3 | 4 | 4 | 3.48 (62) | — |
| [CONV 103](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2303899210-1205670385-2694767873-1638018563?organization=assurantauto) | May 05 | 8 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4.44 (86) | — |
| [CONV 104](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | Apr 23 | 27 | 1 | 4 | 3 | 4 | 3 | 2 | 2 | 5 | 4 | 4 | 2.92 (48) | 🚫 ABAND |
| [CONV 105](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | Apr 28 | 17 | 2 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.62 (66) | — |
| [CONV 106](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2355214065-1153438193-2467140664-0825805307?organization=assurantauto) | May 01 | 19 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4.67 (92) | — |
| [CONV 107](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2364445645-1128272369-2147587128-0825805307?organization=assurantauto) | Apr 29 | 26 | 3 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 2 | 5 | 4.07 (77) | — |
| [CONV 108](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | Apr 22 | 23 | 1 | 5 | 3 | 5 | 3 | 1 | 2 | 5 | 2 | 4 | 2.96 (49) | 🚫 ABAND |
| [CONV 109](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | Apr 18 | 11 | 1 | 5 | 3 | 4 | 3 | 2 | 2 | 5 | 3 | 5 | 3.09 (52) | — |
| [CONV 111](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | May 04 | 8 | 2 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 3.48 (62) | — |
| [CONV 112](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2532578405-1207833073-2362893569-1638018563?organization=assurantauto) | May 05 | 17 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.70 (67) | — |
| [CONV 115](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2566368638-1207112177-2240410041-1659749027?organization=assurantauto) | May 05 | 29 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.70 (67) | — |
| [CONV 116](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2576713574-1126765041-2597093866-2917985560?organization=assurantauto) | Apr 29 | 24 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 3 | 5 | 4.53 (88) | — |
| [CONV 118](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2712705162-0966595057-2769940324-1336708325?organization=assurantauto) | Apr 17 | 15 | 4 | 5 | 4 | 3 | 3 | 4 | 4 | 5 | 4 | 5 | 4.08 (77) | — |
| [CONV 119](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2718387246-0960106993-3073306468-1336708325?organization=assurantauto) | Apr 17 | 37 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4.33 (83) | — |
| [CONV 121](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2761588534-1020727793-3067208203-1489170986?organization=assurantauto) | Apr 21 | 24 | 3 | 5 | 4 | 2 | 4 | 3 | 4 | 5 | 3 | 5 | 3.70 (67) | — |
| [CONV 122](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2813330473-1022956017-2503729675-1489170986?organization=assurantauto) | Apr 21 | 27 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.17 (79) | — |
| [CONV 123](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | Apr 22 | 24 | 1 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 3.14 (54) | — |
| [CONV 124](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | May 05 | 20 | 2 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 3.80 (70) | — |
| [CONV 125](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2853825887-1207046641-2872111545-1659749027?organization=assurantauto) | May 05 | 18 | 3 | 4 | 3 | 5 | 4 | 2 | 3 | 5 | 4 | 4 | 3.62 (66) | — |
| [CONV 127](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | Apr 29 | 20 | 1 | 5 | 3 | 5 | 5 | 2 | 2 | 5 | 2 | 5 | 3.32 (58) | 🚫 ABAND |
| [CONV 128](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | Apr 21 | 22 | 1 | 3 | 4 | 3 | 5 | 4 | 3 | 5 | 5 | 4 | 3.26 (56) | — |
| [CONV 129](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2980862308-1111953905-2636836708-1336708325?organization=assurantauto) | Apr 28 | 21 | 4 | 5 | 4 | 3 | 5 | 3 | 3 | 5 | 3 | 5 | 4.07 (77) | — |
| [CONV 130](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2998791010-1207898609-3150836153-1659749027?organization=assurantauto) | May 05 | 17 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4.33 (83) | — |
| [CONV 132](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | Apr 22 | 22 | 2 | 3 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 4 | 3.51 (63) | — |
| [CONV 134](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3073493438-1104220657-3090842090-2917985560?organization=assurantauto) | Apr 28 | 29 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | — |
| [CONV 135](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3131072886-1018892785-2536825355-1489170986?organization=assurantauto) | Apr 21 | 26 | 4 | 5 | 5 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 4.50 (87) | — |
| [CONV 136](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3133496441-1192038897-2808607161-1659749027?organization=assurantauto) | May 04 | 17 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.83 (96) | — |
| [CONV 137](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | Apr 23 | 16 | 1 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 3.56 (64) | — |
| [CONV 139](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | Apr 27 | 23 | 1 | 4 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.51 (63) | — |
| [CONV 140](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | Apr 22 | 14 | 1 | 4 | 3 | 3 | 3 | 2 | 2 | 5 | 4 | 4 | 2.81 (45) | — |
| [CONV 142](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3244475956-1010242033-3188490730-2917985560?organization=assurantauto) | Apr 20 | 48 | 5 | 4 | 3 | 5 | 4 | 4 | 3 | 5 | 3 | 4 | 4.17 (79) | — |
| [CONV 143](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | May 05 | 49 | 3 | 2 | 3 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 3.37 (59) | — |
| [CONV 144](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3276343573-1207964145-3163874561-1638018563?organization=assurantauto) | May 05 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — |
| [CONV 146](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3315304968-1114444273-2240713784-0825805307?organization=assurantauto) | Apr 28 | 11 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4.56 (89) | — |
| [CONV 147](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3332361473-1008931313-2596204388-1336708325?organization=assurantauto) | Apr 20 | 31 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.39 (85) | — |
| [CONV 152](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3417925909-0981406193-2828435946-2917985560?organization=assurantauto) | Apr 18 | 8 | 3 | 5 | 4 | 2 | 5 | 4 | 4 | 5 | 4 | 5 | 3.92 (73) | — |
| [CONV 154](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3456065548-1018237425-3168961002-2917985560?organization=assurantauto) | Apr 21 | 26 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4.53 (88) | — |
| [CONV 156](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3468960017-1036521969-2878636522-2917985560?organization=assurantauto) | Apr 22 | 24 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — |
| [CONV 159](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | Apr 29 | 7 | 2 | 5 | 4 | 4 | 5 | 3 | 4 | 5 | 4 | 5 | 3.84 (71) | — |
| [CONV 161](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3515729398-1124733425-3166999608-0825805307?organization=assurantauto) | Apr 29 | 15 | 3 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | 3 | 5 | 4.12 (78) | — |
| [CONV 162](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | May 04 | 11 | 2 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.72 (68) | — |
| [CONV 164](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3592956096-1019941361-3199787531-1489170986?organization=assurantauto) | Apr 21 | 12 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.61 (90) | — |
| [CONV 165](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3604895532-1046352369-2534506986-2917985560?organization=assurantauto) | Apr 23 | 19 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 4.44 (86) | — |
| [CONV 166](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3647451624-1047466481-2824721825-0188171332?organization=assurantauto) | Apr 23 | 21 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — |
| [CONV 167](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3672476677-1207308785-2694705593-1659749027?organization=assurantauto) | May 05 | 30 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4.22 (81) | — |
| [CONV 168](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3676613368-1139610097-2890826218-2917985560?organization=assurantauto) | Apr 30 | 20 | 3 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 4.30 (82) | — |
| [CONV 169](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3699588305-1100943857-2799342648-0825805307?organization=assurantauto) | Apr 27 | 21 | 3 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 4 | 4 | 3.90 (72) | — |
| [CONV 172](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3723634684-1195381233-2170810809-1659749027?organization=assurantauto) | May 04 | 66 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 3 | 4 | 3.64 (66) | — |
| [CONV 173](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3729246480-1020924401-2402083339-1489170986?organization=assurantauto) | Apr 21 | 12 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.83 (96) | — |
| [CONV 175](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3796968132-1207833073-2477712641-1638018563?organization=assurantauto) | May 05 | 33 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.17 (79) | — |
| [CONV 177](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | Apr 23 | 17 | 1 | 5 | 3 | 4 | 3 | 3 | 3 | 5 | 4 | 5 | 3.28 (57) | — |
| [CONV 179](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3871431063-1195053553-2645066218-2917985560?organization=assurantauto) | May 04 | 30 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4.11 (78) | — |
| [CONV 180](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3877927423-1141641713-2624881130-2917985560?organization=assurantauto) | Apr 30 | 32 | 3 | 4 | 3 | 5 | 5 | 3 | 3 | 5 | 3 | 5 | 3.84 (71) | — |
| [CONV 183](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4061003182-0966791665-2966544907-1489170986?organization=assurantauto) | Apr 17 | 11 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 4.22 (81) | — |
| [CONV 184](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4080665955-1207046641-3021074873-1659749027?organization=assurantauto) | May 05 | 8 | 3 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 4 | 5 | 4.01 (75) | — |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | Apr 22 | 41 | 2 | 4 | 3 | 4 | 5 | 3 | 3 | 5 | 3 | 5 | 3.51 (63) | — |
| [CONV 187](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4179586080-1206325745-3092374785-1638018563?organization=assurantauto) | May 05 | 15 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 3.72 (68) | — |
| [CONV 188](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4182611759-1059590641-3188888632-0825805307?organization=assurantauto) | Apr 24 | 21 | 3 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.09 (77) | — |
| [CONV 189](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4202030099-0960172529-2925126155-1489170986?organization=assurantauto) | Apr 17 | 25 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4.44 (86) | — |
| [CONV 190](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | Apr 27 | 8 | 1 | 5 | 5 | 4 | 5 | 1 | 1 | 5 | 4 | 4 | 3.30 (57) | 🚫 ABAND |
| [CONV 191](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4272166275-1059459569-2422309354-2917985560?organization=assurantauto) | Apr 24 | 18 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4.31 (83) | — |

---

## Section 5: Flagged Conversations
*Criteria: any override flag, overall score < 2.5/5, D1 ≤ 2, or D12 ≤ 2*

| Conv | Date | Conv ID | Score | D1 | D12 | Flags | Note |
|------|------|---------|-------|----|-----|-------|------|
| [CONV 61](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | Apr 23 | [`1328754597-1046811121-2704338788-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto) | 2.47 (37/100) | 1 | 2 | SAFETY, ABANDONED | CRITICAL: Bot leaked internal queue-status prompt to customer — fundamental… |
| [CONV 140](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | Apr 22 | [`3218327297-1031606769-2176380772-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3218327297-1031606769-2176380772-1336708325?organization=assurantauto) | 2.81 (45/100) | 1 | 4 | — | Bot responded to opening 'Representative' with 'I'm unable to assist furthe… |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | Apr 20 | [`1794270454-1005261297-2430042602-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1794270454-1005261297-2430042602-2917985560?organization=assurantauto) | 2.90 (47/100) | 1 | 4 | ABANDONED | Customer never authenticated; bot repeated 'I wasn't able to find a record'… |
| [CONV 104](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | Apr 23 | [`2307801813-1045041649-2903409130-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2307801813-1045041649-2903409130-2917985560?organization=assurantauto) | 2.92 (48/100) | 1 | 4 | ABANDONED | Agent queue unavailable: repair facility stuck in loop; bot offered email/p… |
| [CONV 108](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | Apr 22 | [`2425241405-1034621425-2596859748-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2425241405-1034621425-2596859748-1336708325?organization=assurantauto) | 2.96 (49/100) | 1 | 4 | ABANDONED | Bot failed 6+ 'speak with representative' requests; 'rep' heard as 'rent'; … |
| [CONV 109](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | Apr 18 | [`2438618780-0981471729-2907041636-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2438618780-0981471729-2907041636-1336708325?organization=assurantauto) | 3.09 (52/100) | 1 | 5 | — | Bot said goodbye while customer actively requesting an operator; transcript… |
| [CONV 10](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | Apr 22 | [`0251497861-1035014641-2786717540-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0251497861-1035014641-2786717540-1336708325?organization=assurantauto) | 3.11 (53/100) | 1 | 5 | — | Bot failed to recognize repeated 'representative' requests; likely failed t… |
| [CONV 123](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | Apr 22 | [`2817014493-1031541233-3068695608-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2817014493-1031541233-3068695608-0825805307?organization=assurantauto) | 3.14 (54/100) | 1 | 4 | — | Bot initially stated it couldn't connect to a representative (incorrect); C… |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | Apr 22 | [`0348917324-1031606769-3098931044-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0348917324-1031606769-3098931044-1336708325?organization=assurantauto) | 3.18 (54/100) | 1 | 4 | HALLUCINATION | Bot falsely told customer 'you're already being connected to a representati… |
| [CONV 81](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | Apr 22 | [`1851846244-1034490353-2169410616-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1851846244-1034490353-2169410616-0825805307?organization=assurantauto) | 3.23 (56/100) | 1 | 4 | ABANDONED | Spanish-speaking caller unable to get service; bot just repeated English-on… |
| [CONV 128](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | Apr 21 | [`2914676966-1017778673-2571366244-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2914676966-1017778673-2571366244-1336708325?organization=assurantauto) | 3.26 (56/100) | 1 | 4 | — | Bot told customer to 'call 1-800-621-2130' while already on the phone; cust… |
| [CONV 51](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | Apr 20 | [`1198705778-1010242033-2904588778-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1198705778-1010242033-2904588778-2917985560?organization=assurantauto) | 3.26 (56/100) | 1 | 4 | ABANDONED | Dealer wanted phone agent; bot ended call with farewell despite explicit ph… |
| [CONV 177](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | Apr 23 | [`3822848610-1045697009-3058598378-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3822848610-1045697009-3058598378-2917985560?organization=assurantauto) | 3.28 (57/100) | 1 | 5 | — | Dealer repeatedly said 'speak with rep'; bot kept asking for purpose; trans… |
| [CONV 190](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | Apr 27 | [`4223284239-1103761905-2187063140-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4223284239-1103761905-2187063140-1336708325?organization=assurantauto) | 3.30 (57/100) | 1 | 4 | ABANDONED | Customer asked for representative; bot offered chat, customer declined, bot… |
| [CONV 127](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | Apr 29 | [`2883648572-1128337905-2480247864-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2883648572-1128337905-2480247864-0825805307?organization=assurantauto) | 3.32 (58/100) | 1 | 5 | ABANDONED | 'Plain number' ASR; 'Customer service' repeated transfer intent not recogni… |
| [CONV 143](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | May 05 | [`3260951102-1205473777-2699620793-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | 3.37 (59/100) | 3 | 4 | — | Long complex call with garbled customer responses; eventually escalated. Mu… |
| [CONV 64](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | Apr 20 | [`1461535746-1010962929-2700776504-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1461535746-1010962929-2700776504-0825805307?organization=assurantauto) | 3.44 (61/100) | 2 | 5 | — | Customer confused after contract selection; bot offered website before iden… |
| [CONV 70](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | Apr 21 | [`1588261601-1022497265-2402279947-1489170986`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1588261601-1022497265-2402279947-1489170986?organization=assurantauto) | 3.48 (62/100) | 1 | 5 | — | Dealer's VIN not found in system; call ended without resolution or alternat… |
| [CONV 101](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | Apr 20 | [`2266244334-1008996849-2518802955-1489170986`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266244334-1008996849-2518802955-1489170986?organization=assurantauto) | 3.48 (62/100) | 2 | 4 | — | Coverage question redirected to portal text; call ended without coverage an… |
| [CONV 111](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | May 04 | [`2521437428-1192301041-2215965113-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | 3.48 (62/100) | 2 | 5 | — | Broken-down car customer received scripted dealer info but no roadside tran… |
| [CONV 132](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | Apr 22 | [`3035186604-1033048561-2998768696-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3035186604-1033048561-2998768696-0825805307?organization=assurantauto) | 3.51 (63/100) | 2 | 4 | — | Repair facility sent RO email but never received case number; bot's '2-minu… |
| [CONV 139](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | Apr 27 | [`3186447997-1100943857-2550001508-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186447997-1100943857-2550001508-1336708325?organization=assurantauto) | 3.51 (63/100) | 1 | 5 | — | VIN not found; bot said goodbye while dealer still needed help. |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | Apr 22 | [`4141745400-1034949105-2328794168-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4141745400-1034949105-2328794168-0825805307?organization=assurantauto) | 3.51 (63/100) | 2 | 5 | — | Multiple lookup failures; coverage question unanswered; bot confused by cal… |
| [CONV 137](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | Apr 23 | [`3165613731-1049694705-2283639864-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3165613731-1049694705-2283639864-0825805307?organization=assurantauto) | 3.56 (64/100) | 1 | 5 | — | 'Viewership' ASR artifact for 'dealership'; customer declined to provide id… |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | Apr 28 | [`1761050634-1111429617-2851139428-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1761050634-1111429617-2851139428-1336708325?organization=assurantauto) | 3.57 (64/100) | 2 | 4 | — | Call ended mid-collection; bot idled with 'I am still here'. |
| [CONV 83](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | Apr 28 | [`1894537135-1114247665-2518254058-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1894537135-1114247665-2518254058-2917985560?organization=assurantauto) | 3.62 (66/100) | 2 | 4 | — | Same email-RO dead-end as CONV 110; call ended waiting for case number. |
| [CONV 105](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | Apr 28 | [`2335431778-1111691761-2532938808-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2335431778-1111691761-2532938808-0825805307?organization=assurantauto) | 3.62 (66/100) | 2 | 4 | — | Same pattern as CONV 70; email RO dead-end; claim not started. |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | Apr 27 | [`0140238296-1100943857-2505086008-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0140238296-1100943857-2505086008-0825805307?organization=assurantauto) | 3.64 (66/100) | 1 | 5 | — | Dealer VIN not found; no alternative offered; call ended without resolution… |
| [CONV 65](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | May 05 | [`1484095264-1208488433-2566382849-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | 3.66 (66/100) | 2 | 5 | — | Bot claimed account was pulled up then asked for caller type; coverage ques… |
| [CONV 162](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | May 04 | [`3542794834-1192235505-2815923256-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | 3.72 (68/100) | 2 | 4 | — | Customer requested rep up front; bot quickly identified caller type and tra… |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | May 05 | [`0212455871-1207046641-2586046905-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | 3.73 (68/100) | 2 | 5 | — | Bot claimed account was pulled up but then asked for caller type; no transf… |
| [CONV 124](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | May 05 | [`2838792712-1209143793-2204820737-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | 3.80 (70/100) | 2 | 4 | — | Tow request mid-flow; bot handled S→F contract number correction well; conv… |
| [CONV 72](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | May 05 | [`1601360915-1207898609-2646140161-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | 3.81 (70/100) | 2 | 5 | — | Bot immediately provided claim-filing instructions without gathering identi… |
| [CONV 63](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | May 05 | [`1391865844-1207046641-2711220665-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | 3.84 (71/100) | 2 | 5 | — | Call ended mid-identification after phone lookup failed; customer's stated … |
| [CONV 159](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | Apr 29 | [`3498885050-1127289329-3031209016-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3498885050-1127289329-3031209016-0825805307?organization=assurantauto) | 3.84 (71/100) | 2 | 5 | — | Call ended prematurely during CallerID after dealer identified; goal not ac… |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | May 01 | [`0612002884-1154617841-2360316984-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0612002884-1154617841-2360316984-0825805307?organization=assurantauto) | 4.13 (78/100) | 2 | 5 | — | Very clean — immediate transfer upon agent request with no friction. |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | May 04 | [`0445586395-1192759793-3072623082-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | 4.33 (83/100) | 2 | 5 | — | Immediate clean transfer upon rep request. |

---

## Section 6: Representative Examples

### Highest scorer: CONV 32 — 5.00/5 (100/100)
**Conv ID:** [`0839037409-1112805873-2891284970-2917985560`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0839037409-1112805873-2891284970-2917985560?organization=assurantauto)  
**Date:** 2026-04-28  |  **Tasks:** CallerIdentification, DealershipIssues  
**Assessment:** Excellent: payment status provided; smooth efficient transfer.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! How can I help you today?
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

### Most notable failure: CONV 106 — 4.67/5 (92/100)
**Conv ID:** [`2355214065-1153438193-2467140664-0825805307`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2355214065-1153438193-2467140664-0825805307?organization=assurantauto)  
**Date:** 2026-05-01  |  **Tasks:** CallerIdentification, ContractHolderIssues  
**Assessment:** Smooth flow: VIN-based lookup, vehicle identified, claim payment status provided, contract number disclosure on request.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
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

### Lowest scorer: CONV 61 — 2.47/5 (37/100)
**Conv ID:** [`1328754597-1046811121-2704338788-1336708325`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1328754597-1046811121-2704338788-1336708325?organization=assurantauto)  
**Date:** 2026-04-23  |  **Tasks:** CallerIdentification, RepairShopIssues  
**Flags:** SAFETY_VIOLATION, ABANDONED  
**Assessment:** CRITICAL: Bot leaked internal queue-status prompt to customer — fundamental system failure.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! How can I help you today?
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
*Weekly distribution: Wk16=2, Wk17=3, Wk18=4, Wk19=2 — **persistent across all 4 weeks**, no improvement trend.*
Core vocabulary is consistently misheard:
- **'claim'** → 'flame', 'lame', 'plain', 'piece', 'plane' (CONV 74, 107, 168, 188, 191 and others)
- **'VIN'** / **'VIN number'** → **'thin'** (CONV 71, 107, 161) — repeating artifact affecting VIN collection
- **'repair facility'** → 'Repurfacin' (CONV 103) — understood from context but ASR artifact
For a service whose primary function is claim handling and caller identification, failure to reliably transcribe these core vocabulary terms is a critical ASR gap.

### Issue 2 — Agent Queue Unavailability With No Fallback *(High Severity)*
*Weekly distribution: Wk16=2, Wk17=1, Wk18=0, Wk19=0 — **concentrated in early weeks**, may have stopped recurring.*
When agent queues are closed (CONV 44, 92, 104), the bot has no graceful fallback beyond business hours info. In CONV 104 this produced an infinite loop offering email/portal options the caller had already refused. A callback scheduling option or clearer escalation path is needed.

### Issue 3 — Transfer Intent Not Recognized *(Medium-High Severity)*
*Weekly distribution: Wk16=1, Wk17=5, Wk18=2, Wk19=0 — **peaked in Wk17 (Apr 20-26)**, declining since.*
Callers requesting 'representative', 'agent', or 'operator' were repeatedly asked to clarify intent first (CONV 10, 108, 109, 127, 140, 177, 190). In CONV 123 the bot explicitly said it couldn't connect to a representative directly. Callers voicing an explicit transfer request should trigger a transfer, not a disambiguation prompt.

### Issue 4 — Chat Upsell Before Phone Transfer *(Low-Medium Severity)*
*Weekly distribution: present in **all weeks** — systemic Portal Self-Service Nudge applied even when caller has already requested phone agent.*
In ~60% of phone-transfer flows the bot offered website/chat alternatives before transferring. Callers who have already said 'phone agent' or 'representative' are not a good chat upsell audience; this pattern adds turns and creates friction.

### Issue 5 — Email RO Dead-End for Repair Facilities *(Medium Severity)*
*Weekly distribution: Wk17=1, Wk18=2, Wk19=0 — **clustered in Wk17-18**.*
Repair facilities that submitted an RO via email but have not yet received a case number (CONV 132, 83, 105) are sent into a dead-end: the bot asks for the case number, they don't have it, and the call ends unresolved. An alternative lookup path (by RO number, shop phone, or date) is needed.

### Issue 6 — Internal Prompt Leakage *(Critical — CONV 61 only)*
*Weekly distribution: Wk17 only (1 instance, Apr 23) — **single occurrence**, severity critical.*
CONV 61 exhibits a fundamental system failure: the bot asked the customer to confirm the status of internal agent queues ('Could you please confirm if customer service, claims, payment, premium, and RV queues are currently open?'). This internal routing instruction was exposed directly to the caller. Requires immediate root-cause investigation.

### Issue 7 — PII Template Tags *(Not an issue — post-conversation database artifact)*
Tags such as `{pii_immediate_genagent_persistence.PERSON:**}` appear in the database transcript only — they are applied during post-conversation redaction and are NOT what the caller heard. Previously flagged conversations (CONV 33, 106, 111, 143, 167) have been re-scored.

### Issue 8 — False Transfer Confirmation *(Critical — CONV 15 only)*
*Weekly distribution: Wk17 only (1 instance, Apr 22) — **single occurrence**, severity critical.*
Bot told the customer 'You're already being connected to a representative' when no transfer occurred. The call ended with a farewell greeting — a trust-breaking hallucination that leaves the caller without a callback.

### Issue 9 — No Spanish Language Support or Escalation Path *(Medium Severity — CONV 81 only so far)*
*Weekly distribution: Wk17 only (1 instance, Apr 22) — **single sample**, indicative of a population gap.*
A Spanish-speaking caller (CONV 81, Apr 22) was unable to get service. The bot repeated 'I'm here to assist you in English' with no offer to escalate to a Spanish-speaking agent. If the caller population includes Spanish speakers, an escalation path or language detection handoff is needed.

### Issue 10 — 'Account Pulled Up' Greeting Then Re-Asks for Caller Type *(Low Severity)*
*Weekly distribution: Wk19 only (2 instances, May 5) — **new pattern emerging in latest week**, may indicate a recent prompt change.*
When the bot uses the personalized greeting 'I have your account information pulled up' (recognized phone number), it then re-asks for caller type (customer/dealer/repair facility), creating a confusing inconsistency (CONV 9, 65). If the account is known, the caller type should be inferred or skipped.
