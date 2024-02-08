# Time Complexity: O(n), where n is the size of the input list 'elements'.
# Space Complexity: O(m), where m is the number of leaders in the input list 'elements'.

# INTUITION:
# The function aims to find the leaders in the given list 'elements'.
# A leader is an element that is greater than all the elements to its right in the list.

# ALGORITHM:
# 1. Reverse the input list 'elements' to iterate from right to left.
# 2. Initialize the list 'leaders' with the last element of the reversed list.
# 3. Iterate through the reversed list (excluding the last element):
#    - If the current element is greater than the last leader in 'leaders', append it to 'leaders'.
# 4. Reverse the 'leaders' list to maintain the original order of leaders.
# 5. Return the list 'leaders'.

def findLeaders(elements, n):
    arr = elements[::-1]  # Reverse the input list
    leaders = [arr[0]]  # Initialize leaders list with the last element
    for i in arr[1:]:  # Iterate through the reversed list (excluding the last element)
        if i > leaders[-1]:  # Check if the current element is greater than the last leader
            leaders.append(i)  # If so, append it to 'leaders'
    return leaders[::-1]  # Reverse the 'leaders' list to maintain the original order

# Example usage:
elements = [16, 17, 4, 3, 5, 2]
n = len(elements)
print(findLeaders(elements, n))  # Output: [17, 5, 2]
