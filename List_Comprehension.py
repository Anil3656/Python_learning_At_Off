#List comprehension is a concise way to create lists in Python. 
# Instead of using loops like for or while, list comprehension lets you build lists in a single line using a readable and compact syntax.

#Syntax:
"[expression for item in iterable if condition]"

#Generating squares in traditional way.
squares  = []
for x in range(10):
    squares.append(x**2)
    #print(x,":",squares)
    
print(squares)

#Generating squares using Lambda Function
sqr = list(map(lambda x : x**2, range(10)))
print(sqr)

#Generating squares using List Comprehension
sqrt = [x**2 for x in range(10)]
print(sqrt)
sqrt = [x**2 for x in range(10) if x%2 == 0]
print(sqrt)
sqrt = [x**2 for x in range(10) if x%2 != 0]
print(sqrt)

#Using List Comprehension printing Un-Identical Pairs
print([(x,y) for x in [1,2,3] for y in [1,2,3] if x != y])

#Find even numbers using List comprehensions
even = [x for x in range(10) if x % 2 == 0]
print(even)

#List comprehensions on Dictionary
dict = {'name' : 'Anil', 'age' : 22, 'city' : 'Hyderabad'}
print(dict['name'])
l = [val for val in dict.items()]
print(l)

#Converting lower case to upper case using List comprehension
names = ['anil','rakesh','srinu']
name = [name.upper() for name in names]
print(name)

#Converting matrix form to normal list using list comprehension
matrix = [[1,2],[3,4],[5,6]]
normal = [name for row in matrix for name in row]
print(normal)