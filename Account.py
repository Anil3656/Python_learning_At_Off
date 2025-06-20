class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient Balance or invalid withdrawal amount.")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance:.2f}")


