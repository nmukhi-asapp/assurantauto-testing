# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 64.0
- **Passed**: 40.0
- **Failed**: 24.0
- **Pass Rate**: 62.5%
- **Total Cost**: $2.1100

## Scenario Details

### Scenario: `e2e_rf_new_claim_phone_insists`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2559

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent informs the caller that the online filing option is faster or more straightforward before proceeding with phone filing

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the caller to inform them when the email response with the case number arrives

**Evaluation 5**:

- **Applicable**: False

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or escalate_to_live_agent before first obtaining the case number from the caller

**Evaluation 7**:

- **Applicable**: False

**Evaluation 8**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_immediate_agent_hoop_failure`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3906

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent offers the online portal or self-service option before attempting escalation

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent follows the Unified Escalation Protocol by offering chat before phone transfer when escalate_to_live_agent is triggered

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT end the conversation or start wrap-up after the customer declines the chat option

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT ask the customer whether the Customer Service queue, Claims queue, or any department is open or available

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent eventually calls escalate_to_agent_from_ivr to transfer the caller to a phone agent

**Evaluation 7**:

- **Applicable**: False

**Evaluation 8**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_sms_failure_silent_proceed`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1838

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

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
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent directs the repair facility to email the Repair Order to ro@autoclaims.com and explains they will receive an email response with a case number

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
- **Cost**: $0.1985

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent explains the online filing option is faster or more straightforward when the caller expresses a preference for phone

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent directs the caller to email the Repair Order to ro@autoclaims.com after they agree to proceed online

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

### Scenario: `e2e_rf_new_claim_ro_email_sent_not_filed`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1144

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT attempt a claim lookup (no claim exists yet)

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent directs the caller to use their case number to file the claim online

**Evaluation 4**:

- **Applicable**: False

**Evaluation 5**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_ro_submitted_found`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1851

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent looks up the claim using the provided claim number or identifier

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent communicates the current status of the submitted claim to the caller

**Evaluation 4**:

- **Applicable**: False

**Evaluation 5**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_online_after_case_number`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3011

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent informs the caller that the online filing option is faster or more straightforward before proceeding with phone filing

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the caller to inform them when the email response with the case number arrives

**Evaluation 5**:

- **Applicable**: False

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After obtaining the case number, agent offers the caller the option to file the claim online using that case number

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent explains to the caller that they can use the case number to file the claim online at autoclaims.com

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT escalate to a human agent or call escalate_to_agent_from_ivr after the caller agrees to file online

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_no_premature_wrap_up`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3060

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent instructs the caller to email the Repair Order to ro@autoclaims.com and asks them to confirm when it has been sent

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the caller to let them know when the email response with the case number arrives

**Evaluation 4**:

- **Applicable**: False

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT end the conversation or call end_of_conversation before the caller has provided the case number

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ After the caller says they are still emailing the Repair Order, agent does NOT treat this as a conversation-ending response — agent stays on the line and continues assisting

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call escalate_to_agent_from_ivr or end_of_conversation before first obtaining the case number from the caller

**Evaluation 8**:

- **Applicable**: False

**Evaluation 9**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_rf_new_claim_no_ro_email_guidance`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1745

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to RepairShopIssues after the caller identifies as a repair facility

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent directs the repair facility to email the Repair Order to ro@autoclaims.com

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent explains the caller will receive an email response with a case number within a few minutes

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent explains the caller can use that case number to file the claim online

**Evaluation 5**:

- **Applicable**: False

**Evaluation 6**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
