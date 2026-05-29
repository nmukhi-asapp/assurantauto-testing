# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 9.0
- **Passed**: 7.0
- **Failed**: 2.0
- **Pass Rate**: 77.8%
- **Total Cost**: $0.3588

## Scenario Details

### Scenario: `e2e_dealer_new_claim_submitted_multi_claim_adjuster_request`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.3588

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to the Dealership service flow after the caller identifies as a Dealer

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks whether the caller has already submitted the claim online before collecting any identifier

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After the caller confirms the claim was submitted online, agent asks for the VIN or contract number — the agent does NOT ask for a claim number as the primary or only identifier option

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ When the caller asks to speak to an adjuster or agent during the new claim flow, the agent does not restart the entire new claim flow from scratch (re-asking 'have you submitted online?'). Instead, it works toward connecting the caller to a Claims Agent.

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks for the VIN or contract number as the one piece of information needed before transfer — the agent does NOT ask for a claim number in this context

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ If the caller provides a VIN, agent uses it in the transfer; if the caller refuses or cannot provide an identifier, agent transfers anyway rather than looping

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent transfers the caller to a Claims Agent via escalate_to_agent_from_ivr

**Evaluation 8**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GACallerType parameter passed to escalate_to_agent_from_ivr is 'Selling Dealer'

**Evaluation 9**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ The GAIntent parameter passed to escalate_to_agent_from_ivr reflects a new claim or general claims intent (NEWCLAIM, CLAIMS, or CLAIMSTATUS)

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
