#Heap: A tree-based data structure in which the value of a parent node is ordered in a certain way with respect to the value of its child node(s). 
# A heap can be either a min heap (the value of a parent node is less than or equal to the value of its children) or a 
# max heap (the value of a parent node is greater than or equal to the value of its children).

'''✅ Real-Time Applications of Heap (Min-Heap / Max-Heap)
Priority Queues
→ Task scheduling, printers, network packet management

CPU Scheduling
→ Operating systems (Shortest Job First, Priority Scheduling)

Dijkstra’s Algorithm
→ GPS navigation, network routing

A* Algorithm (Path finding)
→ Game development, AI path finding

Heap Sort Algorithm
→ Efficient sorting with O(n log n) time complexity

Top-K Elements
→ Search engines (top results), analytics dashboards

Median in a Data Stream
→ Stock market feeds, real-time sensor monitoring

Garbage Collection
→ Memory management in Java, .NET

Event-Driven Simulations
→ Discrete event simulation (e.g., traffic, banks)

Load Balancing / Resource Allocation
→ Cloud computing, job scheduling on servers'''

'''📚 1. Heap (Min-Heap or Max-Heap):
|-------------------------------|-----------------------------------------------------|--------------------|
|       Operation	            |                Description	                      |    Time Complexity |
|-------------------------------|-----------------------------------------------------|--------------------|
|insert()	                    |     Add an element and maintain heap property	      |   O(log n)         |
|extract_min() / extract_max()  |	    Remove and return the root (min or max)	      |    O(log n)        |
|peek() / get_min() / get_max() |	    View the root element without removing it	  |     O(1)           |
|heapify()	                    |     Build a heap from an unsorted list	          |     O(n)           |
|replace()	                    |     Remove root and insert new element in one step  |	 O(log n)          |
|-------------------------------|-----------------------------------------------------|--------------------|'''


'''1. Insertion (Push)
Description: Adds a new element to the heap while maintaining the heap property.

How it works:
-> Add the element at the end of the heap (bottom-right of the tree).
-> "Bubble up" (heapify up) the element until the heap property is restored.'''
import heapq

heap = []
heapq.heappush(heap,(10,'first'))    #heappush(heap,(2,'First task'))
heapq.heappush(heap,(1,'first'))
heapq.heappush(heap,(11,'first'))
#heapq.heappush(heap,7)
#heapq.heappush(heap,5)
#heapq.heappush(heap,4)
#heapq.heappush(heap,2)
#heapq.heappush(heap,3)

print("Heap after insertions: ",heap)

while heap:
    priority, task = heapq.heappop(heap)
    print(f"Processing task: {task} (priority {priority})")


'''2. Deletion (Pop)
Description: Removes and returns the root element (min in min-heap, max in max-heap).

How it works:
-> Replace the root with the last element in the heap.
-> Remove the last element.
-> "Bubble down" (heapify down) the new root to restore the heap property.'''

import heapq

heap1 = [2,4,6]
print(heap1)
heapq.heapify(heap1)
min_ele = heapq.heappop(heap1)  #It removes the first element in Heap every time
print('Removed element: ',min_ele)
print(heap1)
min_ele = heapq.heappop(heap1)
print('Removed element: ',min_ele)
print(heap1) 


'''3. Peek (Access the smallest and largest element without removing)
Description: Returns the value at the root of the heap without removing it.'''

import heapq 

#Retrieving the smallest value in Heap
heap3 = [5,3,7,6]
print(type(heap3))
print('Before Heapify: ',heap3)
heapq.heapify(heap3)
print('After heapify: ',heap3)
print(type(heap3))
print('Smallest value in peek:',heap3[0])
min = min(heap3)
print('Smallest Value in Peek',min)

#Retrieving the largest value in Heap
heap4 = [5,3,7,6]
heapq.heapify(heap4)
max_ele = max(heap4)
heap4.remove(max_ele)
heapq.heapify(heap4)
print('Maximum element in Heap:',heap4[-1])  
print('Maximum element in Heap: ',max_ele)
print(heap4)

'''4.Replace Root Element (heapreplace)
Description: Used to replace root(first element) in heap'''

import heapq

heap = [-4,3,5]
heapq.heapify(heap)
print(heap)

root_ele = heapq.heapreplace(heap,6)
print(root_ele)
print(heap)



# Min-heap using heapq
tasks = []

# (priority, task name)
heapq.heappush(tasks, (2, "Write report"))
heapq.heappush(tasks, (1, "Fix bug"))
heapq.heappush(tasks, (3, "Email client"))

print(tasks)
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing task: {task} (priority {priority})")


# Min-heap using heapq inverted values
tasks = []

# (priority, task name)
heapq.heappush(tasks, (-2, "Write report"))
heapq.heappush(tasks, (-1, "Fix bug"))
heapq.heappush(tasks, (-3, "Email client"))

print(tasks)
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing task: {task} (priority {priority})") 