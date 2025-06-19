#creating and perform some operations
'''my_list = [24,20,14,15,35,30]
print(my_list)
my_list.append(10)
print(my_list)

my_list.insert(2,15)
print(my_list)

my_list.remove(10)
print(my_list)

a = my_list.index(20)
print(a)

my_list.sort(
print(my_list)

num = int(input("Enter the Number"))

if num == 0:
    print(f"{num} number is Zero")
elif num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


x = 10
print(type(x))

y = 'Anil'
print(type(y))

z = True
print(type(z))

a = 10.0
print(type(a))

b = 1j
print(type(b))

r = range(5)
print(type(r))


a = int(input("Enter the Number"))
b = int(input("Enter the Number"))

print((a^b))

x_int = 123
x_float = float(x_int)
print(x_float)
print(type(x_float))

x_float = 3.14
x_int = int(x_float)
print(x_int)
print(type(x_int))



x_list = [1,2,3]
x_tuple = tuple(x_list)
print(x_tuple)
print(type(x_tuple))


x_tuple = (1,2,3)
x_set = set(x_tuple)
print(x_set)
print(type(x_set))

x_set = {1,2,3}
x_list = list(x_set)
print(x_list)
print(x_list)

for i in [1,2,0,4,5]:
    if i == 0:
      continue
    else:
        print(i)

name = input("Enter your name: ")

while name == "":
    print('you did not enter your name')
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
s = ""
while age < 0:
    print("Age can't be negative")
    if age == int(s):
        age = int(input("Enter your age: "))
print(f"Your age is {age}")

food = input("Enter the food item you like (q to Quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter the another food item you like (q to Quit): ")
print("bye")

age = int(input("Enter your age: "))

while age > 18:
    print("Your are eligible for Vote")
    age = int(input("Enter your age"))
print("Your are not eligible for vote")

age = int(input("Enter your age: "))
if age > 18:
    print("Your are eligible for Vote")
else:
   print("Your are not eligible for vote")


#user-defined functions
def my_function(name):
    print(f"Hello {name}!")
my_function("Ak")

#Lambda functions
s = lambda x : x * x
print(s(2))

a = lambda a,b : a+b
print(a(5,5))


d = lambda x,y : x%y
print(d(10,2))

d = lambda x,y : x/y
print(d(10,2))

d = lambda x,y : x//y
print(d(10,2))


d = lambda x,y : x-y
print(d(10,2))

def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive case
print(factorial(7
                ))

#dictionaries
dicts = {
    "name" : "RR",
    "model": "R1B",
    "year": 1899,
    "service" : "Transport"
}

print(dicts)
print(dict["name"])
print(dicts["service"])
print(type(dicts))



n = int(input("Enter the number: " ))
if n > 1:
    for i in range(10,20):
        if n % i == 0:
            print("Is Not Prime Number")
            break
    else:
        print("Is Prime Number")
else:
    print("Is Not Prime Number")


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')'''

'''class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create nodes
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Preorder Traversal (Root -> Left -> Right)
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

print("Binary Tree (Preorder Traversal):")
preorder(root)'''

#Find the biggest number in list
'''list = [1,2,37,5,34,76,89,78,43,90,123,565,70]
max = max(list)
print('Largest number in List is: ',max)


max_dup = list[0]
for num in list:
    if num > max_dup:
        max_dup = num
print('Largest number in List is: ',max_dup)'''


'''
list = [5,6,2,4,2,8,3,1]
#list.sort()
#print('second largest number:',list[-2])
print(sorted(list))
print(max(list))
print(min(list))


start = int(input("Enter starting number: "))
end = int(input("Enter Ending number: "))
sum = 0
for i in range(start,end+1):
    sum += i
print(sum)'''

'''def two_sum(nums,target):

    for i  in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return 'Target not Reached!'

print(two_sum([2,4,6,2],6))'''

'''#Check Valid Peranthases
class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

sol = Solution()
print(sol.isValid('({})'))'''


'''n =int(input('Enter n value: '))
if n < 0 :
    print('Negative')

elif n > 0:
    print('Positive')

else:
    print('Zero')'''


#Use a for loop to print even numbers from 2 to 20.

'''for i in range(2,20):
    if i%2 == 0:
        print(i)'''

'''
i = 1
while i <= 15:
    if i%2 != 0:
        print(i)
        i += 1'''

'''n =10
val = [i for i in range(n)]
for num in val:
    if num%2 == 0:
        print(num,end=" ")  


print(2**9)
print("/\\/\\/\\/\/\\/\\/\/\\/\\/\\/\\/\\/\\")   #one slash and two back slash required 
name = 'AnilKumar'
print(name[2:8:2])

dict = {'name' : 'Anil', 'age' : 23,'name':"rahul"}  #Here duplicate values are not allowed in dictionary 
print(len(dict)) #output: 2

a = [1,3,2]
b= [4,5,6]
print(a+b)
print(list(zip(a,b)))'''


def create_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

print(create_list(5))

l = create_list(4)
print(l)