#Bubble Sort is one of the most straightforward sorting algorithms.
# Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position.

def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]
    return array


#Bs = bubble_sort([5,3,4,2,1])
#arr = [5,3,4,2,1]
#print(bubble_sort(arr))




def bs(a):
    l = len(a)
    for i in range(l):
        for j in range(0,l-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

#aa = [7,4,2,5,3,1,0]
#print(bs(aa))



def Bs(arr):
    s = len(arr)
    
    for i in range(s):
        already_sorted = True
        for j in range(s-i-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
                
                already_sorted = False
        if already_sorted:
            break
    return arr

ss = [3,4,5,6,2,1]
print(Bs(ss))