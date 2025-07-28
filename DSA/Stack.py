#A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
#🔁 How Does a Stack Work?
   # ->The last element added (pushed) to the stack is the first one removed (popped).
   # ->Think of it like a stack of plates: you can only take the top plate off or add a new plate on top.



#Working with list sequence data type
stack = []
print(type(stack))
stack.append(10)  #push operation
stack.append(20)
stack.append(30)
print(stack)

print('Last number:',stack[-1])  #peek retrieves top element without removing it
print(stack[0])

p1 = stack.pop() #30
p2 = stack.pop() #20
p3 = stack.pop() #10
print(p1)
print(stack)

if stack:
   print(True)
else:
    print(False)

    
#working with set() = {} sequence data type
print('\//\//\//\//\//\//\//\//\//\//\//\//\//')
stack = set([])
stack = []
print(type(stack))

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

#Example for Stack implementation
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):    #Add item top of stack
        self.stack.append(item)
        print(f'Pushed item:{item}')
        
    def pop(self):           #remove item top of stack
        if not self.is_empty():
            item =self.stack.pop()
            print(f'removed Item:{item}')
            return item
        return "Stack is Empty!"
        
    def peek(self):         #view the top item without removing 
        if not self.is_empty():
            return self.stack[-1]
        print('Stack is Empty!')
               
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print(f'Stack: {self.stack}')
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
print(f'Peek:{s.peek()}')

s.pop()
#s.pop()
s.pop()
s.display()
print(s.is_empty())


#Example for Stack
#Balanced Parentheses Checker

def balance(exp):
    stack = []
    for char in exp:
        if char in "{([":
            stack.append(char)
        elif char in "])}":
            if not stack:
                return False
            top = stack.pop()    
            if (top,char) not in [('(', ')'), ('{', '}'), ('[', ']')]:
                return False
    return not stack

i = balance("{([])}")
print(i)

i1 = balance("{([)])}")
print(i1)