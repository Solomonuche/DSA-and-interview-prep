"""
Quicksort  is a sorting algorithm that is based on divide and conquer algorithm
It pick an element as a pivot and partitions/groups the array such that all elements
less than the pivot comes before the pivot and elements graeter than the pivot 
comes after the pivot and then recursively sorts the individual subarray

The key process in quicksort is the partition(). The target of the partitions is to place the pivot
at th correct position in the sorted array and put all smaller elements to the left of the pivot
and all greater elements to the right of the pivot

Quicksort big O - best case O(nlogn), worst case O(n^2)
"""

def quicksort(arr, low, high):
    """
    Quicksort algorithm
    """

    if low < high:
        location = partition(arr, low, high)
        quicksort(arr, low, location - 1)
        quicksort(arr, location + 1, high)

def partition(arr, low, high):
    """
    sort an array
    """

    pivot = arr[low]
    pivot_index = low

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low = low + 1
        while arr[high] > pivot:
            high = high - 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[pivot_index], arr[high] = arr[high], pivot

    return high

arr = [5, 2, 6, 4, 9, 3]
low = 0
high = len(arr) - 1

quicksort(arr, low, high)
print(arr)