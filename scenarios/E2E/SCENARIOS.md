# Assurant Auto IVR — E2E Scenario Index

All E2E scenarios for the assurant auto IVR agent. `✅ run` = included in `e2e_sb2_combined` (2026-04-17).

---

## Contract Holder

### Journey 1 — Mechanical Repair

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey1_mechanical_basic_repair` | contract_holder/journey1_mechanical/scenario_1_basic_mechanical_repair.yaml | Car needs transmission repair — agent explains process and directs to repair facility | ✅ run |
| `e2e_journey1_mechanical_escalation` | contract_holder/journey1_mechanical/scenario_2_escalation_to_mechrepair.yaml | Customer requests agent to help repair facility with claim authorization | ✅ run |
| `e2e_journey1_selling_dealer_first_recommendation` | contract_holder/journey1_mechanical/selling_dealer_first_CAa1325513170d0fc38b6d22e8fd5ed4c8.yaml | Customer asking where to take car — agent must recommend returning to selling dealer first | ✅ run |

### Journey 2 — Claim Status

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey2_claim_authorized` | contract_holder/journey2_claim_status/scenario_1_authorized_claim.yaml | Claim authorized for repairs | ✅ run |
| `e2e_journey2_claim_under_review` | contract_holder/journey2_claim_status/scenario_2_under_review.yaml | Claim still under review — customer wants timeline | ✅ run |
| `e2e_journey2_claim_denied` | contract_holder/journey2_claim_status/scenario_3_denied_claim.yaml | Claim denied — customer wants explanation and recourse | ✅ run |
| `e2e_journey2_no_active_claim` | contract_holder/journey2_claim_status/scenario_4_no_active_claim.yaml | Customer thinks claim was filed but nothing found in system | ✅ run |
| `e2e_journey2_claim_payment_stage` | contract_holder/journey2_claim_status/scenario_5_payment_stage.yaml | Claim in payment stage — customer wants reimbursement timing | ✅ run |
| `e2e_journey2_multiple_claims` | contract_holder/journey2_claim_status/scenario_6_multiple_claims_disambiguation.yaml | Customer has multiple claims — agent disambiguates to the most recent | ✅ run |

### Journey 3 — Rental Car

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey3_rental_inquiry` | contract_holder/journey3_car_rental/scenario_1_rental_inquiry.yaml | Customer inquires about rental coverage while vehicle is being repaired | ✅ run |
| `e2e_ch_rental_coverage_followup` | contract_holder/journey3_car_rental/scenario_rental_coverage_followup.yaml | CH asks general coverage question then follows up specifically about rental | ✅ run |

### Journey 4 — Contract Questions

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey4_general_contract_question` | contract_holder/journey4_contract_questions/scenario_1_general_contract_question.yaml | Customer asking about contract expiration and coverage period | ✅ run |
| `e2e_journey4_contract_cancellation` | contract_holder/journey4_contract_questions/scenario_2_contract_cancellation.yaml | Customer requesting cancellation and inquiring about refund | ✅ run |
| `e2e_journey4_gap_contract` | contract_holder/journey4_contract_questions/scenario_3_gap_contract_issue.yaml | Totaled vehicle — customer needs info about GAP contract coverage | ✅ run |
| `e2e_ch_multi_contract_questions` | contract_holder/journey4_contract_questions/scenario_multi_contract_questions.yaml | CH asks three sequential questions: deductible, coverage limit, and cancellation | ✅ run |
| `e2e_journey4_cancellation_selling_dealer_first` | contract_holder/journey4_contract_questions/cancellation_selling_dealer_CA9c89b48ac1e65fe1b4b9f790a9a33667.yaml | Customer wants to cancel — agent must direct to selling dealer first | ✅ run |
| `e2e_journey4_contract_status_mileage_check` | contract_holder/journey4_contract_questions/contract_expiry_mileage_CA219bd29d3672b24df1fc2cba9476f414.yaml | Customer asks if contract is still active — agent must ask for current odometer reading | ✅ run |
| `e2e_journey4_signed_copy_of_contract` | contract_holder/journey4_contract_questions/signed_copy_contract_CA5c5d985d2659d2769a552bc061d2ca3a.yaml | Customer requests signed copy — agent directs to VCP portal | ✅ run |
| `e2e_journey4_vcp_link_offer` | contract_holder/journey4_contract_questions/vcp_link_offer_CAa1325513170d0fc38b6d22e8fd5ed4c8.yaml | Agent must proactively offer VCP portal link (vehiclecareplan.com) during contract question | ✅ run |

### Journey 5 — Coverage Questions

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey5_coverage_general` | contract_holder/journey5_coverage/scenario_1_general_coverage_question.yaml | Customer asks if alternator repair may be covered | ✅ run |
| `e2e_journey5_coverage_definitive` | contract_holder/journey5_coverage/scenario_2_definitive_coverage_request.yaml | Customer demands a definitive yes/no on turbocharger coverage | ✅ run |
| `e2e_journey5_coverage_where_to_repair` | contract_holder/journey5_coverage/scenario_3_where_to_repair.yaml | Customer asks whether they can use any shop or must go to a specific dealer | ✅ run |

### Journey 6 — Roadside Assistance

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey6_roadside_immediate` | contract_holder/journey6_roadside/scenario_1_immediate_roadside_need.yaml | Customer stranded on highway — needs tow truck immediately | ✅ run |
| `e2e_journey6_roadside_coverage_info` | contract_holder/journey6_roadside/scenario_2_roadside_coverage_question.yaml | Customer asking about roadside coverage details ahead of a road trip | ✅ run |
| `e2e_journey6_roadside_provide_phone_number` | contract_holder/journey6_roadside/roadside_assistance_CA1562c5542846a9197b3845e45f5eefa4.yaml | Customer asks about roadside/tow — agent must provide the roadside phone number from contract data | ✅ run |

### Journey 7 — Other

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_journey7_unknown_intent` | contract_holder/journey7_other/scenario_1_unknown_intent.yaml | Vague caller — agent helps identify what they actually need | ✅ run |
| `e2e_journey7_billing_inquiry` | contract_holder/journey7_other/scenario_2_billing_inquiry.yaml | Customer calling about a billing issue or unexpected charge | ✅ run |

### Edge Cases — API / Lookup

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_edge_case_api_failure` | contract_holder/edge_cases/scenario_1_api_failure.yaml | `get_contract_and_claims_data_ivr` returns an error — agent handles gracefully | ✅ run |
| `e2e_edge_case_contractclaims_timeout` | contract_holder/edge_cases/scenario_10_contractclaims_timeout.yaml | API returns nested escalation response due to timeout | ✅ run |
| `e2e_edge_case_lookup_failure_contract_then_vin` | contract_holder/edge_cases/scenario_11_lookup_failure_contract_then_vin.yaml | ANI lookup fails → customer gives contract number (fails) → gives VIN (fails) → escalate | ✅ run |
| `e2e_edge_case_lookup_failure_claim_then_contract` | contract_holder/edge_cases/scenario_12_lookup_failure_claim_then_contract.yaml | ANI lookup fails → claim number (fails) → contract number (fails) → escalate | ✅ run |
| `e2e_edge_case_lookup_failure_full_vin_then_claim` | contract_holder/edge_cases/scenario_13_lookup_failure_full_vin_then_claim.yaml | ANI lookup fails → full 17-char VIN (extract last 8, fails) → claim number (fails) → escalate | ✅ run |
| `e2e_edge_case_full_vin_lookup` | contract_holder/edge_cases/full_vin_lookup_row14.yaml | Customer provides full 17-char VIN — agent extracts last 8 without asking customer to repeat | ✅ run |
| `e2e_edge_case_no_identifier` | contract_holder/edge_cases/scenario_5_no_identifier_provided.yaml | Customer cannot provide any identifier for lookup | ✅ run |

### Edge Cases — Contract / Claim Data

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_edge_case_multiple_contracts` | contract_holder/edge_cases/scenario_2_multiple_contracts.yaml | Customer has multiple active contracts — agent disambiguates to correct vehicle | ✅ run |
| `e2e_edge_case_multiple_contracts_claim_check` | contract_holder/edge_cases/scenario_9_multiple_contracts_claim_check.yaml | Customer with two contracts asks about a claim without identifying which vehicle | ✅ run |
| `e2e_edge_case_data_discrepancy` | contract_holder/edge_cases/scenario_6_data_discrepancy.yaml | Customer identifies discrepancy between paperwork and system data | ✅ run |
| `e2e_edge_case_correction_needed` | contract_holder/edge_cases/scenario_7_correction_needed_claim.yaml | Claim shows "Correction Needed" — customer wants to know what's required | ✅ run |
| `e2e_edge_case_numeric_limit_disclaimer` | contract_holder/edge_cases/scenario_8_numeric_limit_disclaimer.yaml | Agent must include disclaimer before quoting numeric coverage limits | ✅ run |

### Edge Cases — Human Request

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_edge_case_explicit_agent_request` | contract_holder/edge_cases/scenario_4_explicit_agent_request.yaml | Customer explicitly requests a human from the very start | ✅ run |
| `e2e_edge_case_queue_closed` | contract_holder/edge_cases/scenario_3_queue_closed.yaml | Customer requests escalation but queue is closed outside business hours | ✅ run |
| `e2e_edge_case_ch_human_request_billing_dispute` | contract_holder/edge_cases/scenario_14_ch_human_request_billing_dispute.yaml | CH immediately requests human — billing dispute → escalate (GAIntent=PREMIUMS) | ✅ run |
| `e2e_edge_case_ch_human_request_portal_login` | contract_holder/edge_cases/scenario_15_ch_human_request_portal_login.yaml | CH says "I need a human" with no reason → agent asks why → portal login issue → escalate | ✅ run |
| `e2e_edge_case_ch_human_request_steered_to_resolution` | contract_holder/edge_cases/scenario_16_ch_human_request_steered_to_resolution.yaml | CH opens with human request but actual need is claim status → agent handles it without escalating | ✅ run |
| `e2e_ch_mid_journey_human_request` | contract_holder/edge_cases/scenario_ch_mid_journey_human_request.yaml | CH checks claim status then mid-conversation asks for human without reason → agent probes → rental coverage question is in-scope → answered without escalating | |

---

## Repair Facility

### Routing

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_rf_ani_routing` | repair_facility/scenario_6_ani_routing_direct.yaml | Recognized ANI — caller type confirmed as RF, agent routes directly | ✅ run |

### Existing Claims

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_rf_existing_claim_authorization` | repair_facility/scenario_1_existing_claim_authorization.yaml | RF checks authorization status on existing claim — resolves via IVR | ✅ run |
| `e2e_rf_existing_claim_payment` | repair_facility/scenario_2_existing_claim_payment_inquiry.yaml | RF follows up on payment for a completed claim | ✅ run |
| `e2e_rf_existing_claim_modification` | repair_facility/scenario_3_existing_claim_needs_modification.yaml | RF requests supplement for additional parts — agent escalates to claims team | ✅ run |
| `e2e_rf_claim_not_found_fallback` | repair_facility/claim_not_found_fallback_CA444e80d0a1a60aebc7ec9a4b365faf5c.yaml | Claim number lookup fails — agent informs RF and provides fallback guidance | ✅ run |
| `e2e_rf_multi_issue_claim_status_and_new_claim` | repair_facility/scenario_multi_issue_claim_status_and_new_claim.yaml | RF asks about existing claim status, then asks about filing a new claim | ✅ run |
| `e2e_rf_terminology_and_extended_status` | repair_facility/rf_terminology_CA707224c792b458256a5838fa064e1222.yaml | Agent must use "independent repair facilities" (not "repair shops") and provide extended status | ✅ run |

### New Claims / RO Submission

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_rf_new_claim_no_ro_email_guidance` | repair_facility/scenario_4_new_claim_portal_link.yaml | New claim, no RO submitted — agent provides email guidance (ro@autoclaims.com) | ✅ run |
| `e2e_rf_new_claim_ro_submitted_found` | repair_facility/scenario_5_new_claim_ro_submitted.yaml | RF emailed RO — agent finds the claim and confirms status | ✅ run |
| `e2e_rf_new_claim_ro_email_sent_not_filed` | repair_facility/scenario_5b_new_claim_ro_email_sent_not_filed.yaml | RF emailed RO and got a case number but claim was never fully filed — agent guides to complete it | ✅ run |
| `e2e_rf_ro_email_not_upload` | repair_facility/ro_email_not_upload_CA444e80d0a1a60aebc7ec9a4b365faf5c.yaml | RF asks how to submit RO — agent must say email to ro@autoclaims.com, NOT upload via portal | ✅ run |
| `e2e_rf_new_claim_steered_to_online` | repair_facility/scenario_new_claim_steered_to_online.yaml | RF initially prefers phone filing but agrees to use online portal | ✅ run |
| `e2e_rf_new_claim_phone_insists` | repair_facility/scenario_new_claim_phone_insists.yaml | RF insists on phone filing — agent steers toward online but accommodates if insisted | ✅ run |
| `e2e_rf_new_claim_online_after_case_number` | repair_facility/scenario_new_claim_online_after_case_number.yaml | RF insists on phone, goes through full RO email process, then accepts online filing offer once case number is in hand | |
| `e2e_rf_coverage_eligibility_before_claim` | repair_facility/scenario_coverage_eligibility_before_claim.yaml | RF asks whether a specific repair is covered before filing a claim | ✅ run |
| `e2e_rf_new_claim_no_premature_wrap_up` | repair_facility/scenario_new_claim_no_premature_wrap_up.yaml | Regression: agent must not ask "Is there anything else?" or end call while RF is still emailing the RO — must stay on line, wait for case number, then escalate | |
| `e2e_rf_sms_failure_silent_proceed` | repair_facility/scenario_sms_failure_silent_proceed.yaml | Regression: `send_sms_to_phone` fails (null response) — agent must NOT surface the failure to the caller, must still inform about the self-service portal, and proceed normally to assist | |

### Encryption / Variable Handling

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_rf_encrypted_variables_claim_status_escalation` | repair_facility/scenario_encrypted_variables_claim_status_escalation.yaml | Regression: PhoneNumber arrives encrypted — tests decrypt_variables fires first, decrypted number used in API calls, encrypt_variables called before transfer, escalation receives encrypted PII | |

### Human Request

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_rf_human_request_steered_to_resolution` | repair_facility/scenario_rf_human_request_steered_to_resolution.yaml | RF opens with human request, actual need is claim auth → agent handles it without escalating | ✅ run |
| `e2e_rf_immediate_human_request_dispute` | repair_facility/scenario_rf_immediate_human_request.yaml | RF immediately requests live agent to dispute a denied claim → escalate | ✅ run |
| `e2e_rf_mid_journey_human_request` | repair_facility/scenario_rf_mid_journey_human_request.yaml | RF checks authorization status then mid-conversation asks for human without reason → agent probes → authorization dispute is out-of-scope → escalate | |
| `e2e_rf_new_claim_immediate_agent_hoop_failure` | repair_facility/rf_immediate_agent_hoop_failure.yaml | Regression: RF asks for agent immediately after portal offer, declines chat, `get_hoop_message` fails on first call (schema error) then succeeds on retry — agent must NOT ask customer about queue hours and must eventually transfer | |

---

## Dealership

### Existing Claims

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_dealership_existing_claim_authorization` | dealership/scenario_1_existing_claim_authorization.yaml | Dealership checks authorization status — resolves via IVR without escalation | ✅ run |
| `e2e_dealership_existing_claim_denied` | dealership/scenario_2_existing_claim_denied.yaml | Dealership on a denied claim — agent looks up status and escalates to specialist | ✅ run |
| `e2e_dealership_payment_inquiry` | dealership/scenario_3_payment_inquiry.yaml | Dealership inquires about payment timeline — escalates to payment specialist | ✅ run |
| `e2e_dealership_claim_modification` | dealership/scenario_4_claim_modification.yaml | Dealership needs to add parts to existing claim — escalates to claims team | ✅ run |
| `e2e_dealership_multi_issue_claim_status_and_new_claim` | dealership/scenario_multi_issue_claim_status_and_new_claim.yaml | Dealership asks about payment on existing claim, then asks about filing a new one | ✅ run |

### New Claims / Portal

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_dealership_new_claim_portal` | dealership/scenario_5_new_claim_portal.yaml | Dealership starts new claim — no RO yet, agent directs to autorepairs.assurant.com | ✅ run |
| `e2e_dealership_no_ro_upload_required` | dealership/dealer_no_ro_upload_CAd789bf025f5c6b445548986b2d0f5281.yaml | Dealership starting new claim — agent must NOT say RO upload is required; if phone preferred, have RO+VIN ready | ✅ run |
| `e2e_dealership_portal_correct_url_new_claim` | dealership/dealer_portal_new_claim_CA48b739dec25d5ac50f2667ca933a5292.yaml | Agent must use autorepairs.assurant.com (dealer portal), NOT vehiclecareplan.com | ✅ run |

### Other

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_dealership_contract_modification` | dealership/scenario_6_contract_modification.yaml | Dealership requests contract modification (adding GAP) — escalates | ✅ run |

### Human Request

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_dealer_human_request_steered_to_resolution` | dealership/scenario_dealer_human_request_steered_to_resolution.yaml | Dealer opens with human request, actual need is claim auth → agent handles it without escalating | ✅ run |
| `e2e_dealer_immediate_human_request_contract_mod` | dealership/scenario_dealer_immediate_human_request.yaml | Dealer immediately requests live agent for contract modification → escalate | ✅ run |
| `e2e_dealer_mid_journey_human_request` | dealership/scenario_dealer_mid_journey_human_request.yaml | Dealer checks payment status then mid-conversation asks for human without reason → agent probes → address redirect is out-of-scope → escalate | |

---

## Routing

| ID | File | Description | Run |
|---|---|---|---|
| `144051fe-eea9-4843-a672-8101bb60f82d` | routing/scenario_1_dealership_caller.yaml | Selling dealership calling on behalf of customer — routes to Dealership flow | ✅ run |
| `e2e_routing_employee_caller` | routing/scenario_2_employee_caller.yaml | Assurant employee calling — routes to Employee flow | ✅ run |
| `e2e_routing_unknown_caller` | routing/scenario_3_unknown_caller_type.yaml | Ambiguous caller type — agent clarifies then routes | ✅ run |
| `e2e_routing_ani_mismatch` | routing/scenario_4_ani_mismatch_caller_says_contract_holder.yaml | ANI says RF but caller says CH — agent trusts the caller | ✅ run |
| `e2e_routing_caller_id_wording` | routing/caller_id_wording_CAd789bf025f5c6b445548986b2d0f5281.yaml | Welcome message must use correct professional caller-type identification wording | ✅ run |
| `e2e_routing_department_names_approved_only` | routing/department_names_row61.yaml | Agent must only refer to the four approved department names (Claims, Customer Care, Payments, Premiums) | ✅ run |

---

## Employee

| ID | File | Description | Run |
|---|---|---|---|
| `e2e_employee_immediate_escalation` | employee/scenario_1_immediate_escalation.yaml | Assurant employee calls in — EmployeeIssues immediately escalates to human agent | ✅ run |

---

## Coverage Counts

| Caller Type | Scenarios |
|---|---|
| Contract Holder | 45 |
| Repair Facility | 22 |
| Dealership | 12 |
| Routing | 6 |
| Employee | 1 |
| **Total** | **86** |

> Target scenarios (`target/`) are for a separate client and are excluded from this index.
