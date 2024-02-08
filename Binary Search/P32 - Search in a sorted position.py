# Time Complexity: O(log n), where n is the length of the input list 'arr'.
# Space Complexity: O(1), constant space complexity.

# INTUITION:
# The function aims to find the index where the given integer 'm' should be inserted into the sorted list 'arr'.
# It uses binary search to efficiently find the correct insertion position.

# ALGORITHM:
# 1. Initialize two pointers 'l' and 'r' representing the left and right boundaries of the search range, respectively.
# 2. While 'l' is less than or equal to 'r':
#    - Calculate the middle index 'mid' as the average of 'l' and 'r'.
#    - If 'm' is greater than the value at 'arr[mid]', update 'l' to 'mid + 1'.
#    - If 'm' is less than the value at 'arr[mid]', update 'r' to 'mid - 1'.
#    - If 'm' is equal to the value at 'arr[mid]', return 'mid'.
# 3. If the loop completes without finding 'm', return 'l', which represents the correct insertion position.

def searchInsert(arr: [int], m: int) -> int:
    l, r = 0, len(arr) - 1  # Initialize left and right boundaries
    while l <= r:
        mid = (l + r) // 2  # Calculate middle index
        if m > arr[mid]:
            l = mid + 1  # Update left boundary
        elif m < arr[mid]:
            r = mid - 1  # Update right boundary
        else:
            return mid  # Return index if 'm' is found
    return l  # Return left boundary if 'm' is not found

# Example usage:
arr = [1, 3, 5, 6]
m = 5
print(searchInsert(arr, m))  # Output: 2 (Index where 5 should be inserted to maintain sorted order)
