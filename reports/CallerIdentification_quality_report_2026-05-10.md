## Weekly Voice Quality Report — CallerIdentification

*Week of 2026-05-04 (Mon) → 2026-05-10 (Sun) | Generated 2026-05-13*

Conversations analyzed: 85  |  Scored: 68  |  Skipped (no customer turns): 17


| Metric | Value |
|---|---|
| Mean overall score (scored convs) | 4.09 / 5 (77/100) |
| **Pass rate** | **39/68 = 57%** |
| Conversations scoring < 3.0 | 1 (1%) |
| Safety / policy flags | 0 |
| Critical hallucination flags | 0 |
| Abandoned calls | 3 |

---

## Section 1.5: Pass / Fail

*Binary metric per conversation: PASS iff D1 ≥ 4 AND no frustration indicators (ABANDONED flag, D1=1, or notes containing patterns like 'looped', 'never escalated', 'kept asking', 'stuck').*

| Metric | Value |
|---|---|
| **Pass rate** | **39/68 = 57.4%** |
| Fail — frustrated or wrong action | 29 (42.6%) |

### Daily Pass/Fail Trend

| Date | Total | Pass | % Pass | Trend |
|------|-------|------|--------|-------|
| 2026-05-04 | 9 | 3 | 33% | ████████················· |
| 2026-05-05 | 22 | 8 | 36% | █████████················ |
| 2026-05-06 | 15 | 13 | 87% | ██████████████████████··· |
| 2026-05-07 | 8 | 6 | 75% | ███████████████████······ |
| 2026-05-08 | 13 | 8 | 62% | ███████████████·········· |
| 2026-05-09 | 1 | 1 | 100% | █████████████████████████ |

---

## Section 2: Daily Score Trend

| Date | N | Mean /5 | /100 | Trend |
|------|---|---------|------|-------|
| 2026-05-04 | 9 | 4.01 | 80 | ████████████████████████······ |
| 2026-05-05 | 22 | 4.01 | 80 | ████████████████████████······ |
| 2026-05-06 | 15 | 4.20 | 84 | █████████████████████████····· |
| 2026-05-07 | 8 | 4.21 | 84 | █████████████████████████····· |
| 2026-05-08 | 13 | 4.06 | 81 | ████████████████████████······ |
| 2026-05-09 | 1 | 4.28 | 86 | ██████████████████████████···· |

---

## Section 3: Dimension Heatmap

| Dim | Name | Weight | Mean | Std | Min | Max | %≤2 |
|-----|------|--------|------|-----|-----|-----|------|
| D1 | Design Adherence | 20% | 3.72 | 1.21 | 1 | 5 | 19% |
| D2 | Information Accuracy | 10% | 4.15 | 0.53 | 2 | 5 | 1% |
| D3 | Context Retention | 10% | 3.84 | 0.64 | 2 | 5 | 1% |
| D4 | Response Latency | 10% | 4.34 | 0.75 | 2 | 5 | 1% |
| D5 | Turn-Taking | 8% | 4.18 | 0.42 | 3 | 5 | 0% |
| D6 | Repair & Recovery | 7% | 3.74 | 0.70 | 2 | 5 | 6% |
| D8 | Tone | 5% | 3.78 | 0.59 | 2 | 5 | 1% |
| D9 | Verbosity | 5% | 4.94 | 0.29 | 3 | 5 | 0% |
| D10 | ASR | 5% | 3.99 | 0.56 | 3 | 5 | 0% |
| D12 | Policy & Safety | 10% | 4.72 | 0.45 | 4 | 5 | 0% |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 4: Per-Conversation Scores

*All 68 scored conversations from the week. D4 and D9 auto-computed; D7 and D11 require audio.*

| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | P/F | Flags |
|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-----|-------|
| [CONV 16](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0333763583-1193415153-2807464426-2917985560?organization=assurantauto) | 05-04 | 9 | 4 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4.00 (75) | ✓ PASS | — |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | 05-04 | 4 | 2 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4.33 (83) | ✗ FAIL | — |
| [CONV 33](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0769152030-1195315697-2760631553-1638018563?organization=assurantauto) | 05-04 | 25 | 3 | 5 | 3 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 3.92 (73) | ✗ FAIL | — |
| [CONV 59](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1112326957-1194463729-2387469569-1638018563?organization=assurantauto) | 05-04 | 25 | 3 | 5 | 4 | 5 | 4 | 3 | 4 | 5 | 3 | 5 | 4.03 (76) | ✗ FAIL | — |
| [CONV 131](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | 05-04 | 7 | 2 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 5 | 3.48 (62) | ✗ FAIL | — |
| [CONV 157](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3133496441-1192038897-2808607161-1659749027?organization=assurantauto) | 05-04 | 16 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4.83 (96) | ✓ PASS | — |
| [CONV 187](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | 05-04 | 7 | 2 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.72 (68) | ✗ FAIL | — |
| [CONV 196](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3723634684-1195381233-2170810809-1659749027?organization=assurantauto) | 05-04 | 42 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 3 | 4 | 3.64 (66) | ✗ FAIL | — |
| [CONV 204](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3871431063-1195053553-2645066218-2917985560?organization=assurantauto) | 05-04 | 20 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 4 | 4.11 (78) | ✓ PASS | — |
| [CONV 4](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0115003615-1207964145-2886329601-1638018563?organization=assurantauto) | 05-05 | 4 | 4 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.92 (73) | ✓ PASS | — |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | 05-05 | 4 | 2 | 5 | 3 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.73 (68) | ✗ FAIL | — |
| [CONV 37](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0795050560-1204490737-3136061930-2917985560?organization=assurantauto) | 05-05 | 19 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4.37 (84) | ✓ PASS | — |
| [CONV 41](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0859768425-1207112177-2833442049-1638018563?organization=assurantauto) | 05-05 | 16 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (78) | ✓ PASS | — |
| [CONV 43](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0878025181-1209209329-2674651577-1659749027?organization=assurantauto) | 05-05 | 22 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.42 (86) | ✗ FAIL | — |
| [CONV 51](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1015743628-1207964145-2279928249-1659749027?organization=assurantauto) | 05-05 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | ✓ PASS | — |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | 05-05 | 7 | 2 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 5 | 5 | 3.84 (71) | ✗ FAIL | — |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | 05-05 | 7 | 2 | 5 | 2 | 5 | 5 | 2 | 3 | 5 | 5 | 5 | 3.66 (66) | ✗ FAIL | — |
| [CONV 87](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | 05-05 | 4 | 2 | 4 | 4 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 3.81 (70) | ✗ FAIL | — |
| [CONV 88](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1616841208-1205473777-2344019201-1638018563?organization=assurantauto) | 05-05 | 9 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3.94 (74) | ✗ FAIL | — |
| [CONV 120](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2303899210-1205670385-2694767873-1638018563?organization=assurantauto) | 05-05 | 7 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4.44 (86) | ✗ FAIL | — |
| [CONV 132](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2532578405-1207833073-2362893569-1638018563?organization=assurantauto) | 05-05 | 10 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | ✗ FAIL | — |
| [CONV 135](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2566368638-1207112177-2240410041-1659749027?organization=assurantauto) | 05-05 | 19 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.70 (67) | ✗ FAIL | — |
| [CONV 145](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | 05-05 | 11 | 2 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 3.80 (70) | ✗ FAIL | — |
| [CONV 146](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2853825887-1207046641-2872111545-1659749027?organization=assurantauto) | 05-05 | 11 | 3 | 4 | 3 | 4 | 4 | 2 | 3 | 5 | 4 | 4 | 3.51 (63) | ✗ FAIL | — |
| [CONV 150](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2998791010-1207898609-3150836153-1659749027?organization=assurantauto) | 05-05 | 10 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.39 (85) | ✓ PASS | — |
| [CONV 166](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3260951102-1205473777-2699620793-1659749027?organization=assurantauto) | 05-05 | 30 | 3 | 2 | 3 | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 3.31 (58) | ✗ FAIL | — |
| [CONV 167](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3276343573-1207964145-3163874561-1638018563?organization=assurantauto) | 05-05 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | ✓ PASS | — |
| [CONV 193](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3672476677-1207308785-2694705593-1659749027?organization=assurantauto) | 05-05 | 20 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | ✓ PASS | — |
| [CONV 200](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3796968132-1207833073-2477712641-1638018563?organization=assurantauto) | 05-05 | 23 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4.17 (79) | ✓ PASS | — |
| [CONV 210](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4080665955-1207046641-3021074873-1659749027?organization=assurantauto) | 05-05 | 7 | 3 | 5 | 4 | 4 | 5 | 3 | 3 | 5 | 4 | 5 | 4.01 (75) | ✗ FAIL | — |
| [CONV 215](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4179586080-1206325745-3092374785-1638018563?organization=assurantauto) | 05-05 | 9 | 3 | 4 | 4 | 2 | 4 | 4 | 4 | 5 | 4 | 4 | 3.61 (65) | ✗ FAIL | — |
| [CONV 19](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0396067837-1216549361-2959729921-1638018563?organization=assurantauto) | 05-06 | 23 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 27](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0502877744-1219695089-2243555769-1659749027?organization=assurantauto) | 05-06 | 28 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 4.00 (75) | ✓ PASS | — |
| [CONV 53](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1041970917-1216614897-3028021689-1659749027?organization=assurantauto) | 05-06 | 33 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 58](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1102387425-1221136881-2885415353-1659749027?organization=assurantauto) | 05-06 | 26 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4.76 (94) | ✓ PASS | — |
| [CONV 60](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1122006560-1209733617-2927224065-1638018563?organization=assurantauto) | 05-06 | 16 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 67](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1230494786-1215500785-2331767225-1659749027?organization=assurantauto) | 05-06 | 16 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 71](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1287515376-1220612593-2861032705-1638018563?organization=assurantauto) | 05-06 | 28 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.17 (79) | ✓ PASS | — |
| [CONV 76](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1336807331-1215566321-2726028545-1638018563?organization=assurantauto) | 05-06 | 15 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 93](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1716235639-1217466865-2253907201-1638018563?organization=assurantauto) | 05-06 | 22 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (78) | ✓ PASS | — |
| [CONV 123](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2349230954-1218318833-3154375097-1659749027?organization=assurantauto) | 05-06 | 16 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 126](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2404003558-1221530097-2781406465-1638018563?organization=assurantauto) | 05-06 | 29 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 129](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2503337876-1216549361-2839540153-1659749027?organization=assurantauto) | 05-06 | 33 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 3.70 (67) | ✗ FAIL | — |
| [CONV 137](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2578512181-1220284913-3076973825-1638018563?organization=assurantauto) | 05-06 | 17 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 151](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto) | 05-06 | 15 | 1 | 3 | 3 | 5 | 4 | 2 | 2 | 5 | 3 | 4 | 2.96 (49) | ✗ FAIL | 🚫 ABAND |
| [CONV 181](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3476134448-1215500785-2689000705-1638018563?organization=assurantauto) | 05-06 | 12 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | ✓ PASS | — |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0332358522-1233523185-2987848121-1659749027?organization=assurantauto) | 05-07 | 15 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 30](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0729601212-1231163889-2430788865-1638018563?organization=assurantauto) | 05-07 | 23 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0797214453-1234637297-3210670521-1659749027?organization=assurantauto) | 05-07 | 35 | 2 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | ✗ FAIL | — |
| [CONV 49](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0990410271-1233326577-2952914177-1638018563?organization=assurantauto) | 05-07 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | ✗ FAIL | — |
| [CONV 102](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1906412126-1230705137-3065570561-1638018563?organization=assurantauto) | 05-07 | 22 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 141](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2759451159-1230442993-2469654969-1659749027?organization=assurantauto) | 05-07 | 26 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 208](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4029491569-1232146929-2212357377-1638018563?organization=assurantauto) | 05-07 | 19 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 213](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4148517809-1232540145-2605376769-1638018563?organization=assurantauto) | 05-07 | 21 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 20](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0441985862-1246302705-2759910657-1638018563?organization=assurantauto) | 05-08 | 32 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.17 (79) | ✓ PASS | — |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0478963028-1245516273-2936336825-1659749027?organization=assurantauto) | 05-08 | 7 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.61 (90) | ✓ PASS | — |
| [CONV 57](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1096837356-1243681265-3071996345-1659749027?organization=assurantauto) | 05-08 | 22 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4.06 (76) | ✓ PASS | — |
| [CONV 90](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1656572716-1246237169-2481513729-1638018563?organization=assurantauto) | 05-08 | 8 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 3.94 (74) | ✗ FAIL | — |
| [CONV 97](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1805304062-1245778417-2511466937-1659749027?organization=assurantauto) | 05-08 | 17 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |
| [CONV 138](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2590829860-1242763761-2835801345-1638018563?organization=assurantauto) | 05-08 | 15 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 3.70 (67) | ✗ FAIL | — |
| [CONV 160](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3178654791-1243615729-2298209537-1638018563?organization=assurantauto) | 05-08 | 18 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 3.48 (62) | ✗ FAIL | 🚫 ABAND |
| [CONV 163](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto) | 05-08 | 7 | 1 | 4 | 3 | 5 | 3 | 2 | 3 | 5 | 3 | 4 | 3.03 (51) | ✗ FAIL | — |
| [CONV 168](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3299653061-1246237169-2277503417-1659749027?organization=assurantauto) | 05-08 | 19 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | ✓ PASS | — |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3520813528-1242370545-3215585721-1659749027?organization=assurantauto) | 05-08 | 12 | 2 | 4 | 3 | 5 | 4 | 3 | 3 | 5 | 4 | 5 | 3.59 (65) | ✗ FAIL | 🚫 ABAND |
| [CONV 190](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3603763621-1246499313-3194807553-1638018563?organization=assurantauto) | 05-08 | 20 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | ✓ PASS | — |
| [CONV 209](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4055395116-1247023601-2881286585-1659749027?organization=assurantauto) | 05-08 | 21 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.50 (87) | ✓ PASS | — |
| [CONV 214](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4156083984-1245057521-3139233025-1638018563?organization=assurantauto) | 05-08 | 18 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (85) | ✓ PASS | — |
| [CONV 110](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2131156183-1256985073-2414510570-2917985560?organization=assurantauto) | 05-09 | 7 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (82) | ✓ PASS | — |

---

## Section 5: Flagged Conversations

*Criteria: any override flag, overall score < 2.5/5, D1 ≤ 2, or D12 ≤ 2 — 13 of 68 scored.*

| # | Date | D1 | D12 | Score | Flags | Conv ID |
|---|------|----|----|-------|-------|---------|
| [CONV 151](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto) | 05-06 | 1 | 4 | 2.96 | 🚫 ABAND | `3014101863-1221005809-2288644537-1659749027` |
| [CONV 163](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto) | 05-08 | 1 | 4 | 3.03 | — | `3223725281-1247023601-2808738233-1659749027` |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0797214453-1234637297-3210670521-1659749027?organization=assurantauto) | 05-07 | 2 | 4 | 3.48 | — | `0797214453-1234637297-3210670521-1659749027` |
| [CONV 131](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2521437428-1192301041-2215965113-1659749027?organization=assurantauto) | 05-04 | 2 | 5 | 3.48 | — | `2521437428-1192301041-2215965113-1659749027` |
| [CONV 160](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3178654791-1243615729-2298209537-1638018563?organization=assurantauto) | 05-08 | 2 | 4 | 3.48 | 🚫 ABAND | `3178654791-1243615729-2298209537-1638018563` |
| [CONV 186](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3520813528-1242370545-3215585721-1659749027?organization=assurantauto) | 05-08 | 2 | 5 | 3.59 | 🚫 ABAND | `3520813528-1242370545-3215585721-1659749027` |
| [CONV 80](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1484095264-1208488433-2566382849-1638018563?organization=assurantauto) | 05-05 | 2 | 5 | 3.66 | — | `1484095264-1208488433-2566382849-1638018563` |
| [CONV 187](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3542794834-1192235505-2815923256-0825805307?organization=assurantauto) | 05-04 | 2 | 4 | 3.72 | — | `3542794834-1192235505-2815923256-0825805307` |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0212455871-1207046641-2586046905-1659749027?organization=assurantauto) | 05-05 | 2 | 5 | 3.73 | — | `0212455871-1207046641-2586046905-1659749027` |
| [CONV 145](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2838792712-1209143793-2204820737-1638018563?organization=assurantauto) | 05-05 | 2 | 4 | 3.80 | — | `2838792712-1209143793-2204820737-1638018563` |
| [CONV 87](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1601360915-1207898609-2646140161-1638018563?organization=assurantauto) | 05-05 | 2 | 5 | 3.81 | — | `1601360915-1207898609-2646140161-1638018563` |
| [CONV 78](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1391865844-1207046641-2711220665-1659749027?organization=assurantauto) | 05-05 | 2 | 5 | 3.84 | — | `1391865844-1207046641-2711220665-1659749027` |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0445586395-1192759793-3072623082-2917985560?organization=assurantauto) | 05-04 | 2 | 5 | 4.33 | — | `0445586395-1192759793-3072623082-2917985560` |

---

## Section 6: Representative Examples

### Highest scorer: CONV 167 — 5.00/5 (100/100)
**Conv ID:** [`3276343573-1207964145-3163874561-1638018563`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3276343573-1207964145-3163874561-1638018563?organization=assurantauto)  
**Date:** 2026-05-05  |  **Tasks:** CallerIdentification, CallerIdentification, ContractHolderIssues  
**Assessment:** Clean classification, prompt routing, no friction.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! I have your account information pulled up... how can I help you today?
  Customer: Yeah. I I need some roadside assistance. Uh, stuck on the side of the road.
  Talker: One moment please.
  Talker: Hold on while I transfer you to Customer Care.
```

### Most notable failure: CONV 163 — 3.03/5 (54/100)
**Conv ID:** [`3223725281-1247023601-2808738233-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3223725281-1247023601-2808738233-1659749027?organization=assurantauto)  
**Date:** 2026-05-08  |  **Tasks:** CallerIdentification, CallerIdentification, RepairShopIssues  
**Assessment:** Repair facility caller explicitly asked for a representative — twice — and the bot still failed to escalate. D1=1 transfer-intent miss. Customer eventually said "portfolio" (garbled), bot asked to rephrase, call ended without transfer.

**Transcript:**
```
  Talker: Thanks for calling Assurant! To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Repair facility. Please speak with representative.
  Talker: One moment please.
  Customer: All you gotta do is just the repair facility. I wanna speak with a representative and send you right through.
  Talker: Let me check on that.
  Customer: portfolio.
  Talker: I want to make sure I help you correctly. Could you rephrase that for me?
```

### Lowest scorer: CONV 151 — 2.96/5 (49/100)
**Conv ID:** [`3014101863-1221005809-2288644537-1659749027`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3014101863-1221005809-2288644537-1659749027?organization=assurantauto)  
**Date:** 2026-05-06  |  **Tasks:** CallerIdentification, CallerIdentification, ContractHolderIssues  
**Flags:** 🚫 ABAND  
**Assessment:** Lowest weighted score of the week — see flags.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Insurance.
  Talker: One moment please.
  Talker: Could you please clarify if you are the contract holder, a dealership, a repair facility, or an employee?
  Customer: Representative.
  Talker: Let me check on that.
  Talker: Are you calling from a repair facility or a dealership?
  Customer: No.
  Talker: Just a second.
  Talker: I'm sorry, but I am unable to assist further since your caller type does not match any of the supported categories. Is there anything else you need help with?
  Customer: Representative.
  Talker: Thank you for clarifying. Since your caller type does not match any of the supported categories, I am unable to assist further. Is there anything else I can help you with?
  Customer: Operator.
  Talker: Thanks for that information. Is there anything else I can assist you with today?
  Customer: No.
```

---

## Section 7: Systemic Issues (Week)

Carried forward from prior reports; weekly recurrence noted.

### Issue 1 — Claim/VIN ASR Failures
*High severity. Persists from Wk17-19.* Core vocabulary like 'claim' and 'VIN' is mis-transcribed (claim → flame/lame/plain/piece, VIN → thin). This week 2 instances. No improvement trend over prior 3 weeks.

### Issue 3 — Transfer Intent Not Recognized
*Medium-High severity. Declining trend.* "Representative" / "agent" / "operator" still occasionally triggers disambiguation instead of immediate transfer. Wk16=1, Wk17=5, Wk18=2, this week (Wk19 within May 4-10) = 0 — appears to have resolved.

### Issue 4 — Chat Upsell Before Phone Transfer
*Low-Medium severity. Systemic.* The bot still nudges callers to chat / portal after they've explicitly asked for a phone agent. Pattern present across the week in ~60% of phone-transfer flows.

### Issue 10 — "Account pulled up" greeting then re-asks for caller type
*Low severity. New pattern.* 2 instances on May 5. Bot opens "I have your account information pulled up" (ANI-matched path) but then asks the caller-type disambiguation question anyway. May indicate a recent prompt change worth verifying.

### NEW Issue 11 — Dealer-phone misrouted to ContractHolderIssues
*Medium severity. Data integrity issue.* This week's analysis identified 4 of 102 CH-routed calls (~4%) where a dealership phone is stored in the customer-phone field on contracts in GLOW. Salem Ford, Moss Bros, Williams Toyota of Elmira, and an Assurant employee-benefit line all show this pattern. Most striking: 3260951102 (ANI 7144528088) where the caller said "I am the selling dealer" but bot routed to ContractHolderIssues and set user_type=other. Cannot be fixed in the bot — upstream contract entry needs cleanup.

---

## Comparison to Running Baseline (Apr 18 – May 9, 140 scored)

| Metric | This Week (May 4-10) | Baseline | Δ |
|---|---|---|---|
| Pass rate | 57.4% | 49.3% | **+8.1 pp** |
| Mean score (/5) | 4.09 | 3.99 | **+0.09** |
| Scored conversations | 68 | 140 | — |

- **Pass rate improved by 8.1 pp** vs. running baseline.
