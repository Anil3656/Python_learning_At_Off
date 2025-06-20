from Account import BankAccount

# Create two bank accounts
account1 = BankAccount('Anil',2000)
account2 = BankAccount("Bob", 500)

# Perform transactions
account1.deposit(int(input('Enter Amount To Deposit:')))
account1.withdraw(int(input('Enter Amount to Withdraw:')))

# Display final balances
account1.display_balance()
account2.display_balance()