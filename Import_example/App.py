from Addition import add
from Subraction import sub
from Multiplecation import mul



#from Bank_Operations import Operations
#print(Operations.account1.balance())
add = add(10,20)
print(add)

sub = sub(20,30)
print(sub)

mul = mul(20,10)
print(mul)

import Bank_Operations.Account
from Bank_Operations.Account import BankAccount
#from Bank_Operations.Operations import account1, account2

account1 = BankAccount('Anil',2000)

Bank_Operations.Account.BankAccount.deposit(account1,1000)
print(Bank_Operations.Account.BankAccount.display_balance(account1))