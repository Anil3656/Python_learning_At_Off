#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#Syntax:  
'lambda arguments : expression'

x = lambda x : x + 5
print(x(5))

x = lambda x : x**2
print(x(1))
print(x(10))
print(x(20))

y = lambda a,b : a*b
print(y(10,10))

y = lambda a,b,c : a+b+c
print(y(10,20,30))

def sum(a,b):
    x = lambda a,b : a+b
    print(x(a,b))
    
print(sum(10,20))

def summ(n):
    for i in range(1,n):
        x = lambda i: i * 10
        print(x(i))
        
print(summ(5))


def fuc(a):
    return lambda a : a * 2

print(fuc(2)(2))    #When ever the lambda function in return we have to give two arguments


def fun(n):
    return lambda a : a * n

md = fun(2)
print(md(10))


def mul(a,b):
    return lambda a,b : a * b

fun2 = mul(10,2)
print(fun2)
print(fun2(1,2))

'''def check(age):
    if age < 0:
        raise ValueError (" Age Can't be Negative!")    #Raising My own Exception

print(check(-1))'''


