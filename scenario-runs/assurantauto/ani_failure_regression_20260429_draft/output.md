# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 30.0
- **Passed**: 27.0
- **Failed**: 3.0
- **Pass Rate**: 90.0%
- **Total Cost**: $1.2829

## Scenario Details

### Scenario: `e2e_ch_ani_failure_asks_for_identifier`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2966

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
  1. ✅ After the customer identifies as a Contract Holder, agent asks for a claim number, contract number, or the last 8 characters of their VIN before asking 'Is there anything else I can help you with?' or ending the call

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call end_of_conversation before asking the customer for an identifier

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the customer for an identifier (claim number, contract number, or VIN) as its first substantive action in ContractHolderIssues

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent reads back the contract number VSC887701 and asks the customer to confirm before making the API call

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr using the customer-confirmed contract number

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_ani_failure_asks_for_identifier`

- **Run Index**: 1
- **Execution Status**: success
- **Cost**: $0.2880

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
  1. ✅ After the customer identifies as a Contract Holder, agent asks for a claim number, contract number, or the last 8 characters of their VIN before asking 'Is there anything else I can help you with?' or ending the call

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call end_of_conversation before asking the customer for an identifier

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the customer for an identifier (claim number, contract number, or VIN) as its first substantive action in ContractHolderIssues

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent reads back the contract number VSC887701 and asks the customer to confirm before making the API call

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr using the customer-confirmed contract number

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_ani_failure_asks_for_identifier`

- **Run Index**: 2
- **Execution Status**: success
- **Cost**: $0.2156

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
  1. ✅ After the customer identifies as a Contract Holder, agent asks for a claim number, contract number, or the last 8 characters of their VIN before asking 'Is there anything else I can help you with?' or ending the call

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call end_of_conversation before asking the customer for an identifier

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent asks the customer for an identifier (claim number, contract number, or VIN) as its first substantive action in ContractHolderIssues

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent reads back the contract number VSC887701 and asks the customer to confirm before making the API call

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr using the customer-confirmed contract number

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_ani_failure_asks_for_identifier`

- **Run Index**: 3
- **Execution Status**: success
- **Cost**: $0.2613

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
  1. ✅ After the customer identifies as a Contract Holder, agent asks for a claim number, contract number, or the last 8 characters of their VIN before asking 'Is there anything else I can help you with?' or ending the call

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call end_of_conversation before asking the customer for an identifier

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the customer for an identifier (claim number, contract number, or VIN) as its first substantive action in ContractHolderIssues

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 0/1 (0.0%)

**Rules**:
  1. ❌ Agent reads back the contract number VSC887701 and asks the customer to confirm before making the API call

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr using the customer-confirmed contract number

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_ch_ani_failure_asks_for_identifier`

- **Run Index**: 4
- **Execution Status**: success
- **Cost**: $0.2213

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
  1. ✅ After the customer identifies as a Contract Holder, agent asks for a claim number, contract number, or the last 8 characters of their VIN before asking 'Is there anything else I can help you with?' or ending the call

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT call end_of_conversation before asking the customer for an identifier

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent asks the customer for an identifier (claim number, contract number, or VIN) as its first substantive action in ContractHolderIssues

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent reads back the contract number VSC887701 and asks the customer to confirm before making the API call

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr using the customer-confirmed contract number

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
