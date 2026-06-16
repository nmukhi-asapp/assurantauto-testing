## Weekly Voice Quality Report — CallerIdentification

*Week of 2026-05-25 (Mon) → 2026-05-29 (Sat) | Generated 2026-05-29*  
*Scoring under the re-anchored rubric (effective 2026-05-13). Prior weeks have been re-scored under the same rubric for consistent WoW comparison.*

Conversations scored: 50  |  Force-skipped (no caller dialogue): see baseline doc

| Metric | Value |
|---|---|
| Mean overall score | 4.06 / 5 (81/100) |
| **Pass rate** | **45/50 = 90.0%** |
| Conversations scoring < 3.0 | 3 (6%) |
| Safety / policy flags | 0 |
| Critical hallucination flags | 0 |
| Abandoned calls | 2 |

> **Scale reminder.** Under the re-anchored rubric, **3.0–3.5 = failing internal QA**, 3.5–4.0 = borderline, 4.0+ = solid.

---

## Section 1.5: Pass / Fail

PASS iff D1 ≥ 4 AND no frustration indicators.

| Metric | Value |
|---|---|
| **Pass rate** | **45/50 = 90.0%** |
| Fail | 5 (10.0%) |

### Daily Pass/Fail Trend

| Date | Total | Pass | % Pass | Trend |
|------|-------|------|--------|-------|
| 2026-05-25 | 1 | 1 | 100% | █████████████████████████ |
| 2026-05-26 | 9 | 8 | 89% | ██████████████████████··· |
| 2026-05-27 | 16 | 14 | 88% | ██████████████████████··· |
| 2026-05-28 | 11 | 10 | 91% | ███████████████████████·· |
| 2026-05-29 | 13 | 12 | 92% | ███████████████████████·· |

---

## Section 2: Daily Score Trend

| Date | N | Mean /5 | /100 | Trend |
|------|---|---------|------|-------|
| 2026-05-25 | 1 | 4.80 | 96 | █████████████████████████████· |
| 2026-05-26 | 9 | 4.00 | 80 | ████████████████████████······ |
| 2026-05-27 | 16 | 3.98 | 80 | ████████████████████████······ |
| 2026-05-28 | 11 | 4.12 | 82 | █████████████████████████····· |
| 2026-05-29 | 13 | 4.08 | 82 | █████████████████████████····· |

---

## Section 3: Dimension Heatmap

| Dim | Name | Weight | Mean | Std | Min | Max | %≤2 |
|-----|------|--------|------|-----|-----|-----|------|
| D1 | Design Adherence | 20% | 3.78 | 0.82 | 1 | 5 | 6% |
| D2 | Information Accuracy | 10% | 4.06 | 0.62 | 2 | 5 | 2% |
| D3 | Context Retention | 10% | 4.36 | 0.78 | 2 | 5 | 2% |
| D4 | Response Latency | 10% | 4.00 | 0.00 | 4 | 4 | 0% |
| D5 | Turn-Taking | 8% | 4.00 | 0.00 | 4 | 4 | 0% |
| D6 | Repair & Recovery | 7% | 3.66 | 0.89 | 1 | 5 | 8% |
| D8 | Tone | 5% | 3.92 | 0.40 | 2 | 5 | 2% |
| D9 | Verbosity | 5% | 4.28 | 0.67 | 3 | 5 | 0% |
| D10 | ASR | 5% | 4.20 | 0.88 | 2 | 5 | 4% |
| D12 | Policy & Safety | 10% | 4.56 | 0.64 | 2 | 5 | 2% |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 4: Per-Conversation Scores

| # | Date | Turns | D1 | D2 | D3 | D4 | D5 | D6 | D8 | D9 | D10 | D12 | Score | P/F | Flags |
|---|------|-------|----|----|----|----|----|----|----|-----|-----|-----|-------|-----|-------|
| [CONV 1](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1138490278-1470370289-2397749749-1773867395?organization=assurantauto) | 05-25 | 10 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4.80 (96) | ✓ PASS | — |
| [CONV 2](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0039907489-1479741937-2999224640-3594676577?organization=assurantauto) | 05-26 | 13 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 4 | 4.14 (83) | ✓ PASS | — |
| [CONV 3](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0405516622-1481904625-2992423413-1773867395?organization=assurantauto) | 05-26 | 16 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4.09 (82) | ✓ PASS | — |
| [CONV 4](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1707924818-1483805169-3114895680-3594676577?organization=assurantauto) | 05-26 | 29 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 5](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1893740349-1483215345-2915615221-1773867395?organization=assurantauto) | 05-26 | 13 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3.67 (73) | ✓ PASS | — |
| [CONV 6](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2649478448-1484132849-2726136128-3594676577?organization=assurantauto) | 05-26 | 25 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4.03 (81) | ✓ PASS | — |
| [CONV 7](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2877745328-1479938545-2703264064-3594676577?organization=assurantauto) | 05-26 | 13 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 4.26 (85) | ✓ PASS | — |
| [CONV 8](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3060674078-1485246961-2634975552-3594676577?organization=assurantauto) | 05-26 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 3.83 (77) | ✓ PASS | — |
| [CONV 9](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3796567392-1485312497-3119614272-3594676577?organization=assurantauto) | 05-26 | 22 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (86) | ✓ PASS | — |
| [CONV 10](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3940792155-1483739633-2173616629-1773867395?organization=assurantauto) | 05-26 | 16 | 3 | 4 | 3 | 4 | 4 | 2 | 4 | 4 | 3 | 4 | 3.46 (69) | ✗ FAIL | ABANDONED |
| [CONV 11](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0151798507-1499402737-3069034997-1773867395?organization=assurantauto) | 05-27 | 33 | 3 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.76 (75) | ✓ PASS | — |
| [CONV 12](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0744460174-1496781297-2644951541-1773867395?organization=assurantauto) | 05-27 | 28 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 3.98 (80) | ✓ PASS | — |
| [CONV 13](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0802980647-1499206129-2896595264-3594676577?organization=assurantauto) | 05-27 | 21 | 4 | 5 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.92 (78) | ✓ PASS | — |
| [CONV 14](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0824066437-1497895409-3074787648-3594676577?organization=assurantauto) | 05-27 | 14 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.44 (89) | ✓ PASS | — |
| [CONV 15](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1378342986-1493701105-2766506304-3594676577?organization=assurantauto) | 05-27 | 13 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.56 (91) | ✓ PASS | — |
| [CONV 16](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1431614093-1496388081-2857091573-1773867395?organization=assurantauto) | 05-27 | 13 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4.69 (94) | ✓ PASS | — |
| [CONV 17](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1505575918-1498616305-2827076085-1773867395?organization=assurantauto) | 05-27 | 12 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 4.17 (83) | ✓ PASS | — |
| [CONV 18](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2441921249-1493897713-2628436469-1773867395?organization=assurantauto) | 05-27 | 30 | 2 | 4 | 3 | 4 | 4 | 2 | 3 | 4 | 2 | 2 | 2.90 (58) | ✗ FAIL | — |
| [CONV 19](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2477382014-1499009521-2165344576-3594676577?organization=assurantauto) | 05-27 | 37 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 5 | 3.98 (80) | ✓ PASS | — |
| [CONV 20](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2747700678-1493635569-2538441024-3594676577?organization=assurantauto) | 05-27 | 8 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4.36 (87) | ✓ PASS | — |
| [CONV 21](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2984888678-1493832177-2522712384-3594676577?organization=assurantauto) | 05-27 | 11 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (86) | ✓ PASS | — |
| [CONV 22](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3153780624-1499206129-3035728192-3594676577?organization=assurantauto) | 05-27 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3.78 (76) | ✓ PASS | — |
| [CONV 23](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3157909537-1498943985-2424816117-1773867395?organization=assurantauto) | 05-27 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 4.06 (81) | ✓ PASS | — |
| [CONV 24](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3282198693-1493832177-2352792053-1773867395?organization=assurantauto) | 05-27 | 6 | 1 | 2 | 3 | 4 | 4 | 1 | 2 | 3 | 4 | 3 | 2.49 (50) | ✗ FAIL | ABANDONED |
| [CONV 25](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3869080789-1498485233-2320482805-1773867395?organization=assurantauto) | 05-27 | 19 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 3 | 5 | 4.11 (82) | ✓ PASS | — |
| [CONV 26](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/4022760384-1493635569-2456076789-1773867395?organization=assurantauto) | 05-27 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 27](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0153633380-1508970993-2698887669-1773867395?organization=assurantauto) | 05-28 | 88 | 2 | 3 | 2 | 4 | 4 | 2 | 3 | 3 | 2 | 4 | 2.84 (57) | ✗ FAIL | — |
| [CONV 28](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1434550166-1507922417-3119810880-3594676577?organization=assurantauto) | 05-28 | 16 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.39 (88) | ✓ PASS | — |
| [CONV 29](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2101077654-1508839921-3208415552-3594676577?organization=assurantauto) | 05-28 | 5 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.64 (73) | ✓ PASS | — |
| [CONV 30](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2113769453-1514213873-2775877952-3594676577?organization=assurantauto) | 05-28 | 18 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.28 (86) | ✓ PASS | — |
| [CONV 31](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2428792897-1507267057-2174337525-1773867395?organization=assurantauto) | 05-28 | 10 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.52 (90) | ✓ PASS | — |
| [CONV 32](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2556193367-1508970993-2948776437-1773867395?organization=assurantauto) | 05-28 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.17 (83) | ✓ PASS | — |
| [CONV 33](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2741558122-1508119025-2410660341-1773867395?organization=assurantauto) | 05-28 | 17 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.63 (93) | ✓ PASS | — |
| [CONV 34](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2994322615-1507987953-2684586304-3594676577?organization=assurantauto) | 05-28 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 3 | 5 | 4.30 (86) | ✓ PASS | — |
| [CONV 35](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3285831192-1509167601-2280702453-1773867395?organization=assurantauto) | 05-28 | 13 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.33 (87) | ✓ PASS | — |
| [CONV 36](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3670024120-1514082801-2318778869-1773867395?organization=assurantauto) | 05-28 | 16 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3.61 (72) | ✓ PASS | — |
| [CONV 37](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3848709587-1506939377-2588117312-3594676577?organization=assurantauto) | 05-28 | 16 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.56 (91) | ✓ PASS | — |
| [CONV 38](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0043704503-1520636401-3016460608-3594676577?organization=assurantauto) | 05-29 | 15 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4.09 (82) | ✓ PASS | — |
| [CONV 39](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0777565587-1520177649-2741274944-3594676577?organization=assurantauto) | 05-29 | 8 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.74 (95) | ✓ PASS | — |
| [CONV 40](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0845108947-1523651057-2803204586-2917985560?organization=assurantauto) | 05-29 | 15 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 4.26 (85) | ✓ PASS | — |
| [CONV 41](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0905991152-1519587825-2198833472-3594676577?organization=assurantauto) | 05-29 | 10 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.28 (86) | ✓ PASS | — |
| [CONV 42](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1478781705-1523716593-2362676280-0825805307?organization=assurantauto) | 05-29 | 25 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4.28 (86) | ✓ PASS | — |
| [CONV 43](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1676530228-1520046577-2179565888-3594676577?organization=assurantauto) | 05-29 | 7 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4.74 (95) | ✓ PASS | — |
| [CONV 44](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2047781068-1519587825-2258012480-3594676577?organization=assurantauto) | 05-29 | 35 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.48 (70) | ✗ FAIL | — |
| [CONV 45](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2587095257-1521619441-2864955893-1773867395?organization=assurantauto) | 05-29 | 10 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4.22 (84) | ✓ PASS | — |
| [CONV 46](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2897319300-1522209265-2959447096-0825805307?organization=assurantauto) | 05-29 | 35 | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 3.53 (71) | ✓ PASS | — |
| [CONV 47](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3202280767-1523454449-2491597301-1773867395?organization=assurantauto) | 05-29 | 17 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 3.87 (77) | ✓ PASS | — |
| [CONV 48](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3313752376-1521553905-2500510197-1773867395?organization=assurantauto) | 05-29 | 15 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4.33 (87) | ✓ PASS | — |
| [CONV 49](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3795369864-1520767473-3010904565-1773867395?organization=assurantauto) | 05-29 | 16 | 3 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3.70 (74) | ✓ PASS | — |
| [CONV 50](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3905540289-1520046577-2425799157-1773867395?organization=assurantauto) | 05-29 | 16 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3.53 (71) | ✓ PASS | — |

---

## Section 5: Flagged Conversations

*Criteria: any flag, score < 2.5, D1 ≤ 2, or D12 ≤ 2 — 4 of 50.*

| Date | D1 | D12 | Score | Flags | Conv ID | Notes |
|------|----|----|-------|-------|---------|-------|
| 05-27 | 1 | 3 | 2.49 | ABANDONED | [`3282198693-1493832177-23...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3282198693-1493832177-2352792053-1773867395?organization=assurantauto) | Caller (repair facility) had a clear need — provide their shop name so a previously-submitted claim could be located. Bot completely failed to engage with the request, offered a generic apology, and l |
| 05-28 | 2 | 4 | 2.84 | — | [`0153633380-1508970993-26...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/0153633380-1508970993-2698887669-1773867395?organization=assurantauto) | The call was extremely painful with heavy looping in the dealer triage funnel — the bot repeatedly re-asked 'have you submitted online?' and 'contract or VIN?' multiple times despite the caller answer |
| 05-27 | 2 | 2 | 2.90 | — | [`2441921249-1493897713-26...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/2441921249-1493897713-2628436469-1773867395?organization=assurantauto) | Repair facility caller struggled to provide VIN; ASR clearly misrecognized spoken alphanumeric input multiple times (D10). Bot failed to adapt — kept re-asking for VIN length rather than offering lett |
| 05-26 | 3 | 4 | 3.46 | ABANDONED | [`3940792155-1483739633-21...`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3940792155-1483739633-2173616629-1773867395?organization=assurantauto) | Caller provided a claim number (GU2422275) but the bot misinterpreted it as a VIN and looked it up as such, failing to recognize the user's correction. D6 suffers because the bot's clarification ('rep |

---

## Section 6: Representative Examples

### Highest scorer: 4.80/5 (96/100)
**Conv ID:** [`1138490278-1470370289-2397749749-1773867395`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/1138490278-1470370289-2397749749-1773867395?organization=assurantauto)  
**Date:** 2026-05-25  |  **Tasks:** CallerIdentification, CallerIdentification, DealershipIssues  |  **D1:** 5  |  **D12:** 5
**Flags:** —  
**Notes:** Clean dealer claim status flow: correct two-step funneling, identifier collected, claim looked up, status delivered concisely. No observable defects.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! Let's get you to the right place... are you a customer, a dealer, or a repair facility?
  Customer: dealer
  Talker: One moment while I check on that.
  Talker: What do you need help with today, such as an existing claim, filing a new claim, a contract issue, or something else?
  Customer: Status on claim.
  Talker: Got it, may I have the claim number, contract number, or the last eight characters of the vehicle’s Vin?
  Customer: Four nine six three three four four six
  Talker: Let me check on that.
  Talker: One moment please.
  Talker: This claim is currently under review and will be adjudicated in the order it was received, does that answer your question or do you need help with anything else?
```

### Most notable failure: 2.49/5 (50/100)
**Conv ID:** [`3282198693-1493832177-2352792053-1773867395`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3282198693-1493832177-2352792053-1773867395?organization=assurantauto)  
**Date:** 2026-05-27  |  **Tasks:** CallerIdentification, CallerIdentification, RepairShopIssues  |  **D1:** 1  |  **D12:** 3
**Flags:** ABANDONED  
**Notes:** Caller (repair facility) had a clear need — provide their shop name so a previously-submitted claim could be located. Bot completely failed to engage with the request, offered a generic apology, and let the caller disengage without attempting the designed repair-shop flow or escalating to a human. Critical D1/D6 failure; caller abandoned without resolution.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! Let's get you to the right place... are you a customer, a dealer, or a repair facility?
  Customer: A repaired facility.
  Talker: What can I help you with today?
  Customer: So when I sent y'all the the claim, y'all couldn't find my shop. So I'm here to tell you my shop name.
  Talker: I apologize that we were not able to resolve the shop identification issue for your claim. . Is there anything else I can help you with today?
  Customer: That'll be all.
```

### Lowest scorer: 2.49/5 (50/100)
**Conv ID:** [`3282198693-1493832177-2352792053-1773867395`](https://ai-console.asapp.com/company/assurantauto/generative-agent/main/conversations/externalConversationIds/3282198693-1493832177-2352792053-1773867395?organization=assurantauto)  
**Date:** 2026-05-27  |  **Tasks:** CallerIdentification, CallerIdentification, RepairShopIssues  |  **D1:** 1  |  **D12:** 3
**Flags:** ABANDONED  
**Notes:** Caller (repair facility) had a clear need — provide their shop name so a previously-submitted claim could be located. Bot completely failed to engage with the request, offered a generic apology, and let the caller disengage without attempting the designed repair-shop flow or escalating to a human. Critical D1/D6 failure; caller abandoned without resolution.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! Let's get you to the right place... are you a customer, a dealer, or a repair facility?
  Customer: A repaired facility.
  Talker: What can I help you with today?
  Customer: So when I sent y'all the the claim, y'all couldn't find my shop. So I'm here to tell you my shop name.
  Talker: I apologize that we were not able to resolve the shop identification issue for your claim. . Is there anything else I can help you with today?
  Customer: That'll be all.
```

---

## Section 7: Systemic Issues (Week)

- **ASR mishearing** — flagged in 8 of 50 calls (16%) in notes.
- **Repeated questions / poor context retention** — flagged in 2 of 50 calls (4%) in notes.
- **Generic response did not address specific need** — flagged in 14 of 50 calls (28%) in notes.
- **Excessive filler / verbosity** — flagged in 4 of 50 calls (8%) in notes.

---

## Comparison vs. Re-scored Baseline (Apr 18 onward)

| Metric | This Week | Baseline | Δ |
|---|---|---|---|
| Pass rate | 90.0% | 71.7% | **+18.3 pp** |
| Mean score (/5) | 4.06 | 3.83 | **+0.23** |
| Scored conversations | 50 | 304 | — |

- **Pass rate improved by 18.3 pp** vs. baseline.
- **Mean score improved by 0.23** points.