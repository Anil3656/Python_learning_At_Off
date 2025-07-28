#Insertion Sort
#Insertion Sort builds the final sorted array one element at a time by inserting each element into its correct position within the sorted part of the array.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j],arr[j - 1] = arr[j - 1],arr[j]
            j -= 1
            
            

a = [4,5,3,2,1]
insertion_sort(a)
print(a)



def In_sort(a):
    
    for i in range(1,len(a)):
        key_value = a[i]
        j = i - 1
        
        while j >= 0 and a[j] > key_value:
            a[j + 1] = a[j]
            j  -= 1
            
            a[j + 1] = key_value
    return a

c = [2,4,5,1,3]
print(In_sort(c))