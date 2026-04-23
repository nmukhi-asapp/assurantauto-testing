# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 143.0
- **Passed**: 59.0
- **Failed**: 84.0
- **Pass Rate**: 41.3%
- **Total Cost**: $4.9809

## Scenario Details

### Scenario: `e2e_rf_multi_issue_claim_status_and_new_claim`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2224

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up claim 47407207 using an available claim lookup function

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent communicates the claim status (Under Review) to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains what the Under Review status means using the longVerbiageStatus or equivalent explanation, without escalating to a human agent for this question

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent addresses the caller's second issue (starting a new claim) without requiring a new call or immediately escalating

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent solely because the caller asked what the status means

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_encrypted_variables_claim_status_escalation`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3009

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls decrypt_variables before calling is_repair_facility, send_sms_to_phone, or any claim lookup function

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent looks up the claim using claim number 37020301A and provides the status to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The decrypted phone number (1064378068, not the encrypted value) is used as the PhoneNumber parameter in is_repair_facility or send_sms_to_phone

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls encrypt_variables before calling escalate_to_agent_from_ivr

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls escalate_to_agent_from_ivr with an encrypted ClaimNumber (the value returned by encrypt_variables, not the plain-text claim number 37020301A)

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_phone_insists`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3118

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent informs the caller that the online filing option is faster or more straightforward before proceeding with phone filing

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller to inform them when the email response with the case number arrives

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller for the case number from the response email

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent before first obtaining the case number from the caller

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_immediate_human_request_dispute`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2819

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks what the caller needs help with before escalating, rather than blindly escalating on the request alone

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent recognizes the authorization dispute cannot be resolved through the IVR and escalates using escalate_to_agent_from_ivr, OR informs the customer that agents are not currently available due to business hours

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent informs the caller they will be connected to the appropriate team, OR informs the customer that agents are not currently available due to business hours

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_sms_failure_silent_proceed`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2389

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 2/2 (100.0%)

**Rules**:
  1. ✅ Agent does NOT say anything about a technical issue, a failed SMS, or a self-service portal link that could not be sent
  2. ✅ Agent does NOT mention that it attempted to send a link and failed

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent proceeds to handle the caller's repair facility needs without referencing the SMS outcome — either by asking about claim type or by responding to what the caller volunteers

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent informs the caller about the self-service portal (autoclaims.com) — either verbally telling them about it or confirming a link was sent — regardless of whether the SMS succeeded or failed

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent directs the repair facility to email the Repair Order to ro@autoclaims.com and explains they will receive an email response with a case number

**Evaluation 6**:

- **Applicable**: False

**Evaluation 7**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_steered_to_online`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1943

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the online filing option is faster or more straightforward when the caller expresses a preference for phone

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent directs the caller to email the Repair Order to ro@autoclaims.com after they agree to proceed online

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the caller will receive a case number by email to complete the online filing

**Evaluation 5**:

- **Applicable**: False

**Evaluation 6**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_human_request_steered_to_resolution`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2414

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks what the caller needs help with before deciding whether to escalate

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent recognizes the claim status inquiry is within its scope and does NOT escalate

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks for a claim identifier and looks up the claim using getClaimsClaimNumber

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent provides the authorization status and informs the caller the authorization letter was sent

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT transfer to a human agent

**Evaluation 7**:

- **Applicable**: False

**Evaluation 8**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_ro_email_sent_not_filed`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2761

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT attempt a claim lookup (no claim exists yet)

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent directs the caller to use their case number to file the claim online

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_coverage_eligibility_before_claim`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2229

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the contract or claim data to check coverage for the vehicle

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent uses the contract coverage information to address whether the repair type may be covered, without immediately escalating

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the pre-authorization requirement (caller must get authorization before repairs begin) using available contract or process knowledge

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent solely because the caller asked about coverage eligibility before filing

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_terminology_and_extended_status`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2512

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent uses the term 'repair facilities' or 'independent repair facilities', NOT 'repair shops' or 'independent repair shops'

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using the provided claim number or last 8 VIN

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent provides an extended status description (longVerbiageStatus) explaining what the status means, not just a short status label

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent without first communicating the extended claim status to the caller

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_ro_submitted_found`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2020

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using the provided claim number or identifier

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent communicates the current status of the submitted claim to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_online_after_case_number`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2728

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent informs the caller that the online filing option is faster or more straightforward before proceeding with phone filing

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller to inform them when the email response with the case number arrives

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller for the case number from the response email

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After obtaining the case number, agent offers the caller the option to file the claim online using that case number

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains to the caller that they can use the case number to file the claim online at autoclaims.com

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT escalate to a human agent or call escalate_to_agent_from_ivr after the caller agrees to file online

**Evaluation 9**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_ro_email_not_upload`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2177

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ When discussing Repair Order submission, agent directs the RF to email the RO to ro@autoclaims.com

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT tell the repair facility to upload the Repair Order directly through a web portal (e.g. does NOT say 'upload via the portal' or direct them to submit it through autorepairs.assurant.com or autoclaims.com upload form)

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT reference autorepairs.assurant.com for repair facility RO submission (that portal is for dealerships)

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains that after emailing the RO, the caller will receive an email response with a case number they can use to file the claim online

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_mid_journey_human_request`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2697

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using the claim number or other identifier provided

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent provides the authorization status of the claim to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ When the caller requests a live agent, the agent asks what they need help with before escalating

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Caller states they want to dispute the authorization amount or payout

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent recognizes the authorization dispute cannot be resolved through the IVR and escalates using escalate_to_agent_from_ivr, OR informs the customer that agents are not currently available due to business hours

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent informs the caller they will be connected to the appropriate team, OR informs the customer that agents are not currently available due to business hours

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 9**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_ani_routing`

- **Run Index**: 0
- **Execution Status**: failed
- **Cost**: $0.0000

---

### Scenario: `e2e_rf_existing_claim_authorization`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2250

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent must first offer self-service portal website to help the caller

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using contract number, VIN last 8, or claim number

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent provides the authorization status of the claim

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_claim_not_found_fallback`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2338

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent attempts claim lookup using the provided claim number

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ When the claim is not found, agent clearly tells the caller the claim could not be found

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After a failed claim lookup, agent offers to look up using an alternative identifier — contract number OR last 8 digits of VIN

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT repeatedly ask the caller to restate the same claim number without offering alternative identifiers

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent successfully retrieves the claim when provided the contract number as an alternative identifier

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_existing_claim_payment`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2100

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent must first offer self-service portal website to help the caller

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using the claim number or other identifier provided

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent provides the payment status and explains next steps for payment

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_no_premature_wrap_up`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3333

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller to let them know when the email response with the case number arrives

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the caller for the case number from the response email

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT end the conversation or call end_of_conversation before the caller has provided the case number

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After the caller says they are still emailing the Repair Order, agent does NOT treat this as a conversation-ending response — agent stays on the line and continues assisting

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT call escalate_to_agent_from_ivr or end_of_conversation before first obtaining the case number from the caller

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 9**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_existing_claim_modification`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2452

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent must first offer self-service portal website to help the caller

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the existing claim

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent escalates to claims team or transfers to appropriate specialist for claim modification, OR informs the customer that agents are not currently available due to business hours

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does not attempt to approve or modify the claim authorization amount directly

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_no_ro_email_guidance`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2297

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent directs the repair facility to email the Repair Order to ro@autoclaims.com

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the caller will receive an email response with a case number within a few minutes

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the caller can use that case number to file the claim online

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Repair Facility: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, NEWCLAIM-OCR-EMAIL, NEWCLAIM-OCR-TEXT, UPDATECLAIM, COVERAGEINFO, GAP, PAYMENT, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Repair Facility'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
