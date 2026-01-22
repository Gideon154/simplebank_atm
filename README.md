# simplebank_atm
# Project: SimpleBank_ATM

## 1. Requirement Analysis
**Goal:** Develop a simulation of a basic banking system.
**Scope:**
- User can create an account with an initial balance.
- System processes deposits to increase balance.
- System validates and processes withdrawals.
- System generates account statements.

## 2. System Design
The system is designed using Object-Oriented principles. The following nomenclature maps the design to the implementation:

| Entity | Code Name | Function |
| :--- | :--- | :--- |
| **Class** | `BankAccount` | Data structure for user details and balance. |
| **Class** | `BankService` | Logic controller for financial operations. |
| **Method** | `process_deposit` | Logic to validate and add funds. |
| **Method** | `process_withdrawal` | Logic to check limits and deduct funds. |
| **Method** | `get_status` | Logic to display formatted output. |

## 3. Implementation
The solution is coded in **Python** (`main.py`). It strictly adheres to the class and method names defined in the design phase to ensure traceability.

## 4. Testing Plan
- **Test 1:** Deposit positive amount -> Balance increases.
- **Test 2:** Withdraw valid amount -> Balance decreases.
- **Test 3:** Withdraw invalid amount (Overdraft) -> Error message displayed.
