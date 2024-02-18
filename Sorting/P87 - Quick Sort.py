from typing import List

# Time Complexity: O(n log n) in average case, O(n^2) in worst case
# Space Complexity: O(log n) in average case (for the recursive call stack), O(n) in worst case

# INTUITION:
# QuickSort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array
# and partitioning the other elements into two sub-arrays according to whether they are less than or greater
# than the pivot. The sub-arrays are then recursively sorted. This process repeats until the entire array is sorted.

# ALGO:
# 1. INITIALIZE a function partition to select a pivot and partition the array.
# 2. RECURSIVELY SORT the sub-arrays before and after the pivot.

def partition(arr: List[int], start: int, end: int) -> int:
    pivot = arr[start]
    i, j = start, end
    while i < j:
        while i < end and arr[i] <= pivot:
            i += 1
        while j > start and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quickSort(arr: List[int], start: int, end: int) -> None:
    if start < end:
        pivotIndex = partition(arr, start, end)
        quickSort(arr, start, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, end)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quickSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
