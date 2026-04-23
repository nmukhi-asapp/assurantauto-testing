# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 7.0
- **Passed**: 5.0
- **Failed**: 2.0
- **Pass Rate**: 71.4%
- **Total Cost**: $0.1885

## Scenario Details

### Scenario: `e2e_journey1_selling_dealer_first_recommendation`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1885

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
  1. ✅ Agent calls get_contract_and_claims_data_ivr before answering the customer's questions

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent recommends the selling dealer as the first option for repairs before mentioning independent repair facilities

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT say 'vehicle service contract' — must refer to it simply as 'contract' or 'coverage'

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent provides the selling dealer name or contact information from the contract data

**Evaluation 6**:

- **Applicable**: False

**Evaluation 7**:

- **Applicable**: False

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
