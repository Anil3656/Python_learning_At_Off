#Recursion: Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem until it reaches a base condition that stops the recursive calls.

'''
🔄 Uses of Recursion

Breaking down complex problems into simpler sub-problems.

Solving problems that have inherent recursive structure, like:

    Tree traversal

    Graph traversal (DFS)

    Factorial calculation

    Fibonacci sequence

    Tower of Hanoi

Backtracking algorithms, such as:

    N-Queens

    Sudoku solver

Divide and Conquer techniques:

    Merge Sort

    Quick Sort

Mathematical computations, like permutations and combinations.'''


#Basic syntax Of Recursion 
def recursive_function(parameters):
    # Base case: condition to stop recursion
    if 'base_condition':
        return 'base_result'
    else:
        # Recursive case: function calls itself
        return recursive_function('modified_parameters')
    
    

n = 9 # int(input("Enter the n Value: ")) 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(n))


import sys
print(sys.getrecursionlimit())
#sys.getrecursionlimit(2000)


def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
    
lists = [1,2,3,4]
print(f'Sum of List elements: {sum_list(lists)}')

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
            
root = Node(10)
root.left = Node(5)
root.right = Node(15)


#Fibonacci series using Recursion 
'''in_order(root)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
print(fibonacci(4))
'''

'''
Using Iterative version

n = 5
a, b = 0, 1

#print(a)
if n > 0:
    print(a)
    print(b)
for _ in range(2, n + 1):
    a, b = b, a + b
    print(b)'''


def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(6))