# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 9.0
- **Passed**: 0.0
- **Failed**: 9.0
- **Pass Rate**: 0.0%
- **Total Cost**: $0.1170

## Scenario Details

### Scenario: `e2e_dealership_payment_inquiry`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1170

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent routes to DealershipIssues after the caller identifies as a Dealership
- **Error**: Failed to run rules: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks for a claim identifier and looks up the claim using an available claim lookup function
- **Error**: Failed to run rules: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent identifies the claim status as Payment Authorized or similar and communicates it to the caller
- **Error**: Failed to run rules: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent escalates using escalate_to_agent_from_ivr for specific payment timeline information, OR informs the customer that agents are not currently available due to business hours
- **Error**: Failed to run rules: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 5**:

- **Applicable**: False
- **Error**: Failed to run applicability: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ ClaimStatus is set to 'Authorized'
- **Error**: Failed to run rules: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 7**:

- **Applicable**: False
- **Error**: Failed to run applicability: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 8**:

- **Applicable**: False
- **Error**: Failed to run applicability: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

**Evaluation 9**:

- **Applicable**: False
- **Error**: Failed to run applicability: litellm.InternalServerError: InternalServerError: Litellm_proxyException - Connection error.

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
