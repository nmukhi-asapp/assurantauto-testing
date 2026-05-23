# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 71.0
- **Passed**: 49.0
- **Failed**: 22.0
- **Pass Rate**: 69.0%
- **Total Cost**: $2.4818

## Scenario Details

### Scenario: `e2e_dealership_multi_issue_claim_status_and_new_claim`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3346

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to DealershipIssues after the caller identifies as a Dealership

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up claim 37030101 using an available claim lookup function

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent communicates the claim status (Payment Authorized) to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent explains what Payment Authorized means using the longVerbiageStatus or equivalent explanation, without escalating to a human agent solely for this question

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent addresses the caller's second issue (starting a new claim) without requiring a new call or immediately escalating

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent solely because the caller asked what the payment status means

**Evaluation 7**:

- **Applicable**: False

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_dealership_case_number_lookup`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2048

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to DealershipIssues after the caller identifies as a Dealership

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent categorizes the inquiry as an existing claim issue

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ After the caller explicitly identifies their number as a case number (e.g., says "case number 49137123"), the agent does NOT follow up by asking whether that number is a claim number, contract number, or VIN. The agent proceeds directly to confirm and look up the number without re-requesting the identifier type.


**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_claims_case_number or getClaimsClaimNumber with the case number provided by the caller, without first asking the caller to re-identify the number type

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent presents claim status to the caller or escalates, using the data returned by the lookup

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_dealership_new_claim_portal`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2121

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to DealershipIssues after the caller identifies as a Dealership

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent identifies the caller's issue as a new claim

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks whether the Repair Order or claim submission has already been filed with Assurant — accepts any equivalent phrasing such as 'Have you submitted the Repair Order?', 'Have you already submitted the claim online?', or similar

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The caller provided the vehicle VIN to the agent before being transferred to a claims adjuster

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Dealership: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, UPDATECLAIM, COVERAGEINFO, GAP, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Selling Dealer'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_dealership_payment_inquiry`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3260

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to DealershipIssues after the caller identifies as a Dealership

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks for a claim identifier and looks up the claim using an available claim lookup function

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent identifies the claim status as Payment Authorized or similar and communicates it to the caller

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent escalates using escalate_to_agent_from_ivr for specific payment timeline information, OR informs the customer that agents are not currently available due to business hours

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ GAIntent is set to 'CLAIMS' or 'CLAIMSTATUS'

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ ClaimStatus is set to 'Authorized'

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Dealership: CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, UPDATECLAIM, COVERAGEINFO, GAP, RV, GA_ERROR, ALLOTHER_QUESTIONS, DEFAULT

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ GAIntent is set to 'CLAIMSTATUS'

**Evaluation 9**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Selling Dealer'

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_rental_coverage_followup`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2678

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to the Contract Holder service flow after customer identifies as a Contract Holder

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr to retrieve contract data before answering

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent provides a general overview of contract coverage using the retrieved contract data

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent answers the rental car follow-up question without escalating to a human agent

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent provides the specific rental reimbursement amount ($35 per day) from the contract terms

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent provides the maximum rental duration (10 days) from the contract terms

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent to answer the rental coverage follow-up question

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_journey5_coverage_where_to_repair`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3054

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to the Contract Holder service flow after customer identifies as a Contract Holder

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr before answering the customer's substantive questions

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent recommends the selling dealer (Texas Auto Group) as the first option before mentioning independent repair facilities

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent clarifies the customer may also use any licensed independent repair facility of their choice

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains the repair facility must contact Assurant for authorization before starting work

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT use the term 'repair shop' or 'independent repair shop' — must say 'repair facility' or 'independent repair facility'

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent provides accurate policy information from the contract terms

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_rental_roadside_inline`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2884

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to ContractHolderIssues after the caller identifies as a contract holder

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent answers the deductible question using data from get_contract_and_claims_data_ivr without escalating

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent does NOT escalate to a live agent solely because the customer asked about rental car benefits when an authorized claim exists and rentalIndicator is Y

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent handles the rental inquiry inline using Journey 3 — presents booking options (Enterprise booking vs. self-booking for reimbursement) since the claim is authorized

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent handles the roadside coverage question using termsStructuredText from contract data

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the agent escalated the call, the GAIntent output variable is set to one of the valid values for Contract Holder: CANCELLATION, CARRENTAL, CLAIMS, CLAIMSTATUS, NEWCLAIM, CONTRACTCHANGES, COVERAGEINFO, GAP, LOCATE_RF, PAYMENT, ROADSIDE_ASSISTANCE, RV, GA_ERROR, PREMIUMS, ALLOTHER_QUESTIONS, DEFAULT

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_journey7_unknown_intent`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3202

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to the Contract Holder service flow after customer identifies as a Contract Holder

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr before answering the customer's substantive questions

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks clarifying questions to understand what the customer needs help with

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent attempts to understand and route the customer's request to the appropriate service area

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ If the customer's need remains unclear after clarification attempts, agent escalates using escalate_to_agent_from_ivr, OR informs the customer that agents are not currently available due to business hours

**Evaluation 6**:

- **Applicable**: False

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Question field captures the agent's best understanding of the customer's inquiry

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_journey5_coverage_definitive`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2224

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to the Contract Holder service flow after customer identifies as a Contract Holder

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr before answering the customer's substantive questions

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent initially provides a qualified answer referencing the termsStructuredText

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ When customer insists on a definitive answer, agent escalates using escalate_to_agent_from_ivr, OR informs the customer that agents are not currently available due to business hours

**Evaluation 5**:

- **Applicable**: False

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Question field captures the specific turbocharger coverage question and repair cost

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent explains that a specialist can provide a detailed coverage determination

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
