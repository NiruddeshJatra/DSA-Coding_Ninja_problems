def mergeSort(arr: [int], l: int, r: int) -> None:
    # Time Complexity: O(n*log(n))
    # Space Complexity: O(n) due to the temporary array used for merging
    
    # INTUITION:
    # This function implements the merge sort algorithm to sort the given list 'arr' in ascending order.
    # Merge sort works by recursively dividing the array into halves until each sub-array contains only one element,
    # and then merging the sorted sub-arrays to produce the final sorted array.
    
    # ALGORITHM:
    # 1. If the left index 'l' is greater than or equal to the right index 'r', return as the array is already sorted.
    # 2. Calculate the middle index 'mid' as the average of 'l' and 'r'.
    # 3. Recursively call mergeSort for the left half (from 'l' to 'mid') and the right half (from 'mid+1' to 'r').
    # 4. After both halves are sorted, merge them using the merge function.
    
    if l >= r:
        return
    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)

def merge(arr, l, mid, r) -> None:
    # Merge function to merge two sorted halves of the array
    
    # INTUITION:
    # This function merges two sorted halves of the array into a single sorted array.
    
    # ALGORITHM:
    # 1. Initialize two pointers 'index1' and 'index2' for the left and right halves respectively.
    # 2. Create a temporary array 'temp' to store the merged elements.
    # 3. While both halves have elements remaining:
    #     - Compare the elements at 'index1' and 'index2'.
    #     - Append the smaller element to 'temp' and move the corresponding pointer.
    # 4. Append any remaining elements from the left half (if any) to 'temp'.
    # 5. Append any remaining elements from the right half (if any) to 'temp'.
    # 6. Copy the merged elements from 'temp' back to the original array 'arr'.
    
    index1, index2 = l, mid + 1
    temp = []
    
    while index1 <= mid and index2 <= r:
        if arr[index1] < arr[index2]:
            temp.append(arr[index1])
            index1 += 1
        else:
            temp.append(arr[index2])
            index2 += 1
    
    if index1 <= mid:
        temp.extend(arr[index1 : mid + 1])

    if index2 <= r:
        temp.extend(arr[index2 : r + 1])

    for i in range(len(temp)):
        arr[l] = temp[i]
        l += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)  # Output: Sorted array: [5, 6, 7, 11, 12, 13]
