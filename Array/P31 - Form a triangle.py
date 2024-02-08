# Time Complexity: O(n log n), where n is the size of the input list 'arr' due to sorting.
# Space Complexity: O(1), constant space complexity.

# INTUITION:
# The function aims to determine whether it is possible to form a triangle using elements from the given list 'arr'.
# To form a triangle, the sum of the lengths of any two sides must be greater than the length of the third side.
# Therefore, the function first sorts the input list 'arr' in non-decreasing order.
# Then, it iterates through the sorted list from index 2 to len(arr) - 1.
# For each index 'i', it checks if the sum of the lengths of arr[i-1] and arr[i-2] is greater than arr[i].
# If this condition is true for any index 'i', it means it is possible to form a triangle, so the function returns True.
# If the loop completes without finding such an index, it means it is not possible to form a triangle, so the function returns False.

# ALGORITHM:
# 1. Sort the input list 'arr' in non-decreasing order.
# 2. Iterate through the sorted list from index 2 to len(arr) - 1:
#    - Check if arr[i-1] + arr[i-2] is greater than arr[i].
#    - If true, return True.
# 3. If the loop completes without finding such an index, return False.

def possibleToMakeTriangle(arr):
    arr.sort()  # Sort the input list in non-decreasing order
    for i in range(2, len(arr)):
        if arr[i - 1] + arr[i - 2] > arr[i]:
            return True
    return False
