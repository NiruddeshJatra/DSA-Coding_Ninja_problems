# Time Complexity: O(n log n), where n is the number of elements in the array.
# The array is recursively divided in half log(n) times, and merging the two halves takes O(n) time in each step.

# Space Complexity: O(n), because we need additional space for the temporary arrays used during the merging process.

# INTUITION:
# Inversion in an array occurs when two elements are out of order. In the context of an array `arr`, an inversion
# is defined as a pair `(arr[i], arr[j])` where `i < j` and `arr[i] > arr[j]`.
# The idea is to use the merge sort technique to count inversions efficiently. The merge step of merge sort is where 
# we detect and count the inversions across the left and right halves of the array.

# ALGO:
# 1. Split the array into two halves recursively using merge sort.
# 2. While merging two sorted halves, if an element from the left half is greater than an element from the right half,
#    this implies that all elements remaining in the left half form inversions with the current element from the right half.
# 3. Continue merging while counting the inversions and return the sorted array along with the inversion count.

def merge(arr1, arr2):
    cnt = 0
    l, r = 0, 0
    sortedArr = []
    
    # Merging two sorted arrays and counting inversions
    while l < len(arr1) and r < len(arr2):
        # If arr1[l] is less than or equal to arr2[r], it's not an inversion
        if arr1[l] <= arr2[r]:  
            sortedArr.append(arr1[l])
            l += 1
        else:
            # If arr1[l] > arr2[r], then arr1[l], arr1[l+1], ..., arr1[end] are all inversions with arr2[r]
            sortedArr.append(arr2[r])
            r += 1
            cnt += len(arr1) - l  # Add inversions with all remaining elements in arr1

    # Append remaining elements of arr1 or arr2
    sortedArr.extend(arr1[l:])
    sortedArr.extend(arr2[r:])
    
    return sortedArr, cnt


def mergeSort(arr):
    # Base case: if the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr, 0
    
    # Split array into two halves
    mid = len(arr) // 2
    left, leftInv = mergeSort(arr[:mid])  # Sort left half and count inversions
    right, rightInv = mergeSort(arr[mid:])  # Sort right half and count inversions
    
    # Merge sorted halves and count cross inversions
    mergedArr, crossInv = merge(left, right)
    
    # Total inversions = inversions in left half + inversions in right half + cross inversions
    totalInversions = leftInv + rightInv + crossInv
    
    return mergedArr, totalInversions


def getInversions(arr, n):
    # Step 1: Sort the array and count inversions using merge sort
    _, inversionCount = mergeSort(arr)  # We only care about the inversion count
    
    # Step 2: Return the total inversion count
    return inversionCount
