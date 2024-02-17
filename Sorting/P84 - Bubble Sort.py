from typing import List

def bubbleSort(arr: List[int], n: int) -> None:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
    # INTUITION:
    # This function implements the bubble sort algorithm to sort the given list 'arr' in ascending order.
    # Bubble sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them
    # if they are in the wrong order.
    
    # ALGORITHM:
    # 1. Iterate through each element in the list using the outer loop variable 'i'.
    # 2. For each iteration of 'i', iterate through the elements starting from index 1 using the inner loop variable 'j'.
    # 3. Within the inner loop, compare the current element with its previous element.
    # 4. If the current element is smaller than its previous element, swap them to bring the smaller element towards
    #    the beginning of the list.
    # 5. Repeat steps 2-4 until the entire list is sorted.
    
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr, len(arr))
print("Sorted array:", arr)  # Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]
