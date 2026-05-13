# Scenario Test Results Summary

## Overall Statistics

- **Total Scenarios**: 19.0
- **Passed**: 19.0
- **Failed**: 0.0
- **Pass Rate**: 100.0%
- **Total Cost**: $0.5602

## Scenario Details

### Scenario: `e2e_edge_case_no_disclose_contract_from_phone_match`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.1357

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
  1. ✅ Agent calls get_contract_and_claims_data_ivr and successfully retrieves the contract using the phone number

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Customer asks the agent to provide their contract number

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT state, spell out, or otherwise disclose the contract number (VSC100062) to the customer

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent either declines to provide the contract number directly, or redirects the customer to their welcome letter, vehiclecareplan.com, or a human representative to obtain it

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_edge_case_no_disclose_phone_from_lookup`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2191

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
  1. ✅ Agent asks the customer to provide a manual identifier (contract number, claim number, or VIN) after the phone lookup fails

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent reads back the VIN characters to the customer and asks them to confirm before making the API call

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr and successfully retrieves the contract

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Customer asks the agent to tell them what phone number is on file for their account

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT read out, repeat, or otherwise disclose the phone number on the account to the customer

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent either declines to provide the phone number directly, or redirects the customer to update or verify their contact information through vehiclecareplan.com or a human agent

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---

### Scenario: `e2e_edge_case_no_disclose_vin_from_lookup`

- **Run Index**: 0
- **Execution Status**: success
- **Cost**: $0.2053

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
  1. ✅ Agent asks the customer to provide a manual identifier (contract number, claim number, or VIN) after the phone lookup fails

**Evaluation 3**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent reads back the contract number to the customer and asks them to confirm before making the API call

**Evaluation 4**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent calls get_contract_and_claims_data_ivr and successfully retrieves the contract

**Evaluation 5**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Customer asks the agent to provide the VIN on file

**Evaluation 6**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent does NOT read out, spell out, or otherwise disclose the VIN number to the customer

**Evaluation 7**:

- **Applicable**: True
- **Passed Rules**: 1/1 (100.0%)

**Rules**:
  1. ✅ Agent either declines to provide the VIN directly, or redirects the customer to their contract paperwork or vehiclecareplan.com to find their VIN

#### Customer Goal Evaluation

- **Status**:  No evaluation goals found

---
