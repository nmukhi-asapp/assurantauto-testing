## Weekly Voice Quality Report — CallerIdentification

*Week of 2026-05-18 (Mon) → 2026-05-23 (Sat) | Generated 2026-05-23*  
*Scoring under the re-anchored rubric (effective 2026-05-13). Prior weeks have been re-scored under the same rubric for consistent WoW comparison.*

Conversations scored: 68  |  Force-skipped (no caller dialogue): see baseline doc

| Metric | Value |
|---|---|
| Mean overall score | 3.76 / 5 (75/100) |
| **Pass rate** | **49/68 = 72.1%** |
| Conversations scoring < 3.0 | 5 (7%) |
| Safety / policy flags | 0 |
| Critical hallucination flags | 0 |
| Abandoned calls | 8 |

> **Scale reminder.** Under the re-anchored rubric, **3.0–3.5 = failing internal QA**, 3.5–4.0 = borderline, 4.0+ = solid.

---

## Section 1.5: Pass / Fail

PASS iff D1 ≥ 4 AND no frustration indicators.

| Metric | Value |
|---|---|
| **Pass rate** | **49/68 = 72.1%** |
| Fail | 19 (27.9%) |

### Daily Pass/Fail Trend

| Date | Total | Pass | % Pass | Trend |
|------|-------|------|--------|-------|
| 2026-05-18 | 9 | 6 | 67% | █████████████████········ |
| 2026-05-19 | 14 | 8 | 57% | ██████████████··········· |
| 2026-05-20 | 20 | 15 | 75% | ███████████████████······ |
| 2026-05-21 | 9 | 9 | 100% | █████████████████████████ |
| 2026-05-22 | 15 | 10 | 67% | █████████████████········ |
| 2026-05-23 | 1 | 1 | 100% | █████████████████████████ |

---

## Section 2: Daily Score Trend

| Date | N | Mean /5 | /100 | Trend |
|------|---|---------|------|-------|
| 2026-05-18 | 9 | 3.76 | 75 | ██████████████████████········ |
| 2026-05-19 | 14 | 3.55 | 71 | █████████████████████········· |
| 2026-05-20 | 20 | 3.79 | 76 | ███████████████████████······· |
| 2026-05-21 | 9 | 4.16 | 83 | █████████████████████████····· |
| 2026-05-22 | 15 | 3.65 | 73 | ██████████████████████········ |
| 2026-05-23 | 1 | 4.06 | 81 | ████████████████████████······ |

---

## Section 3: Dimension Heatmap

| Dim | Name | Weight | Mean | Std | Min | Max | %≤2 |
|-----|------|--------|------|-----|-----|-----|------|
| D1 | Design Adherence | 20% | 3.32 | 0.97 | 1 | 5 | 24% |
| D2 | Information Accuracy | 10% | 4.04 | 0.44 | 3 | 5 | 0% |
| D3 | Context Retention | 10% | 3.91 | 0.84 | 2 | 5 | 6% |
| D4 | Response Latency | 10% | 3.99 | 0.12 | 3 | 4 | 0% |
| D5 | Turn-Taking | 8% | 3.99 | 0.12 | 3 | 4 | 0% |
| D6 | Repair & Recovery | 7% | 3.28 | 0.83 | 2 | 5 | 18% |
| D8 | Tone | 5% | 3.78 | 0.48 | 2 | 5 | 1% |
| D9 | Verbosity | 5% | 3.82 | 0.71 | 2 | 5 | 1% |
| D10 | ASR | 5% | 3.96 | 0.78 | 2 | 5 | 1% |
| D12 | Policy & Safety | 10% | 3.99 | 0.80 | 2 | 5 | 6% |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 4: Per-Conversation Scores

| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | P/F | Flags |
|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-----|-------|
| [CONV 1](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0482468177-1377964529-2833039861-1773867395?organization=assurantauto) | 05-18 | 14 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 4.00 (80) | ✓ PASS | — |
| [CONV 2](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1826820468-1378030065-2154596672-3594676577?organization=assurantauto) | 05-18 | 12 | 3 | 3 | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 4 | 3.34 (67) | ✗ FAIL | — |
| [CONV 3](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1877670037-1377767921-2559558133-1773867395?organization=assurantauto) | 05-18 | 4 | 2 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.48 (70) | ✗ FAIL | ABANDONED |
| [CONV 4](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2419691510-1380717041-2972944704-3594676577?organization=assurantauto) | 05-18 | 9 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 3.31 (66) | ✗ FAIL | — |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2879550793-1378030065-2543829493-1773867395?organization=assurantauto) | 05-18 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 3.83 (77) | ✓ PASS | ABANDONED |
| [CONV 6](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3008296336-1375015409-2776875509-1773867395?organization=assurantauto) | 05-18 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4.11 (82) | ✓ PASS | — |
| [CONV 7](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3186337246-1377702385-2197340661-1773867395?organization=assurantauto) | 05-18 | 23 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.70 (74) | ✓ PASS | — |
| [CONV 8](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3374584035-1376653809-2911224309-1773867395?organization=assurantauto) | 05-18 | 22 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3.53 (71) | ✓ PASS | — |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3412290305-1377047025-2660745717-1773867395?organization=assurantauto) | 05-18 | 20 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.50 (90) | ✓ PASS | — |
| [CONV 10](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0700046509-1390285297-2857273664-3594676577?organization=assurantauto) | 05-19 | 32 | 1 | 3 | 2 | 4 | 4 | 2 | 3 | 3 | 4 | 3 | 2.62 (52) | ✗ FAIL | ABANDONED |
| [CONV 11](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0750593503-1390219761-2424342848-3594676577?organization=assurantauto) | 05-19 | 17 | 3 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 3.89 (78) | ✓ PASS | — |
| [CONV 12](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1165175064-1389040113-2723004917-1773867395?organization=assurantauto) | 05-19 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3.78 (76) | ✓ PASS | — |
| [CONV 13](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1263637076-1390547441-2556922176-3594676577?organization=assurantauto) | 05-19 | 6 | 2 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 2 | 3.31 (66) | ✗ FAIL | — |
| [CONV 14](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1433396036-1389302257-2664270144-3594676577?organization=assurantauto) | 05-19 | 31 | 2 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 4 | 3 | 3.09 (62) | ✗ FAIL | — |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1522139949-1393037809-2815082997-1773867395?organization=assurantauto) | 05-19 | 26 | 2 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3 | 2 | 2.84 (57) | ✗ FAIL | — |
| [CONV 16](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2186399567-1388909041-2223671616-3594676577?organization=assurantauto) | 05-19 | 12 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.70 (74) | ✓ PASS | — |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2607439919-1389892081-2311832053-1773867395?organization=assurantauto) | 05-19 | 19 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.87 (77) | ✓ PASS | — |
| [CONV 18](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2833004169-1390481905-2278394176-3594676577?organization=assurantauto) | 05-19 | 12 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.50 (90) | ✓ PASS | — |
| [CONV 19](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3351813446-1390940657-3205480949-1773867395?organization=assurantauto) | 05-19 | 21 | 2 | 4 | 2 | 4 | 4 | 2 | 3 | 3 | 3 | 3 | 2.90 (58) | ✗ FAIL | — |
| [CONV 20](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3837411393-1393562097-2774567232-3594676577?organization=assurantauto) | 05-19 | 24 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 3.70 (74) | ✓ PASS | — |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3916085332-1390744049-2941370869-1773867395?organization=assurantauto) | 05-19 | 32 | 2 | 4 | 3 | 4 | 4 | 2 | 3 | 3 | 3 | 3 | 3.01 (60) | ✗ FAIL | — |
| [CONV 22](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4032218088-1387663857-2269088064-3594676577?organization=assurantauto) | 05-19 | 12 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4.44 (89) | ✓ PASS | — |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4144091124-1391858161-2594736448-3594676577?organization=assurantauto) | 05-19 | 19 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4.03 (81) | ✓ PASS | — |
| [CONV 24](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0301526269-1403130353-2926545216-3594676577?organization=assurantauto) | 05-20 | 15 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 4.26 (85) | ✓ PASS | — |
| [CONV 25](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1128039730-1404178929-2364457461-1773867395?organization=assurantauto) | 05-20 | 12 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 3.76 (75) | ✓ PASS | — |
| [CONV 26](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1285303874-1404768753-2562689344-3594676577?organization=assurantauto) | 05-20 | 39 | 3 | 4 | 2 | 4 | 4 | 2 | 4 | 3 | 4 | 4 | 3.34 (67) | ✗ FAIL | — |
| [CONV 27](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1304381900-1402540529-2153955829-1773867395?organization=assurantauto) | 05-20 | 13 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3.64 (73) | ✓ PASS | — |
| [CONV 28](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2008114990-1403589105-2726216181-1773867395?organization=assurantauto) | 05-20 | 16 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.87 (77) | ✓ PASS | — |
| [CONV 29](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2266845133-1404310001-2332213749-1773867395?organization=assurantauto) | 05-20 | 15 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.64 (73) | ✓ PASS | — |
| [CONV 30](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2316820171-1402016241-2345503040-3594676577?organization=assurantauto) | 05-20 | 21 | 2 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 3.26 (65) | ✗ FAIL | — |
| [CONV 31](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2609152972-1402081777-2588918261-1773867395?organization=assurantauto) | 05-20 | 10 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.48 (70) | ✗ FAIL | — |
| [CONV 32](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2777527569-1404375537-3165161792-3594676577?organization=assurantauto) | 05-20 | 14 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4.22 (84) | ✓ PASS | — |
| [CONV 33](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2822538112-1405358577-3156197877-1773867395?organization=assurantauto) | 05-20 | 23 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4.56 (91) | ✓ PASS | — |
| [CONV 34](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2870400520-1402016241-2223423989-1773867395?organization=assurantauto) | 05-20 | 15 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4.52 (90) | ✓ PASS | — |
| [CONV 35](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3001945888-1401426417-2341782005-1773867395?organization=assurantauto) | 05-20 | 11 | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 2 | 2.98 (60) | ✗ FAIL | — |
| [CONV 36](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3325106448-1405555185-2329395701-1773867395?organization=assurantauto) | 05-20 | 21 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 37](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3406085218-1403589105-3135080768-3594676577?organization=assurantauto) | 05-20 | 19 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.76 (75) | ✓ PASS | — |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3419836940-1405817329-2834481653-1773867395?organization=assurantauto) | 05-20 | 7 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4.80 (96) | ✓ PASS | — |
| [CONV 39](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3449184562-1405751793-2983168320-3594676577?organization=assurantauto) | 05-20 | 18 | 2 | 4 | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 2 | 3.01 (60) | ✗ FAIL | — |
| [CONV 40](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3629673613-1404768753-2415444469-1773867395?organization=assurantauto) | 05-20 | 4 | 2 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 3.50 (70) | ✓ PASS | — |
| [CONV 41](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3661049974-1403458033-3086205429-1773867395?organization=assurantauto) | 05-20 | 14 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3.64 (73) | ✓ PASS | — |
| [CONV 42](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3673574996-1401885169-2779482432-3594676577?organization=assurantauto) | 05-20 | 24 | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3.64 (73) | ✓ PASS | — |
| [CONV 43](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3861483472-1401360881-3199895872-3594676577?organization=assurantauto) | 05-20 | 18 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | 3.72 (74) | ✓ PASS | — |
| [CONV 44](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0634000074-1414861297-2212858176-3594676577?organization=assurantauto) | 05-21 | 6 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.17 (83) | ✓ PASS | — |
| [CONV 45](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2224363715-1417613809-3161688384-3594676577?organization=assurantauto) | 05-21 | 14 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 3 | 4 | 3.92 (78) | ✓ PASS | — |
| [CONV 46](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2503372958-1417351665-2477885760-3594676577?organization=assurantauto) | 05-21 | 3 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.44 (89) | ✓ PASS | — |
| [CONV 47](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2519884784-1417875953-2176172533-1773867395?organization=assurantauto) | 05-21 | 20 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (88) | ✓ PASS | — |
| [CONV 48](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2786743658-1417613809-3217983808-3594676577?organization=assurantauto) | 05-21 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.41 (88) | ✓ PASS | — |
| [CONV 49](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2892887667-1414795761-3122825536-3594676577?organization=assurantauto) | 05-21 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.70 (74) | ✓ PASS | ABANDONED |
| [CONV 50](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2952200137-1418007025-3123888629-1773867395?organization=assurantauto) | 05-21 | 24 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 3.87 (77) | ✓ PASS | — |
| [CONV 51](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2960262622-1418072561-2488320501-1773867395?organization=assurantauto) | 05-21 | 7 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4.33 (87) | ✓ PASS | — |
| [CONV 52](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3934013696-1417613809-2264303936-3594676577?organization=assurantauto) | 05-21 | 25 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 53](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0115970268-1430131185-2304543040-3594676577?organization=assurantauto) | 05-22 | 6 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 4.00 (80) | ✓ PASS | ABANDONED |
| [CONV 54](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0304031398-1431376369-2172436981-1773867395?organization=assurantauto) | 05-22 | 15 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 55](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0355718901-1432031729-3029189109-1773867395?organization=assurantauto) | 05-22 | 7 | 2 | 4 | 3 | 4 | 4 | 2 | 4 | 4 | 3 | 4 | 3.23 (65) | ✗ FAIL | ABANDONED |
| [CONV 56](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0804668998-1432031729-2944371008-3594676577?organization=assurantauto) | 05-22 | 37 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.87 (77) | ✓ PASS | — |
| [CONV 57](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1189260666-1426985457-2525006144-3594676577?organization=assurantauto) | 05-22 | 7 | 2 | 4 | 4 | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 3.23 (65) | ✗ FAIL | — |
| [CONV 58](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1196398450-1429606897-2607530485-1773867395?organization=assurantauto) | 05-22 | 17 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.59 (72) | ✓ PASS | — |
| [CONV 59](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1438919296-1427444209-2863171904-3594676577?organization=assurantauto) | 05-22 | 24 | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 4.00 (80) | ✓ PASS | — |
| [CONV 60](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1900627521-1430065649-2379530741-1773867395?organization=assurantauto) | 05-22 | 25 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.81 (76) | ✓ PASS | — |
| [CONV 61](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1944150293-1430131185-2474019136-3594676577?organization=assurantauto) | 05-22 | 15 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3.78 (76) | ✓ PASS | — |
| [CONV 62](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2505000701-1428689393-2975304000-3594676577?organization=assurantauto) | 05-22 | 16 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3.89 (78) | ✓ PASS | — |
| [CONV 63](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2616988110-1428623857-2593950016-3594676577?organization=assurantauto) | 05-22 | 23 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4.30 (86) | ✓ PASS | — |
| [CONV 64](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3297018882-1432031729-3182397760-3594676577?organization=assurantauto) | 05-22 | 25 | 2 | 4 | 3 | 4 | 4 | 2 | 3 | 4 | 2 | 3 | 3.01 (60) | ✗ FAIL | — |
| [CONV 65](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3742430796-1428689393-2629550581-1773867395?organization=assurantauto) | 05-22 | 16 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.70 (74) | ✓ PASS | — |
| [CONV 66](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4025058174-1431769585-2766768448-3594676577?organization=assurantauto) | 05-22 | 24 | 2 | 4 | 2 | 4 | 4 | 2 | 3 | 3 | 3 | 3 | 2.90 (58) | ✗ FAIL | ABANDONED |
| [CONV 67](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4037200496-1431835121-3181807936-3594676577?organization=assurantauto) | 05-22 | 50 | 3 | 4 | 3 | 4 | 4 | 2 | 3 | 2 | 3 | 4 | 3.29 (66) | ✗ FAIL | ABANDONED |
| [CONV 68](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0946967104-1441927665-2652604736-3594676577?organization=assurantauto) | 05-23 | 8 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4.06 (81) | ✓ PASS | — |

---

## Section 5: Flagged Conversations

*Criteria: any flag, score < 2.5, D1 ≤ 2, or D12 ≤ 2 — 20 of 68.*

| Date | D1 | D12 | Score | Flags | Conv ID | Notes |
|------|----|----|-------|-------|---------|-------|
| 05-19 | 1 | 3 | 2.62 | ABANDONED | [`0700046509-1390285297-28...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0700046509-1390285297-2857273664-3594676577?organization=assurantauto) | Bot collected a VIN identifier from the caller, failed lookup, then asked for the identifier AGAIN before transfer and ultimately ended the call instead of transferring despite repeated explicit agent |
| 05-19 | 2 | 2 | 2.84 | — | [`1522139949-1393037809-28...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1522139949-1393037809-2815082997-1773867395?organization=assurantauto) | Bot transferred to a Claims Agent without ever collecting an identifier from the repair facility (no VIN/claim/contract number), violating the pre-escalation identifier requirement (D1=2, D12=2). Repa |
| 05-19 | 2 | 3 | 2.90 | — | [`3351813446-1390940657-32...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3351813446-1390940657-3205480949-1773867395?organization=assurantauto) | Bot performed Smart Deflection appropriately on the first agent request, but after the caller insisted multiple times on a human, the bot kept looping with clarification questions instead of transferr |
| 05-22 | 2 | 3 | 2.90 | ABANDONED | [`4025058174-1431769585-27...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4025058174-1431769585-2766768448-3594676577?organization=assurantauto) | Bot failed to recognize repeated 'Representative' requests and never escalated to a human despite clear insistence (D1, D6 failure). Context was lost — bot re-asked for identifier after caller provide |
| 05-20 | 2 | 2 | 2.98 | — | [`3001945888-1401426417-23...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3001945888-1401426417-2341782005-1773867395?organization=assurantauto) | Bot transferred to Customer Care without collecting any identifier (no contract/claim number or VIN asked), violating the pre-escalation identifier collection requirement (D1=2, D12=2). The flow was a |
| 05-22 | 2 | 3 | 3.01 | — | [`3297018882-1432031729-31...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3297018882-1432031729-3182397760-3594676577?organization=assurantauto) | Bot escalated to a live agent without successfully collecting any identifier (contract/claim/VIN), violating the pre-escalation identifier requirement (D1=2). ASR struggled badly with the caller's spe |
| 05-20 | 2 | 2 | 3.01 | — | [`3449184562-1405751793-29...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3449184562-1405751793-2983168320-3594676577?organization=assurantauto) | Bot transferred to agent without collecting any identifier (contract/claim number or VIN) after phone lookup failed — D1 and D12 violation per required pre-escalation identifier collection. Repair/rec |
| 05-19 | 2 | 3 | 3.01 | — | [`3916085332-1390744049-29...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3916085332-1390744049-2941370869-1773867395?organization=assurantauto) | Caller identified as dealer but bot did not follow dealer claim funneling design and instead got confused by the caller's side-conversation chatter. Bot escalated to a Claims Agent with only a 7-chara |
| 05-19 | 2 | 3 | 3.09 | — | [`1433396036-1389302257-26...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1433396036-1389302257-2664270144-3594676577?organization=assurantauto) | The bot scolded the caller for profanity in a way that felt preachy and inappropriate (D8/D12 concern), and repeatedly asked clarifying questions even after the caller said 'transfer me' multiple time |
| 05-22 | 2 | 4 | 3.23 | ABANDONED | [`0355718901-1432031729-30...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0355718901-1432031729-3029189109-1773867395?organization=assurantauto) | Caller asked for a representative but the bot did not follow the Smart Deflection / escalation protocol — instead it pivoted to asking for a phone number to look up an account, ignoring the agent requ |
| 05-22 | 2 | 3 | 3.23 | — | [`1189260666-1426985457-25...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1189260666-1426985457-2525006144-3594676577?organization=assurantauto) | Bot only asked for an identifier once before transferring (design requires two asks before escalation), and the caller is a contract holder where phone lookup should have satisfied identification — in |
| 05-20 | 2 | 3 | 3.26 | — | [`2316820171-1402016241-23...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2316820171-1402016241-2345503040-3594676577?organization=assurantauto) | Bot escalated to a Claims Agent without successfully collecting any identifier (VIN was asked but never provided), violating the pre-escalation identifier requirement for dealer callers (D1=2). Caller |
| 05-22 | 3 | 4 | 3.29 | ABANDONED | [`4037200496-1431835121-31...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4037200496-1431835121-3181807936-3594676577?organization=assurantauto) | Bot got stuck in a repetitive loop asking for confirmation that the repair order email was sent, repeating the same email address and instruction 8+ times despite obvious caller confusion. Repair & Re |
| 05-19 | 2 | 2 | 3.31 | — | [`1263637076-1390547441-25...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1263637076-1390547441-2556922176-3594676577?organization=assurantauto) | Bot transferred to Customer Care without collecting any identifier (no contract/claim/VIN asked) — violates pre-escalation identifier requirement (D1=2, D12=2). Smart Deflection attempt was minimal (j |
| 05-18 | 2 | 3 | 3.31 | — | [`2419691510-1380717041-29...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2419691510-1380717041-2972944704-3594676577?organization=assurantauto) | Bot escalated to a live agent without successfully collecting any identifier (contract/claim/VIN) — caller declined and bot transferred anyway, violating the pre-escalation identifier requirement (D1= |
| 05-18 | 2 | 4 | 3.48 | ABANDONED | [`1877670037-1377767921-25...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1877670037-1377767921-2559558133-1773867395?organization=assurantauto) | The transcript ends mid-flow with the bot saying it's checking contracts/claims after the caller requested a representative. There's no evidence of Smart Deflection being attempted (personalized offer |
| 05-20 | 2 | 3 | 3.50 | — | [`3629673613-1404768753-24...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3629673613-1404768753-2415444469-1773867395?organization=assurantauto) | Bot transferred to Customer Care on the first agent request without attempting Smart Deflection (Guardrail 6) and without collecting/confirming any identifier pre-transfer. D1 penalized for skipping r |
| 05-21 | 3 | 4 | 3.70 | ABANDONED | [`2892887667-1414795761-31...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2892887667-1414795761-3122825536-3594676577?organization=assurantauto) | Call appears truncated/abandoned after the bot said 'One moment while I check on that' — the customer's follow-up ('number.') suggests they began providing info but the call ended with no progress on  |
| 05-18 | 3 | 4 | 3.83 | ABANDONED | [`2879550793-1378030065-25...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2879550793-1378030065-2543829493-1773867395?organization=assurantauto) | Transcript ends abruptly after the bot says it's checking contracts/claims for a dealer caller — no further interaction occurs. The DealershipIssues task never actually engages the caller, suggesting  |
| 05-22 | 4 | 4 | 4.00 | ABANDONED | [`0115970268-1430131185-23...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0115970268-1430131185-2304543040-3594676577?organization=assurantauto) | Call appears abandoned mid-identifier collection after caller gave only a partial phone number. ASR may have only captured 7 digits ('four zero three five three two nine'), suggesting a possible recog |

---

## Section 6: Representative Examples

### Highest scorer: 4.80/5 (96/100)
**Conv ID:** [`3419836940-1405817329-2834481653-1773867395`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3419836940-1405817329-2834481653-1773867395?organization=assurantauto)  
**Date:** 2026-05-20  |  **Tasks:** CallerIdentification, CallerIdentification, ContractHolderIssues  |  **D1:** 5  |  **D12:** 5
**Flags:** —  
**Notes:** Bot correctly applied Smart Deflection on first agent request, personalized with vehicle/claim context, then transferred on the second insistence per design. Identifier was satisfied via phone-based account lookup for contract holder. Clean, textbook execution.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! I have your account information pulled up... how can I help you today?
  Customer: I need to speak to an agent.
  Talker: Let me see what I can do for you.
  Talker: I can help you get an agent. But I can see you have a **** JEEP WRANGLER on file, and you recently filed a claim on ****-**-**. I can help you check the claim's status, answer questions about your contract, and I will direct you to the right folks if it is something I can't handle. Can you describe what you need?
  Customer: I need to speak to an agent.
  Talker: One moment.
  Talker: Hold on while I transfer you to Customer Care.
```

### Most notable failure: 2.62/5 (52/100)
**Conv ID:** [`0700046509-1390285297-2857273664-3594676577`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0700046509-1390285297-2857273664-3594676577?organization=assurantauto)  
**Date:** 2026-05-19  |  **Tasks:** CallerIdentification, CallerIdentification, RepairShopIssues  |  **D1:** 1  |  **D12:** 3
**Flags:** ABANDONED  
**Notes:** Bot collected a VIN identifier from the caller, failed lookup, then asked for the identifier AGAIN before transfer and ultimately ended the call instead of transferring despite repeated explicit agent requests — a critical D1 failure (refused to escalate when required, caller stuck in loop and abandoned frustrated). D6/D3 also poor: bot re-asked for identifier already provided, and repair-coverage question was never addressed. Caller clearly frustrated ('What a waste').  

**Transcript:**
```
  Talker: Thanks for calling Assurant! Let's get you to the right place... are you a customer, a dealer, or a repair facility?
  Customer: repair facility
  Talker: Please hold for a moment while I connect you.
  Talker: What can I help you with today — are you checking on an existing claim, starting a new claim, or something else?
  Customer: Start a claim.
  Talker: One moment please.
  Talker: Have you already emailed the Repair Order to Assurant?
  Customer: No.
  Talker: Just a second.
  Talker: Would you prefer to file the claim online, which is the fastest option, or would you like me to walk you through the process over the phone?
  Customer: Agent.
  Talker: Before I connect you — just so you know, independent repair facilities like yours can file claims, check claim status, provide documentation, and check payment status at auto claims dot com.
  Customer: Agents.
  Talker: Please hold while I connect you.
  Talker: What specifically do you need help with regarding starting the new claim?
  Customer: Claim coverage.
  Talker: Hold on please.
  Talker: Could you let me know the claim number, contract number, or the last 8 characters of the Vin so I can check the coverage details for you?
  Customer: K j two one one two four nine
  Talker: Is that your contract number or the last 8 characters of your Vin?
  Customer: Ven.
  Talker: Let me check on that.
  Talker: I was not able to find any claims associated with that Vin, so would you like to be connected with a human agent?
  Customer: Yes. That's what I said the first time. Agent.
  Talker: Happy to help!
  Talker: Before I transfer you, could you provide your claim number, contract number, or the last 8 characters of your Vin so I can proceed?
  Customer: Oh my god. Agent.
  Talker: Please hold while I connect you.
  Customer: {pii_immediate_genagent_persistence.LOC:********}.
  Talker: Please hold while I connect you.
  Talker: Thank you for calling Assurant. Please feel free to call back when you have your claim number, contract number, or Vin available, and we’ll be happy to assist you. Have a great day.
  Customer: What a waste.
```

### Lowest scorer: 2.62/5 (52/100)
**Conv ID:** [`0700046509-1390285297-2857273664-3594676577`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0700046509-1390285297-2857273664-3594676577?organization=assurantauto)  
**Date:** 2026-05-19  |  **Tasks:** CallerIdentification, CallerIdentification, RepairShopIssues  |  **D1:** 1  |  **D12:** 3
**Flags:** ABANDONED  
**Notes:** Bot collected a VIN identifier from the caller, failed lookup, then asked for the identifier AGAIN before transfer and ultimately ended the call instead of transferring despite repeated explicit agent requests — a critical D1 failure (refused to escalate when required, caller stuck in loop and abandoned frustrated). D6/D3 also poor: bot re-asked for identifier already provided, and repair-coverage question was never addressed. Caller clearly frustrated ('What a waste').  

**Transcript:**
```
  Talker: Thanks for calling Assurant! Let's get you to the right place... are you a customer, a dealer, or a repair facility?
  Customer: repair facility
  Talker: Please hold for a moment while I connect you.
  Talker: What can I help you with today — are you checking on an existing claim, starting a new claim, or something else?
  Customer: Start a claim.
  Talker: One moment please.
  Talker: Have you already emailed the Repair Order to Assurant?
  Customer: No.
  Talker: Just a second.
  Talker: Would you prefer to file the claim online, which is the fastest option, or would you like me to walk you through the process over the phone?
  Customer: Agent.
  Talker: Before I connect you — just so you know, independent repair facilities like yours can file claims, check claim status, provide documentation, and check payment status at auto claims dot com.
  Customer: Agents.
  Talker: Please hold while I connect you.
  Talker: What specifically do you need help with regarding starting the new claim?
  Customer: Claim coverage.
  Talker: Hold on please.
  Talker: Could you let me know the claim number, contract number, or the last 8 characters of the Vin so I can check the coverage details for you?
  Customer: K j two one one two four nine
  Talker: Is that your contract number or the last 8 characters of your Vin?
  Customer: Ven.
  Talker: Let me check on that.
  Talker: I was not able to find any claims associated with that Vin, so would you like to be connected with a human agent?
  Customer: Yes. That's what I said the first time. Agent.
  Talker: Happy to help!
  Talker: Before I transfer you, could you provide your claim number, contract number, or the last 8 characters of your Vin so I can proceed?
  Customer: Oh my god. Agent.
  Talker: Please hold while I connect you.
  Customer: {pii_immediate_genagent_persistence.LOC:********}.
  Talker: Please hold while I connect you.
  Talker: Thank you for calling Assurant. Please feel free to call back when you have your claim number, contract number, or Vin available, and we’ll be happy to assist you. Have a great day.
  Customer: What a waste.
```

---

## Section 7: Systemic Issues (Week)

- **Transfer-intent not recognized** — flagged in 1 of 68 calls (1%) in notes.
- **ASR mishearing** — flagged in 4 of 68 calls (6%) in notes.
- **Repeated questions / poor context retention** — flagged in 5 of 68 calls (7%) in notes.
- **Generic response did not address specific need** — flagged in 9 of 68 calls (13%) in notes.
- **Excessive filler / verbosity** — flagged in 16 of 68 calls (24%) in notes.

---

## Comparison vs. Re-scored Baseline (Apr 18 onward)

| Metric | This Week | Baseline | Δ |
|---|---|---|---|
| Pass rate | 72.1% | 68.1% | **+3.9 pp** |
| Mean score (/5) | 3.76 | 3.78 | **-0.02** |
| Scored conversations | 68 | 254 | — |
