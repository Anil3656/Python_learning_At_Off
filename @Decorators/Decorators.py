#What is a Decorator in Python?
#In Python, a decorator is a function that takes another function as input, adds some kind of functionality to it, and returns a new function without modifying the original function's code.

'''def hello():
    print("Hello World!")
#Creating a new object through function 
message = hello
message()'''


#Create an function 
def hello(fun):
    def inner():
        print("Hello!",end=" ")
        fun()
    return inner
def name():
    print("Anil")
#create an object and call function with another function
obj = hello(name)
obj()

#By using @ syntax 
import __main__
@hello
def name():
    print("AnilKumar")
    
if __name__ == "__main__":
    name()
    
#By wrapping sum_ab using All_sum function
def All_sum(func):
    def inner(a,b):
        print(f"{str(a)} + {str(b)} =", end=" ")
        return func(a,b)
    return inner
@All_sum
def sum_ab(a,b):
    add = a+b
    print(add)
    
if __name__ == "__main__":
    sum_ab(5,3)

#measuring the  execution time
import time   
def myFunction(n):
    time.sleep(n)
    
def measure_time(func):
    def wrapper(*args):
        t = time.time()
        res = func(*args)
        print("Function took " + str(time.time()-t) + " seconds to run")
        return res
    return wrapper
@measure_time
def myFunction(n):
    time.sleep(n)
    
if __name__ == "__main__":
    myFunction(2)


'''#1.Function Based Decorator:
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper
#With Using @ Syntax 
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#Without Using @ Syntax (Manual Way)
def say_hello():
    print("Hello!")

decorated = my_decorator(say_hello)
decorated()

#2.Decorator With Argument:
#Make the decorator customizable.
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)      #Here we are giving number that much times it will Print
def greet():
    print("Hi")
    
    
#3. Classed Based Decorator:
#Decorator implemented using a class with a __call__ method.
#Used when you need to maintain state or have more structured decorator
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

@Logger
def add(x, y):
    return x + y

#4. Built-in Decorators(standard Library):

#Decorator	        Use Case	                             Example
#@staticmethod	Declares a static method (no self)	        @staticmethod
#@classmethod	Method receives cls instead of self	        @classmethod
#@property	    Method as a read-only attribute	            @property


#5. Chained/Stacked Decorator:
#Applying multiple decorators on one function.
#Compose multiple functionalities (e.g., authorization + logging)

#@auth
#@log
def update():
    pass'''




