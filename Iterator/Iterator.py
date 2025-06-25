#In Python, iterator and iterable are fundamental concepts used for looping over data structures like lists, tuples, sets, etc. 
# While they sound similar, they serve different purposes.

#Iterable:
#An iterable is any Python object capable of returning its members one at a time, allowing it to be looped over in a for loop.

#Examples of Iterables:
'''Lists: [1, 2, 3]
Tuples: (1, 2, 3)
Strings: "abc"
Sets: {1, 2, 3}
Dictionaries: {"a": 1, "b": 2}'''
#An iterable implements the __iter__() method which returns an iterator.

num = [1,2,3,4,5]
it = iter(num)
print(it)
for val in it:
    print(val)
    
#Iterator:
#An iterator is the object that actually performs the iteration — it keeps track of where it is in the iteration process.

#Implements two methods:
#__iter__() – returns the iterator object itself.
#__next__() – returns the next value from the iterable. If no more items, it raises StopIteration.

nums = [10,20,30,40]
it = iter(nums)
print(it)

print(next(it)) #10
print(next(it)) #20
print(next(it)) #30
print(next(it)) #40
#print(next(it))  #it raises the StopIteration Exception

#Difference Table:
'''
Feature	                Iterable	                        Iterator
Purpose	        To provide an iterator	         To fetch data one item at a time
Key Method	         __iter__()	                    __next__() and __iter__()
Usage	        Used with for loops	                    Used with next()
Returns     	Returns an iterator	             Returns next value or raises StopIteration
Examples	List, Tuple, Dict, Set, etc.	            Result of iter(iterable)  '''  

#Example:

class countDown:
    def __init__(self, start):
        self.num = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        val = self.num
        self.num -= 1
        return val
Count = countDown(5)
for val in Count:
    print(val)
    


class evenNumber:
    def __init__(self,n):
        self.n = n
        self.current = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        
        even = self.current
        self.current +=2
        return even

eve = evenNumber(10)
for e in eve:
    print(e)
        
        