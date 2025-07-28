'''def fun(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
k = fun(name ='nani',Age =23)    
print(k)'''
        
 #working with List        
from collections import deque  #deque means double ended queue it works from both side of Queue

queue = deque()
#Enqueue-Add elements to the right - O(1)
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
#Dequeue(popleft)- remove element to the left - O(1)
print(queue.popleft())  #it prints first element from left side of queue
q2 = queue.pop()        #it prints last element in queue right side of queue
print(q2)
print(queue)
#print(queue[-1])        #peek element right side queue
#print(queue[0])         #peek element left side queue

'''#working Set 
from collections import deque
q = deque(set())
print(q,type(q))

q.append(10)    #deque([10])
q.append(20)    #deque([10,20])
q.append(30)    #deque([10,20,30])
print(q)

pl = q.popleft()   #10  it returns removed value
print(pl)

q.appendleft(40)    #deque([40, 20, 30])
print(q)

q.remove(40)        #deque([20, 30])
print(q)

b = deque(set())
b.append(1)     #deque([1, 20, 30])
b.append(2)     #deque([2, 1, 20, 30])
b.append(3)     #deque([3, 2, 1, 20, 30])

q.extendleft(b)  #deque([3, 2, 1, 20, 30])
print(q)

q.reverse()     #deque([30, 20, 1, 2, 3])
print(q)

#print(q.count(b))'''


#Example for Implementing a Queue
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        print(f'Enqueue item:{item}')
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f'Removed Item:{item}')
            return item
        print('Queue id empty!')
            
    def peek(self):
        if not self.is_empty():
            return self.queue[0] 
        return 'Queue is empty!'
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def display(self):
        print(f'Queue:{self.queue}')
        
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print('Peek:',q.peek())
q.dequeue()
q.dequeue()
q.dequeue()
print(q.is_empty())



#Example of Queue -> Print Job Scheduler

from collections import deque

job_queue = deque()

job_queue.append("A")
job_queue.append("B")
job_queue.append("C")

while job_queue:
    job = job_queue.popleft() #remove from left side or First element
    #job = job_queue.pop()     #remove from right side or Last element
    print(job)

print(job_queue) 