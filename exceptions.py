'''An exception in Python is an error that occurs during the execution of a program.
 When Python encounters an error that it cannot handle, it raises an exception. 
 If the exception is not caught (handled), the program will terminate.
Exceptions are different from syntax errors. A syntax error occurs when Python code is not written correctly. 
Exceptions, on the other hand, happen during the execution of syntactically correct code.


'Exception	'                               ' Description'
ZeroDivisionError	 ----->      Raised when a number is divided by zero.
TypeError	         ----->      Raised when an operation is applied to an object of inappropriate type.
ValueError	         ----->      Raised when a function receives an argument of the right type but inappropriate value.
IndexError	         ----->      Raised when a sequence subscript is out of range.
KeyError	         ----->      Raised when a dictionary key is not found.
FileNotFoundError	 ----->      Raised when a file or directory is requested but doesn’t exist.
AttributeError	     ----->      Raised when an invalid attribute reference is made.
ModuleNotFoundError	 ----->      Raised when an import statement fails to find the module definition.
NameError	         ----->      Raised when a local or global name is not found.
IndentationError	 ----->      Raised when indentation is incorrect.
StopIteration	     ----->      Raised to indicate the end of an iterator.
RuntimeError	     ----->      Raised when an error is detected that doesn’t fall in any other category.
MemoryError	         ----->      Raised when an operation runs out of memory.
AssertionError	     ----->      Raised when an assert statement fails.'''



'''#ZeroDivisionError....................................
#div = a / b
#print(div)

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
try:
    div = a / b
    print(div)
except ZeroDivisionError:
    print('Zero Division Error Ocurred')

            #OR
try:
    div = a / b
    print(div)
except ZeroDivisionError as m:
    print('Zero Division Error Ocurred',m)'''

'''#TypeError................................................
a = input('Enter a value: ')
b = int(input('Enter b value: '))
#print(a+b)              TypeError: can only concatenate str (not "int") to str

try:
    print(a+b)
except TypeError as e:
    print("Type error ocurred",e)
else:
    print('No error ocurred')
finally:
    print('Finally block cleared!')'''

'''#ValueError.................................................
#number = int('abc')
#print(number)   ValueError: invalid literal for int() with base 10: 'abc'
try:
    number = int('abc')
    print(number)
except ValueError as v:
    print('Value error ocurred',v)'''


'''#IndexError...................................................
my_list =[1,2,3,4]
#print(my_list[10])  IndexError: list index out of range

try:
    print(my_list[10])

except IndexError as i:
    print('Index error ocurred',i)'''

"""#KeyError.............................................

my_dict ={
    'name' : 'Rohan',
    "age" : 23,
    'city' : 'Hyderabad'
}
#print(my_dict['class'])    KeyError: 'class'

try:
    print(my_dict['class'])
except KeyError as k:
    print('Key error ocurred',k)"""


'''#FileNotFoundError......................................

try:
    with open(DailyUpdatesonPythonSession.txt) as file:
        content = file.read()
except FileNotFoundError as fnf:
    print('File not found error: ',fnf)'''


'''#AttributeError..............................................

#x = 10
#x.append(5)         AttributeError: 'int' object has no attribute 'append'

try:
    x = 10
    x.append(5) 
except AttributeError as a:
    print('Attribute error: ',a)'''

'''#ModuleNotFoundError.................................................

#import file_ll 
try:
    import non_existing_module
except ImportError as e:
    print("Module import failed:", e)
'''

'''#NameError....................................

try:
     print(abc)       #NameError: name 'abc' is not defined
     print(int('abc'))
except NameError as n:
     print('NameError:',n)'''


'''#write a program demo for multiple exceptions
my_list = [1,2,3,4]
try:
    print(10/0)
    num = int('abc')
    print(num)
    print(my_list[5])
    print('abb'+123)

except:                     
     print('multiple exceptions are Handled')'''
'''
abc = 'a'
print(type(abc))
my_list = [1,2,3]
print(my_list[10])'''

a = input('Enter a value: ')
b = int(input('Enter b value: '))
#print(a+b)             

try:
    print(a+b)
except TypeError as e:
    print("Type error ocurred",e)
else:
    print('No error ocurred')
finally:
    print('Finally block cleared!')

number = int('123')
#print(number)

my_list = [1,2,3,4]
print(my_list[1])
#print(my_list[5])

x = 10
x.append()
print(x)


