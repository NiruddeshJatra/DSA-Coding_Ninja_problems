from typing import List

def selectionSort(arr: List[int]) -> None:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
    # INTUITION:
    # This function implements the selection sort algorithm to sort the given list 'arr' in ascending order.
    # Selection sort works by repeatedly finding the minimum element from the unsorted part of the list
    # and moving it to the beginning of the unsorted part.
    
    # ALGORITHM:
    # 1. Iterate through each element in the list using the outer loop variable 'i'.
    # 2. For each iteration of 'i', iterate through the elements starting from index 'i' using the inner loop variable 'j'.
    # 3. Within the inner loop, find the index of the minimum element in the unsorted part of the list.
    # 4. Swap the current element at index 'i' with the minimum element found in step 3, if necessary.
    # 5. Repeat steps 2-4 until the entire list is sorted.
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

# Example usage:
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [11, 12, 22, 25, 64]
