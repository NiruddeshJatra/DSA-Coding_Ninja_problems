# Time Complexity: O(n), where n is the size of the input list 'arr' in the worst-case scenario.
# Space Complexity: O(1), constant space complexity.

# INTUITION:
# The function aims to find the starting and ending indices of the target value 'x' in the sorted list 'arr'.
# It uses a two-pointer approach to traverse the list from both ends towards the center.
# The 'start' pointer starts from the beginning of the list, and the 'end' pointer starts from the end of the list.
# The function updates the 'start' pointer while the element at 'start' is not equal to 'x' and updates the 'end' pointer while the element at 'end' is not equal to 'x'.
# If both pointers encounter the target value 'x', it returns the indices of the first and last occurrences of 'x'.
# If the pointers meet or 'start' becomes greater than 'end' without finding 'x', it returns [-1, -1] to indicate that 'x' is not found in the list.

# ALGORITHM:
# 1. Initialize 'start' to 0 and 'end' to len(arr) - 1.
# 2. While 'start' is less than 'end':
#    - If arr[start] is not equal to 'x', increment 'start'.
#    - If arr[end] is not equal to 'x', decrement 'end'.
#    - If arr[start] is equal to 'x' and arr[end] is equal to 'x', return [start, end].
# 3. If 'start' becomes greater than 'end' or the pointers meet without finding 'x', return [-1, -1].

def searchRange(arr: [int], x: int) -> [int]:
    start, end = 0, len(arr) - 1
    
    while start < end:
        if arr[start] != x:
            start += 1
        if arr[end] != x:
            end -= 1
        if arr[start] == x and arr[end] == x:
            return [start, end]
    
    return [-1, -1]
