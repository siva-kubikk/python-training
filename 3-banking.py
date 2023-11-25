bank = {
    "transactions": [],
    "balance": 0
}

def bank_deposit(account, amount):
    if amount > 0:
        account['balance'] += amount
        account['transactions'].append(f"Deposit: ${amount}")
        print(f"Depositing ${amount}.\nNew balance is ${account['balance']}.\n")
    else:
        print("Invalid deposit amount.")

def bank_withdraw(account, amount):
    if 0 < amount <= account['balance']:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawing ${amount}.\nNew balance is ${account['balance']}.\n")
    else:
        print("Invalid or excessive withdrawal amount.")


bank_deposit(bank, 1000)
bank_withdraw(bank, 5000)

# Print transaction history
print("Transaction History:", bank['transactions'])
