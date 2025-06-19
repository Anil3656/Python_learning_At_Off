#Functions in Python Program
#User Defined functions

'''#function without parameters and Arguments
def function1():
    print('Hi everyone!')

function1()

#function with parameters and Argumrnts
def sum(a,b):
    add = a+b
    return add

total = sum(10,20)
print(total)

#Function with multiple parameters and arguments

def multi_function(*n):
    result = sum(n)
    return result
total_sum = multi_function(1,2,3,4,5)
print(total_sum)

#Function with multiple parameters and arguments but adding another parameter infront

def multi_function(a,b,*n):
    result = sum(n)
    return result
total_sum = multi_function(1,2,3,4,5)
print(total_sum)

#Function with multiple parameters and arguments but adding after Nth parameter


def multi_function(*n,a=4):
    result = sum(n)
    return result
total_sum = multi_function(1,2,3,4,5)
print(total_sum)


#Variables......................................

#Gobal Varaible
name = 'Jhon'
def fun_1(name):
    print('hi',name)
def fun_2(name):
    print('How are',name)
def fun_3(name):
    print('What is going on',name)

fun_1(name)
fun_2(name)
fun_3(name)

#Local Variable
def function1():
    name = 'Ak'
    print('Hello!',name)
function1()

#Not possible to access name variable in function1 bcz it is Local variable
def funct1():
    print(name)
funct1()'''

#Non-Local Varaiable
#3.write a program to perform arithmetic operations using nested functions
'''def func1(a,b):
    sum = a+b
    print('sum of two numbers:',sum)
    def func2(a,b):
        sub = a-b
        print('Subraction of two numbers:',sub)
        def func3(a,b):
            mul = a*b
            print('Multiplication two numbers:',mul)
            def div(a,b):
                divi = a//b
                print('Division of two nubers:',divi)
                def mod(a,b):
                    mod = a%b
                    print('Modulo division of two numbers:',mod)
                mod(10,20)
            div(10,20)
        func3(2,5)
    func2(10,20)
func1(10,20)



#1.write a program demo for global variables.To modify the global variable value
name = "pk"

def function1():
    global name 
    name = 'Ak'

function1()
print('Hello!',name)

#2.write a program demo for *arguments

def multi_function(*argu):
    result = sum(argu)
    return result
total_sum = multi_function(1,2,3,4,5)
print(total_sum)'''

#4.write a program to perform bank operations 
'''->account_create()
->deposit()
->withdraw()
->check_balance()
->display_account_info()'''

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generated_ac_num()

    def generated_ac_num(self):
        # A simple method to generate a random account number for simplicity
        import random
        return random.randint(1000000000, 9999999999)

    def account_create(self):
        print(f"Account created successfully for {self.account_holder}.")
        print(f"Account Number: {self.account_number}")
        print(f"Initial Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}")
            print(f"New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}")
            print(f"New Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_account_info(self):
        print("\nAccount Information:")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")


# Main program to test the BankAccount class

# Create an account for a user
account_holder_name = input("Enter the account holder's name: ")
initial_balance = float(input("Enter the initial balance: ") or 0)

account = BankAccount(account_holder_name, initial_balance)
account.account_create()

# Deposit money
deposit_amount = float(input("\nEnter the amount to deposit: "))
account.deposit(deposit_amount)

# Withdraw money
withdraw_amount = float(input("\nEnter the amount to withdraw: "))
account.withdraw(withdraw_amount)

# Check balance
account.check_balance()

# Display account information
account.display_account_info()


#find the factorial of given range
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Print factorial for each number in range
for num in range(start, end + 1):
    print(f"Factorial of {num} is {factorial(num)}")