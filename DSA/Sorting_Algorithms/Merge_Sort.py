#A divide-and-conquer algorithm that divides the list into two halves, recursively sorts each half, and then merges the sorted halves.

#Time Complexity: O(n log n) in all cases.

#Space Complexity: O(n) auxiliary space.
#Use Case: Ideal for large datasets and external sorting (sorting data that doesn't fit into memory).

#Example 

def merge(left, right):
    
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left
    
    
    result = []
    index_left = index_right = 0
    
    
    while len(result) < len(left) + len(right):
        
        if left[index_left] <= right[index_right]:    #condition for Ascending Order  O/P: [1, 2, 4, 5, 6]
        #if left[index_left] >= right[index_right]:   #Condition for Descending order O/P: [6, 5, 4, 2, 1]
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def m_sort(array):
    
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2 
    
    return merge(
                m_sort(array[:midpoint]),
                m_sort(array[midpoint:]))
 
#arr = [1]   
#arr = [2,1]   
arr = [4,5,2,6,1]
#arr = 1 -------------------> TypeError because here i giving array type data  instead of int data type are given 
print(m_sort(arr))