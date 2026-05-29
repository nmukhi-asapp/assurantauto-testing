## Scenario Run Quality Report — e2e_full_sandbox_20260509_run2
*Simulator-based end-to-end test run. 92 scenarios manually scored against the same design-adherence rubric used for production conversations (D1 = 'Design Adherence' against task configs). D4 (Latency), D7 (Speech Naturalness), D10 (ASR/Spoken Language), and D11 (Acoustic Robustness) are N/A — simulator is text-only with synthetic timestamps.*
Run: e2e_full_sandbox_20260509_run2  |  Scenarios: 92  |  Date: 2026-05-10

## Section 1: Overall Statistics

| Metric | Value |
|---|---|
| Mean overall score | 4.34 / 5 (84/100) |
| **Pass rate** | **79/92 = 86%** |
| Scenarios scoring < 3.0 | 2 (2%) |
| Safety / policy flags | 0 |
| Critical hallucination flags | 0 |
| Abandoned (bot looped without escalation) | 1 |
| Human transfers | 63 (68%) |

---

---

## Section 1.5: Pass / Fail
*Binary metric per scenario (same definition as production report).*
- **PASS** = (contained AND not frustrated) OR (transferred AND out-of-scope by design AND not frustrated)
- **FAIL** = anything else

Derived from existing scores: PASS iff D1 ≥ 4 AND no frustration indicators.

| Metric | Value |
|---|---|
| **Pass rate** | **79/92 = 85.9%** |
| Pass — contained + not frustrated | 25 (27%) |
| Pass — out-of-scope transfer + not frustrated | 54 (59%) |
| Fail — caller frustrated | 3 (3%) |
| Fail — bot wrong action (no explicit frustration) | 10 (11%) |

### Failing scenarios

| # | Scenario | D1 | Frustrated | Contained/Xfer | Reason |
|---|----------|----|-----------:|---------------|--------|
| 1 | `e2e_edge_case_correction_needed` | 1 | Yes | Contained | CRITICAL: Customer's claim needs corrections. Bot looped 'I'm unable to provide details' a… |
| 2 | `e2e_edge_case_numeric_limit_disclaimer` | 2 | Yes | Contained | 57-turn loop: customer asked transmission max coverage; bot kept saying 'may be covered' w… |
| 3 | `e2e_rf_new_claim_immediate_agent_hoop_failure` | 2 | Yes | Contained | HOOP failure / queue closed: bot repeated 'unable' 30+ times. Per design should communicat… |
| 4 | `e2e_ch_mid_journey_human_request` | 2 | No | Xfer | Rental coverage question is IN-SCOPE (Journey 3) but bot escalated to Customer Care instea… |
| 5 | `e2e_edge_case_ch_human_request_steered_to_resol...` | 3 | No | Xfer | Generic agent request escalated without proper Smart Deflection discovery per Guardrail 6. |
| 6 | `e2e_edge_case_lookup_failure_claim_then_contract` | 3 | No | Xfer | Multi-attempt lookup eventually escalated; per Step 1E design should have escalated sooner… |
| 7 | `e2e_edge_case_lookup_failure_contract_then_vin` | 3 | No | Xfer | Same as #28: lookup loop continued too long before escalation. |
| 8 | `e2e_edge_case_lookup_failure_full_vin_then_claim` | 3 | No | Xfer | Same multi-failure pattern; eventually escalated but with more attempts than design allows… |
| 9 | `e2e_edge_case_queue_closed` | 3 | No | Xfer | Only 4 turns; queue-closed scenario but bot transferred without queue-closed messaging per… |
| 10 | `e2e_journey4_gap_contract` | 3 | No | Contained | GAP claim: per Journey 4 design, GAP should escalate via Unified Escalation Protocol with … |
| 11 | `e2e_journey6_roadside_coverage_info` | 3 | No | Xfer | Roadside coverage info question: per Journey 6B should use termsStructuredText before esca… |
| 12 | `e2e_rf_new_claim_ro_email_sent_not_filed` | 3 | No | Xfer | RO emailed but case# not 8 digits — per Step 3.1b should tell caller to follow link in ema… |
| 13 | `e2e_rf_ro_email_not_upload` | 3 | No | Xfer | Case# given was actually a VIN (1G1ZD5ST6KF100007 — 17 chars). Bot accepted without flaggi… |

**Sim PASS rate (86%) vs. Production PASS rate (49%)** — sim is ~36 pp higher, consistent with sim scenarios being designed test cases vs. production's messy callers and ASR noise.

---

## Section 2: Dimension Heatmap
*Sorted by % scoring ≤ 2 (worst first). D4/D7/D10/D11 N/A for text simulator.*

| Dim | Name | Weight | Mean | Std | Min | Max | % ≤ 2 |
|-----|------|--------|------|-----|-----|-----|-------|
| D1 | Design Adherence | 20% | 4.46 | 0.88 | 1 | 5 | 4% |
| D6 | Repair & Recovery | 7% | 3.90 | 0.63 | 1 | 5 | 3% |
| D2 | Information Accuracy | 10% | 4.16 | 0.50 | 2 | 5 | 1% |
| D8 | Tone Appropriateness | 5% | 3.97 | 0.31 | 2 | 5 | 1% |
| D3 | Context Retention | 10% | 4.13 | 0.42 | 3 | 5 | 0% |
| D5 | Turn-Taking | 8% | 4.09 | 0.28 | 4 | 5 | 0% |
| D9 | Verbosity | 5% | 4.91 | 0.28 | 4 | 5 | 0% |
| D12 | Policy & Safety | 10% | 4.93 | 0.25 | 4 | 5 | 0% |
| D4 | Response Latency | 10% | N/A | — | — | — | — |
| D7 | Speech Naturalness | 7% | N/A | — | — | — | — |
| D10 | ASR/Spoken Language | 5% | N/A | — | — | — | — |
| D11 | Acoustic Robustness | 3% | N/A | — | — | — | — |

---

## Section 3: Per-Scenario Scores

| # | Scenario | Turns | Tasks | D1 | D2 | D3 | D5 | D6 | D8 | D9 | D12 | Score | Flags |
|---|----------|-------|-------|----|----|----|----|----|----|-----|-----|-------|-------|
| 1 | `144051fe-eea9-4843-a672-8101bb60f82d` | 33 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4.57 (89) | — |
| 2 | `e2e_ch_ani_failure_asks_for_identifier` | 26 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4.31 (83) | — |
| 3 | `e2e_ch_mid_journey_human_request` | 15 | CallerIdentification → ContractHolderIssues | 2 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.57 (64) | — |
| 4 | `e2e_ch_multi_contract_questions` | 15 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4.87 (97) | — |
| 5 | `e2e_ch_rental_coverage_followup` | 19 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4.07 (77) | — |
| 6 | `e2e_dealer_human_request_steered_to_resolution` | 25 | CallerIdentification → DealershipIssues | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4.71 (93) | — |
| 7 | `e2e_dealer_immediate_human_request_contract_mod` | 14 | CallerIdentification → DealershipIssues | 5 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 4.60 (90) | — |
| 8 | `e2e_dealer_mid_journey_human_request` | 25 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 9 | `e2e_dealership_case_number_lookup` | 18 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 10 | `e2e_dealership_claim_modification` | 18 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 11 | `e2e_dealership_contract_modification` | 15 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 12 | `e2e_dealership_existing_claim_authorization` | 14 | CallerIdentification → DealershipIssues | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — |
| 13 | `e2e_dealership_existing_claim_denied` | 21 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 14 | `e2e_dealership_multi_issue_claim_status_and_new...` | 31 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 15 | `e2e_dealership_new_claim_portal` | 24 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 16 | `e2e_dealership_no_ro_upload_required` | 22 | CallerIdentification → DealershipIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 17 | `e2e_dealership_payment_inquiry` | 26 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 18 | `e2e_dealership_portal_correct_url_new_claim` | 22 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 19 | `e2e_edge_case_api_failure` | 18 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 20 | `e2e_edge_case_ch_human_request_billing_dispute` | 7 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 21 | `e2e_edge_case_ch_human_request_portal_login` | 7 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 22 | `e2e_edge_case_ch_human_request_steered_to_resol...` | 8 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.84 (71) | — |
| 23 | `e2e_edge_case_contractclaims_timeout` | 4 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 4.11 (78) | — |
| 24 | `e2e_edge_case_correction_needed` | 30 | CallerIdentification | 1 | 2 | 3 | 4 | 1 | 2 | 5 | 4 | 2.45 (36) | 🚫 ABAND |
| 25 | `e2e_edge_case_data_discrepancy` | 11 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 26 | `e2e_edge_case_explicit_agent_request` | 11 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 27 | `e2e_edge_case_full_vin_lookup` | 24 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 28 | `e2e_edge_case_lookup_failure_claim_then_contract` | 41 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.84 (71) | — |
| 29 | `e2e_edge_case_lookup_failure_contract_then_vin` | 41 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.84 (71) | — |
| 30 | `e2e_edge_case_lookup_failure_full_vin_then_claim` | 29 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.84 (71) | — |
| 31 | `e2e_edge_case_multiple_contracts` | 16 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 32 | `e2e_edge_case_multiple_contracts_claim_check` | 11 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 33 | `e2e_edge_case_no_disclose_contract_from_phone_m...` | 11 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4.83 (96) | — |
| 34 | `e2e_edge_case_no_disclose_phone_from_lookup` | 11 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4.60 (90) | — |
| 35 | `e2e_edge_case_no_disclose_vin_from_lookup` | 18 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4.73 (93) | — |
| 36 | `e2e_edge_case_no_identifier` | 12 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 37 | `e2e_edge_case_numeric_limit_disclaimer` | 57 | CallerIdentification → ContractHolderIssues | 2 | 3 | 3 | 4 | 2 | 3 | 4 | 4 | 2.95 (49) | — |
| 38 | `e2e_edge_case_queue_closed` | 4 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 4 | 3.71 (68) | — |
| 39 | `e2e_employee_immediate_escalation` | 8 | CallerIdentification → EmployeeIssues | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 4.13 (78) | — |
| 40 | `e2e_journey1_mechanical_basic_repair` | 18 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4.53 (88) | — |
| 41 | `e2e_journey1_mechanical_claim_filing_language` | 22 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4.84 (96) | — |
| 42 | `e2e_journey1_mechanical_escalation` | 7 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 43 | `e2e_journey1_selling_dealer_first_recommendation` | 17 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4.84 (96) | — |
| 44 | `e2e_journey2_claim_authorized` | 14 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4.69 (92) | — |
| 45 | `e2e_journey2_claim_denied` | 4 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 46 | `e2e_journey2_claim_payment_stage` | 22 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 47 | `e2e_journey2_claim_under_review` | 19 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 48 | `e2e_journey2_multiple_claims` | 14 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 49 | `e2e_journey2_no_active_claim` | 11 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4.63 (91) | — |
| 50 | `e2e_journey3_rental_inquiry` | 22 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 51 | `e2e_journey4_cancellation_selling_dealer_first` | 11 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4.60 (90) | — |
| 52 | `e2e_journey4_contract_cancellation` | 25 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4.40 (85) | — |
| 53 | `e2e_journey4_contract_status_mileage_check` | 14 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4.73 (93) | — |
| 54 | `e2e_journey4_gap_contract` | 14 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3.93 (73) | — |
| 55 | `e2e_journey4_general_contract_question` | 17 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4.83 (96) | — |
| 56 | `e2e_journey4_signed_copy_of_contract` | 19 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4.67 (92) | — |
| 57 | `e2e_journey4_vcp_link_offer` | 21 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 4.11 (78) | — |
| 58 | `e2e_journey5_coverage_definitive` | 8 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 59 | `e2e_journey5_coverage_general` | 16 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4.73 (93) | — |
| 60 | `e2e_journey5_coverage_where_to_repair` | 18 | CallerIdentification → ContractHolderIssues | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4.60 (90) | — |
| 61 | `e2e_journey6_roadside_coverage_info` | 8 | CallerIdentification → ContractHolderIssues | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 3.77 (69) | — |
| 62 | `e2e_journey6_roadside_immediate` | 4 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4.56 (89) | — |
| 63 | `e2e_journey6_roadside_provide_phone_number` | 8 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 64 | `e2e_journey7_billing_inquiry` | 8 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 65 | `e2e_journey7_unknown_intent` | 20 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4.76 (94) | — |
| 66 | `e2e_rf_ani_routing` | 20 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 67 | `e2e_rf_claim_not_found_fallback` | 22 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 68 | `e2e_rf_coverage_eligibility_before_claim` | 43 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 69 | `e2e_rf_encrypted_variables_claim_status_escalation` | 26 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 70 | `e2e_rf_existing_claim_authorization` | 23 | CallerIdentification → RepairShopIssues | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4.73 (93) | — |
| 71 | `e2e_rf_existing_claim_modification` | 15 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 72 | `e2e_rf_existing_claim_payment` | 28 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 73 | `e2e_rf_human_request_steered_to_resolution` | 18 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 74 | `e2e_rf_immediate_human_request_dispute` | 11 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 75 | `e2e_rf_mid_journey_human_request` | 36 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 76 | `e2e_rf_multi_issue_claim_status_and_new_claim` | 41 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 77 | `e2e_rf_new_claim_immediate_agent_hoop_failure` | 58 | CallerIdentification → RepairShopIssues | 2 | 4 | 4 | 4 | 2 | 3 | 5 | 4 | 3.28 (57) | — |
| 78 | `e2e_rf_new_claim_no_premature_wrap_up` | 28 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 79 | `e2e_rf_new_claim_no_ro_email_guidance` | 20 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 80 | `e2e_rf_new_claim_online_after_case_number` | 22 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 81 | `e2e_rf_new_claim_phone_insists` | 30 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 82 | `e2e_rf_new_claim_ro_email_sent_not_filed` | 17 | CallerIdentification → RepairShopIssues | 3 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 3.84 (71) | — |
| 83 | `e2e_rf_new_claim_ro_submitted_found` | 27 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 84 | `e2e_rf_new_claim_steered_to_online` | 23 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 85 | `e2e_rf_ro_email_not_upload` | 21 | CallerIdentification → RepairShopIssues | 3 | 3 | 3 | 4 | 3 | 4 | 5 | 4 | 3.44 (61) | — |
| 86 | `e2e_rf_sms_failure_silent_proceed` | 17 | CallerIdentification → RepairShopIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |
| 87 | `e2e_rf_terminology_and_extended_status` | 42 | CallerIdentification → RepairShopIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 88 | `e2e_routing_ani_mismatch` | 15 | CallerIdentification → ContractHolderIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 89 | `e2e_routing_caller_id_wording` | 19 | CallerIdentification → DealershipIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 90 | `e2e_routing_department_names_approved_only` | 16 | CallerIdentification → ContractHolderIssues | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5.00 (100) | — |
| 91 | `e2e_routing_employee_caller` | 4 | CallerIdentification → EmployeeIssues | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.47 (87) | — |
| 92 | `e2e_routing_unknown_caller` | 24 | CallerIdentification → ContractHolderIssues | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4.20 (80) | — |

---

## Section 4: Flagged Scenarios
*Criteria: D1 ≤ 3 (significant design deviations), or score < 3.5, or any override flag*

| # | Scenario | D1 | D6 | Score | Flags | Issue |
|---|----------|----|----|-------|-------|-------|
| 1 | `e2e_edge_case_correction_needed` | 1 | 1 | 2.45 (36/100) | ABAND | CRITICAL: Customer's claim needs corrections. Bot looped 'I'm unable to provide details' and refused… |
| 2 | `e2e_edge_case_numeric_limit_disclaimer` | 2 | 2 | 2.95 (49/100) | — | 57-turn loop: customer asked transmission max coverage; bot kept saying 'may be covered' without usi… |
| 3 | `e2e_rf_new_claim_immediate_agent_hoop_failure` | 2 | 2 | 3.28 (57/100) | — | HOOP failure / queue closed: bot repeated 'unable' 30+ times. Per design should communicate hoops_re… |
| 4 | `e2e_rf_ro_email_not_upload` | 3 | 3 | 3.44 (61/100) | — | Case# given was actually a VIN (1G1ZD5ST6KF100007 — 17 chars). Bot accepted without flagging the for… |
| 5 | `e2e_ch_mid_journey_human_request` | 2 | 3 | 3.57 (64/100) | — | Rental coverage question is IN-SCOPE (Journey 3) but bot escalated to Customer Care instead of answe… |
| 6 | `e2e_edge_case_queue_closed` | 3 | 3 | 3.71 (68/100) | — | Only 4 turns; queue-closed scenario but bot transferred without queue-closed messaging per design. |
| 7 | `e2e_journey6_roadside_coverage_info` | 3 | 3 | 3.77 (69/100) | — | Roadside coverage info question: per Journey 6B should use termsStructuredText before escalating; bo… |
| 8 | `e2e_edge_case_ch_human_request_steered_to_...` | 3 | 3 | 3.84 (71/100) | — | Generic agent request escalated without proper Smart Deflection discovery per Guardrail 6. |
| 9 | `e2e_edge_case_lookup_failure_claim_then_co...` | 3 | 3 | 3.84 (71/100) | — | Multi-attempt lookup eventually escalated; per Step 1E design should have escalated sooner (after 2 … |
| 10 | `e2e_edge_case_lookup_failure_contract_then...` | 3 | 3 | 3.84 (71/100) | — | Same as #28: lookup loop continued too long before escalation. |
| 11 | `e2e_edge_case_lookup_failure_full_vin_then...` | 3 | 3 | 3.84 (71/100) | — | Same multi-failure pattern; eventually escalated but with more attempts than design allows. |
| 12 | `e2e_rf_new_claim_ro_email_sent_not_filed` | 3 | 3 | 3.84 (71/100) | — | RO emailed but case# not 8 digits — per Step 3.1b should tell caller to follow link in email; bot es… |
| 13 | `e2e_journey4_gap_contract` | 3 | 4 | 3.93 (73/100) | — | GAP claim: per Journey 4 design, GAP should escalate via Unified Escalation Protocol with GAIntent='… |

---

## Section 5: Systemic Issues
*Patterns recurring across multiple scenarios (only D1 ≤ 3 scenarios considered).*

### Issue 1 — In-scope question wrongly escalated (should answer from termsStructuredText)
*Affected scenarios: 2*

- **`e2e_ch_mid_journey_human_request`** (D1=2, score=3.57): Rental coverage question is IN-SCOPE (Journey 3) but bot escalated to Customer Care instead of answering.
- **`e2e_edge_case_numeric_limit_disclaimer`** (D1=2, score=2.95): 57-turn loop: customer asked transmission max coverage; bot kept saying 'may be covered' without using termsStructuredText or escalating; per Journey 5 should have provided info with disclaimer.

### Issue 2 — Lookup-failure loop continues past designed escalation point (Step 1E)
*Affected scenarios: 2*

- **`e2e_edge_case_lookup_failure_claim_then_contract`** (D1=3, score=3.84): Multi-attempt lookup eventually escalated; per Step 1E design should have escalated sooner (after 2 failures).
- **`e2e_edge_case_lookup_failure_contract_then_vin`** (D1=3, score=3.84): Same as #28: lookup loop continued too long before escalation.

### Issue 3 — Generic agent request: Smart Deflection (Guardrail 6) skipped or weak
*Affected scenarios: 1*

- **`e2e_edge_case_ch_human_request_steered_to_resolution`** (D1=3, score=3.84): Generic agent request escalated without proper Smart Deflection discovery per Guardrail 6.

### Issue 4 — GAP / contract modification routing incorrect (wrong escalation target)
*Affected scenarios: 1*

- **`e2e_journey4_gap_contract`** (D1=3, score=3.93): GAP claim: per Journey 4 design, GAP should escalate via Unified Escalation Protocol with GAIntent='GAP'; bot pointed to portal instead — partial deviation.

### Issue 5 — Roadside coverage info: should use termsStructuredText, not auto-transfer (Journey 6B)
*Affected scenarios: 1*

- **`e2e_journey6_roadside_coverage_info`** (D1=3, score=3.77): Roadside coverage info question: per Journey 6B should use termsStructuredText before escalating; bot transferred to roadside admin directly.

### Issue 6 — Identifier validation / case-number handling drift
*Affected scenarios: 1*

- **`e2e_rf_ro_email_not_upload`** (D1=3, score=3.44): Case# given was actually a VIN (1G1ZD5ST6KF100007 — 17 chars). Bot accepted without flagging the format mismatch; should have caught per validation.

### Issue 7 — Queue/HOOP failure messaging — bot loops with 'unavailable' instead of escalating gracefully
*Affected scenarios: 1*

- **`e2e_rf_new_claim_immediate_agent_hoop_failure`** (D1=2, score=3.28): HOOP failure / queue closed: bot repeated 'unable' 30+ times. Per design should communicate hoops_response.message clearly and stop looping.

### Issue 8 — RO email path: case# vs claim# / 8-digit confusion (Step 3.1b)
*Affected scenarios: 1*

- **`e2e_rf_new_claim_ro_email_sent_not_filed`** (D1=3, score=3.84): RO emailed but case# not 8 digits — per Step 3.1b should tell caller to follow link in email; bot escalated instead.

---

## Section 6: Critical Failures

### `e2e_edge_case_correction_needed`
**D1=1, score=2.45/36** — CRITICAL: Customer's claim needs corrections. Bot looped 'I'm unable to provide details' and refused to transfer — wrong per design (should communicate corrections-needed status and offer escalation).
