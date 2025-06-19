#Type casting..................................................(22/04/2025)
'''#Other Type to Integer Type.................

#Float To Int with integer values
print(int(12.0))         
print(type(int(12.0)))

#Str To Int with integer values
print(int("123"))         
print(type(int("123")))

#Str To Int with String values
#print(int("abc"))   #Not possible
#print(type(int("abc")))   #ValueError: invalid literal for int() with base 10: 'abc

#Complex To Int with Complex values
#print(int(2j))
#print(type(int(2j)))   #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'''

'''#Other type To String Type..................

#Int To Str with Integer Values
print(str(123))         
print(type(str(123)))

#complex To Str with complex Values
print(str(12j))         
print(type(str(12j)))

#Bool To Str With Boolean Values
print(bool(True))         
print(type(bool(True)))

#Bool To Str Without Boolean Values
print(bool())         
print(type(bool()))'''

'''#Other Type To Float Type.................

#Int to Float with Interger Values
print(float(12))         
print(type(float(12)))

#Str to Float with String Values
print(float("12"))         
print(type(float("12")))

#Str to Float with String Values
#print(float("abd"))         
#print(type(float("abc")))   #ValueError: could not convert string to float: 'abd'

#complex to Float with complex Values
#print(float(12j))         
#print(type(float(12j)))  #TypeError: float() argument must be a string or a real number, not 'complex'''

'''#Other To Complex Type...................

#Int to Complex with Interger Values
print(complex(12))         
print(type(complex(12)))

#Float to Complex with Float Values
print(complex(12.0))         
print(type(complex(12.0)))

#Str to Complex with String Values
print(complex("12"))         
print(type(complex("12")))

#Str to Complex with String Values
#print(complex("abc"))         
#print(type(complex("abc")))  #ValueError: complex() arg is a malformed string'''

#Conditional Statements...................................................................

'''#If Condition and else Condition..........
x = int(input("Enter the Number: "))
if x%2 == 0:
    print("Even")
else:
    print("Odd")

if x in range(1,10):
    print("x Is between 1 to 10")
else:
    print("x Is not In Between 1 to 10")


#If, elif, else conditions...................
x = int(input("Enter the Number: "))
if x >= 18 and x <= 65:
    print("Eligible to vote")
elif x >= 65:
    print("Your a Senior Cetizen")
else:
    print("Your not eligible to vote")'''


'''#match Statement.............................

value = "rohan"

match value :
    case "rohan":
        print("rohan Present")
    case "Rakesh":
        print("Rakesh present")
    case "Nani":
        print("Nani Present")
    case _ :
        print("Your entered wrong Information")'''

#Looping Statements...........................................................

"""#For Loop.....................

for i in range(5):
    if i == 2:
        continue
    #print(i)

for i in range(5):
    if i == 2:
      break
    #print(i)

for i in range(5):
    if i == 2:
        pass
    #print(i)

for i in range(1,5):
    print("*")

#Neated for loop..............

for i in range(1,5):
    for j in range(1,5):
        print("*", end=" ")
    print()"""

'''#While Loop..................


x = 0
while x < 5:
    #print("Hi")
    x += 1 

    
x = input("Enter your name")
while x == "":
    print("You did't enter your name")
    x = input("Enter your name")
print(f"Hello {x}")'''


'''#Nested While loop.............................End Of the Day (22/04/2025)

i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print("*", end="  ")
        j += 1
    print()
    i += 1'''

#Patterns...............
'''for i in range():
    for j in range(5-i):
        print("*", end=" ")
    print()



n = 5
for i in range(1, n + 1):
    # First inner loop: print spaces
    for space in range(n - i):
        print(" ", end="")

    # Second inner loop: print numbers
    for num in range(1, i + 1):
        print("*", end=" ")

    print()
n = 5
for i in range(n):
    for space in range(i):
        print(" ",end="")
    for j in range(n - i):
        print("*",end="")
    print()'''

'''
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()


for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''


'''for i in range(n+1):
    print(' '*(n-i), '*'*(i))

n = int(input("Enter n value: "))
for i in range(n):
    print(' '*(i), '*'*(n-i))


for i in range(n):
    print("* "*(i), ' '*(n-i))

for i in range(n):
    print('  '*(n-i-1) + '* '*(i+1))


for i in range(n):
    print('  '* (n-i-1) + '* '* (i+1))

for i in range(n):
    print('* '* (i+1) + '  '* (n-i-1))


if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} Not a prime')
            break
    else:
        print(f'{n} Prime Number')
else:
     print(f'{n} Not a prime')'''


'''sum_sq = sum(i**2 for i in range(1,n+1))
print(sum_sq)


f = input('Enter the key: ')
if f == f[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')


n1 = int(input("Enter n value: "))
sum = n1*(n1+1)//2 
print(sum)

def countdown(n):
    print(n)
    if n == 0:
        return             # Terminate recursion
    else:
        countdown(n - 1)   # Recursive call

countdown(5)


n = int(input('Enter n value: '))

if n <= 0:
    print("Factorial does not exsit below 0")
else:
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    print(f'Factorial of {n} is: ',factorial)'''
'''


def function(a,b):
    c = a+b
    print('Sum of a+b is:',c)
    print()
    d = a-b
    print('Sub of a+b is:',d)
    e = a*b
    print('Mul of a+b is:',e)
    f = a//b
    print('Divi of a+b is:',f)
    g = a%b
    print('M-divi of a+b is:',g)
function(5,3)

#factorial of n numbers
n = int(input("Enter the n value: "))
fac = 1
if n < 1:
    print("Number should be positive!")
else:
    for i in range(1,n+1):
        fac = fac*i
print(f"Factorial of {n} is: ",fac)
'''





'''def fizzBuzz(A):
    result = []
    for i in range(1, A + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

fizzBuzz(5)'''

'''def fizzBuzz(A):
    result = []
    for i in range(1, A + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
print(fizzBuzz(10))

def fun(**kwargs):
    for key, val in kwargs.items():
        print("{} : {}".format(key, val))

fun(name ='ak',city ='hyd')
fun(name ='bk',city ='Nlr')'''



'''set1 = {1, 2, 4}
set2 = {4, 5, 6}
print(len(set1 + set2))'''

'''def fun(a,b):
    if a > b:
        return a
    else:
        return b

fun(30,20)
print(fun(20,30))

print((lambda a,b : a if a>b else b)(3,4))


class Human:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def greet(self):
        return f"Hello{self.name}!"

    def Age(self):
        return f"Your age is: {self.age}"
    def City(self):
        return f"Your city is: {self.city}"

Aneel = Human(' Ak',22,'Nellore')
print(Aneel.name)  #Here calling Object
print(Aneel.age)
print(Aneel.city)
print(Aneel.Age())   #Here calling Method or Function
print(Aneel.City())
Ani = Human(' Nani',23,'hyd')
print(Ani.name)
print(Ani.age)
print(Ani.city)
print(Ani.Age())
print(Ani.City())
print(Aneel.greet())
print(Ani.greet())'''

'''i = 0
while i <= 15:
    if i%2 != 0:
        print(i)
    i += 1'''

t = 'ABC'
n ='789'
print(t[2] + n[1])


n = 10
sqr = n**2
print(sqr)

for i in range(1,n+1):
    print(f'{n} X {i} = {i*n}')
    
    
def space_remove(str):
    result = ''
    for char in str:
        if char != " ":
            result += char
    return result

ip_str = "H e l l o W o r l d !"
get = space_remove(ip_str)
print(get)


A = 90
B = 969
C = 505

if A > B and A > C:
    print("A is largest:",A)
elif B > A and B > C:
    print("B is largest:",B)
else:
    print("C is largest:",C)
    
    
num = str("0")
count = 0
if num != 0:
    for n in num:
        count += 1
    print(type(count),count) 
print("Number is Zero!")


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 = "Hello! World$%$%"
result = ''
for char in str1:
    if char not in punctuations:
        result += char
print(result)


n = 1234
reverse = 0

while n != 0:
    digit = n % 10       #get the last element 
    reverse = reverse*10 +digit   #Multiply and add number
    n = n // 10                    #It remove the last element
print(reverse)
print(n)

f = "ma"

if f == f[ : :-1]:
    print("palindrome")
else:
    print("Not palindrome")
    
num = input("Enter a number: ")
if num == num[::-1]:                #In Python, this is called "slicing".
    print("Palindrome number")
else:
    print("Not a palindrome")