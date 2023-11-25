bank = {
    "transactions": [],
    "balance": 0
}

def bank_deposit(account, amount):
    if amount > 0: # Checking if deposit is greater than zero
        account['balance'] += amount
        account['transactions'].append(f"Deposit: ${amount}")
        print(f"Depositing ${amount}.\nNew balance is ${account['balance']}.\n")
    else:
        print("Invalid deposit amount.")

def bank_withdraw(account, amount):
    # if 0 < amount <= account['balance']:
    if amount > 0:
      if amount <= account['balance']:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawing ${amount}.\nNew balance is ${account['balance']}.\n")
      else:
         print(f"Excess withdrawal amount ${amount}. Balance is only ${account['balance']}")
    else:
        print(f"Withdrawal amount ${amount} cannot be less than $0.")


bank_deposit(bank, 1000)
bank_withdraw(bank, -10)

# Print transaction history
print("Transaction History:", bank['transactions'])
