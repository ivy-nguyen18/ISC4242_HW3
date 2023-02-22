'''
Develop a function (and test how it works) that searches for the index of an element in an array of
integers, which is sorted, but the array values are not necessarily distinct.
If the element is not found in the array, the function must return -1.
If the element is found but there are multiple array values equal to the one, return the index of the first
occurrence of the element’s value in the array.,
The function must be a modification of the Binary Search algorithm.
Think how to keep the running time estimate as 𝑂(log 𝑛), where 𝑛 is the number of elements in the
array (non-empty array) even in case of many value repetitions in the array.
Let us call the function
get_index_sorted_non_unique(arr, elem)
'''

def get_index_sorted_non_unique(arr, elem):
    lo = 0
    hi = len(arr)-1

    while (lo <= hi):
        if lo > hi or lo < 0:
            return -1
        
        mid = lo + (hi - lo) // 2

        if arr[mid] == elem:
            if arr[mid - 1] != elem:
                return mid
            else:
                hi = mid - 1
                continue
        
        elif arr[mid] > elem:
            if lo < mid:
                hi = mid - 1
                continue
            else:
                return -1
        
        else:
            if mid < hi:
                lo = mid + 1
                continue
            else:
                return -1

arr = [-17, -10, -3, -3, -3, -3, -3, 10, 15]
#arr = [-17, -10, -3, 0, 0, 3, 5, 5, 10, 15]
#arr = []
x = -3
#x = 7
#x = 5
res_index = get_index_sorted_non_unique(arr, x)

if len(arr) == 0:
    print("Element not found. Right?")
elif res_index >= 0:
    print(f"The first occurence of the element {x} in the array has index {res_index}")
else:
    print(f"There is no element {x} in the array")