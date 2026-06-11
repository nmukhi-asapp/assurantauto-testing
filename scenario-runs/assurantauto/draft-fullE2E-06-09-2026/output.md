# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 5.0
- **Passed**: 4.0
- **Failed**: 1.0
- **Pass Rate**: 80.0%
- **Total Cost**: $0.1877

## Scenario Details

### Scenario: `e2e_dealer_coverage_question_engine_mounts`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1877

#### Evaluation Results

**Evaluation 1**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent routes to DealershipIssues after the caller identifies as a dealership

**Evaluation 2**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks for a vehicle identifier before looking up the contract

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr to retrieve the contract data

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent uses the termsStructuredText to respond to the engine mount coverage question rather than escalating immediately

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent describes what the contract terms say about engine coverage without explicitly confirming or denying that engine mounts are definitively covered

#### Customer Goal Evaluation

- **Status**: ✅ Passed
- **Pass Percentage**: 100.0%
- **Attempted**: True

---
