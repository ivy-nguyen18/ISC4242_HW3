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