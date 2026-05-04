# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 7.0
- **Passed**: 2.0
- **Failed**: 5.0
- **Pass Rate**: 28.6%
- **Total Cost**: $0.2307

## Scenario Details

### Scenario: `e2e_dealer_chat_deflection_declined_phone_transfer`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2307

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
  1. ✅ Agent offers chat support before attempting a phone transfer (Unified Escalation Protocol Step 1 — mandatory chat deflection)

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After the caller declines chat, agent does NOT end the conversation or ask "Is there anything else I can help you with?"

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ After the caller declines chat, agent asks for a claim number, contract number, or VIN before transferring (Unified Escalation Protocol Step 2A)

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent eventually calls escalate_to_agent_from_ivr to transfer the caller to a phone agent

**Evaluation 6**:

- **Applicable**: False

**Evaluation 7**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
