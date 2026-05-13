# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 5.0
- **Passed**: 4.0
- **Failed**: 1.0
- **Pass Rate**: 80.0%
- **Total Cost**: $0.1512

## Scenario Details

### Scenario: `e2e_dealership_case_number_lookup`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1512

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
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent calls get_claims_case_number or getClaimsClaimNumber with the case number provided by the caller, without first asking the caller to re-identify the number type

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent presents claim status to the caller or escalates, using the data returned by the lookup

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
