#Generators in Python are a powerful tool for writing memory-efficient code, especially when working with large datasets or streams of data.
#A generator is a special type of function that returns an iterator and allows you to iterate over data lazily,
#meaning it produces values one at a time only when requested, instead of computing them all at once and storing them in memory.
#It uses the yield keyword instead of return

# How Does a Generator Work?
'''
1.When you call a generator function, it doesn't execute immediately — it returns a generator object.
2.Each time you call next() on the generator:

    ->The function resumes from where it last left off (after yield).

    ->Executes code until the next yield.

    ->Returns the yielded value.
3.Once all yield statements are done, it raises a 'StopIteration' exception.'''

#🆚 Generator vs Normal Function:
'''
Feature	             Normal Function (return)	            Generator (yield)
----------------------------------------------------------------------------------
Returns	                A single value	                   An iterator (stream)
Execution	             All at once	                    One step at a time
Memory Usage	    High (stores all data)	              Low (yields one value)
Use case	            Simple results	                   Large data / streams'''

#Real-world Use Cases:
'''
1.Reading large files line-by-line: open(file), yield line
2.Infinite streams (e.g., prime numbers, Fibonacci)
3.Lazy evaluation for large datasets
4.Web scraping data chunk by chunk
5.Processing logs, streaming APIs'''



#Examples:
def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3
    
msg = greeting()
print(next(msg))
print(next(msg))
print(next(msg))
#print(next(msg))   #Exception will occurred After limit excide 'StopIteration'

'''
def countDown(n):
    count = 1
    while count <= n:
        yield count 
        count += 1

num  = countDown(3)
print(next(num))
print(next(num))
print(next(num))
#print(next(num))     #Once all yield statements are done, it raises a StopIteration exception.


def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

fib = fibonacci()
for _ in range(5):
    print(next(fib))



#Generator Expression
#A generator expression is an expression that returns a 'generator object'.

def squares(n):
    for i in range(n):
        yield i ** 2
    
square = squares(5)
for i in square:
    print(i)'''
    
    
#A generator expression provides you with a more simple way to return a generator object.
#A generator expression is like a list comprehension in terms of syntax. 

sqrt = (x**2 for x in range(5))
print(sqrt)
for i in sqrt:
    print(i)
    
List_sqrt = [x**2 for x in range(5)]
print(List_sqrt)
for list in List_sqrt:
    print(list)