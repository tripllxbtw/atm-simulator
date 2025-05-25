# atm-simulator
# 🏦 ATM Simulator

This is a simple console-based ATM simulator written in Python.  
It allows users to log in with a PIN code and perform basic banking operations.

## 💡 Features

- PIN code verification (3 attempts)
- Deposit (limit: 10,000) with bonus every 3rd deposit (5%)
- Withdrawal (limit: 5,000, 1% commission)
- Transfer (limit: 15,000, 1% commission)
- Wealth tax (10%) if balance exceeds 5,000,000
- Change PIN code
- Transaction history
- Clear transaction history
- Operation limit: 10 per session

## 🚀 How to Run

1. Make sure you have Python installed
2. Save the script as `atm.py`
3. Run it using terminal:

```bash
python atm.py
