def insertionSort(arr):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
    # INTUITION:
    # This function implements the insertion sort algorithm to sort the given list 'arr' in ascending order.
    # Insertion sort works by iterating through the list and repeatedly moving elements that are out of order
    # towards the beginning of the list until the entire list is sorted.
    
    # ALGORITHM:
    # 1. Iterate through each element in the list starting from the second element (index 1) using the loop variable 'i'.
    # 2. Within each iteration, initialize a pointer 'j' to the current index 'i'.
    # 3. While 'j' is greater than 0 and the element at index 'j' is less than the element at index 'j-1':
    #     - Swap the elements at index 'j' and index 'j-1' to move the out-of-order element towards the beginning of the list.
    #     - Decrement 'j' to continue checking and potentially swapping with previous elements.
    # 4. Repeat steps 2-3 until the entire list is sorted.
    
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Example usage:
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [5, 6, 11, 12, 13]
