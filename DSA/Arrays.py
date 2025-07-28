'''my_list = [1,2,3,4,5]
print(my_list,type(my_list))

#Different Types of Importing And Creating An Array In Python 
import array
arr = array.array('i',[1,2,3,4,5])
print(arr[1:4:2])

import array as arr
arr1 = arr.array('i',[1,2,3,4,5])
print(arr1[1:4:2])

from array import *
a = array('d',[1,2,3,4,5,6,7])
print(a)

import numpy as np

np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr[2])  # Output: 3

#Operations In Arrays:-------------------------------------------------------------------------
#Accessing Array Elements

from array import *
a = array('i',[1,2,3,4,5,6,7])
print(a)     #Accessing complete array: array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
print(a[1])  #Accessing an Particular element in array Index: 2.0
print(a[2:5]) #Slicing an array
print(a[3:7:2])

print(len(a))  #Finding the length of the array using len() function

#Adding / Changing operations:----------------------------------------------------------------------
#1.Using array_Name.append() function we can add only one element in array
a.append(8)    #Here appending 8 into array
a.append(9)
a.append(10)
print(a)

#2.extend() function is used to Add more than one elements in array
a.extend([11,12,13])
print(a)

#3.insert() function is used to add an element in particular index position
#a.insert(Index,element)
a.insert(1,14)
print(a)

#Deleting and Removing the elements in array    
#array.pop() ->It remove the last element in the array #it returns removed values in Terminal window
#array.pop(3) ->It removes a particular index in array

print(a.pop()) 
print(a.pop(1))
print(a)

#The remove() function is used to remove the value where we do not need the removed value to be returned.
#array.remove(ele-value) ->This function takes the element value itself as the parameter.
a.remove(10)     
print(a)      # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12])

#Loop Through an array:--------------------------------------------------------------------------------------

for ele in a:      #Looping all elements
    print(ele)
for e in a[2:5]:   #Looping an Specific elements
    print(e)'''
    
    
    
#Example programs--------------------------
#Find the maximum number in array

import Arrays as arr
import array as arr
#Using max() in-built function
def max_num(arr):
    return max(arr)

m = arr.array('i',[1,2,3,4,5,6,9,7,8,8])
print(m)
print(max_num(m))

#Without using in-built function
def find_max(arr):
    if not arr:
        return None
    max_n = arr[0]
    for num in arr:
        if num > max_n:
            max_n = num
    return max_n

n =[15,25,35,45,55,65,75,85]
print(f'Max number is: {find_max(n)}')




#Find the min value in Array
#Using min() in-built function
def min_num(arr):
    return min(arr)

m = [1,2,3,4,5,6,9,7,8,8]
print(min_num(m))

#Without using in-built function
def find_min(arr):
    if not arr:
        return None
    min_n = arr[0]
    for num in arr:
        if num < min_n:
            min_n = num
    return min_n

n =[15,25,35,45,55,65,75,85]
print(f'Min value is: {find_min(n)}')




#Sum of an array[] using built-In function
def sum_of(arr):
    return sum(arr)

s = [10,20,30]
print(f'Sum of an array: {sum_of(s)}')

#Without built-In function
def sum_Of(a):
    if not a:
        return None
    sum = 0
    for num in a:
        sum += num
    return sum
s1 = [10,20,30,40]
print(f'Sum of array: {sum_Of(s1)}')


#Count the even number in Array
def count_even(arr):
    if not arr:
        return None
    count = 0
    for num in arr:
        if num%2 == 0:
            count += 1
    return count

e = [1,2,3,4,5,6,7,8,9,10]
print(f'even numbers: {count_even(e)}')

#Find even numbers in array
def even_num(arr):
    return sum([num for num in arr if num%2 == 0])

print(f'Even numbers are: {even_num(e)}')