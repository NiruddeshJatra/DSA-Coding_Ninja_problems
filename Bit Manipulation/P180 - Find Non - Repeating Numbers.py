# Time Complexity: O(n), where n is the length of the array.  
# - We traverse the array twice: once to compute the XOR of all elements and once to separate the elements based on the rightmost set bit.
# - Each traversal takes O(n).  
# - Total complexity is O(n).

# Space Complexity: O(1).  
# - We use only a few variables for computation, with no additional data structures.

# INTUITION:  
# The problem involves finding two unique non-repeating numbers in an array where every other number repeats exactly twice.  
# Using XOR, we can isolate the combined result of the two unique numbers (`temp` = x XOR y).  
# The rightmost set bit in `temp` helps us partition the numbers into two groups:  
# 1. Numbers with that bit set.  
# 2. Numbers without that bit set.  
# By XOR-ing each group separately, we recover the two unique numbers.

# ALGO:  
# 1. Compute the XOR of all elements in the array.  
#    - This gives `temp`, where `temp = x XOR y` (x and y are the two unique numbers).  
# 2. Find the rightmost set bit in `temp`.  
#    - This bit represents a difference between x and y.  
# 3. Partition the array into two groups based on the rightmost set bit.  
#    - Group 1: Numbers with that bit set.  
#    - Group 2: Numbers with that bit unset.  
# 4. XOR all numbers in each group to get the two unique numbers (x and y).  
# 5. Return the result as a list `[x, y]`.

def findNonRepeating(arr):
    temp = 0
    # Step 1: XOR all elements to get x XOR y
    for num in arr:
        temp ^= num

    # Step 2: Find the rightmost set bit in x XOR y
    right = temp & ~(temp - 1)

    # Step 3: Partition the array into two groups and find x and y
    x = y = 0
    for num in arr:
        if num & right:
            x ^= num  # XOR for the group with the set bit
        else:
            y ^= num  # XOR for the group without the set bit

    # Step 4: Return the two unique numbers
    return [x, y]

# Example Usage
# Input: arr = [4, 1, 2, 1, 2, 5]
# Output: [4, 5] (order may vary)
result = findNonRepeating([4, 1, 2, 1, 2, 5])
print(result)  # Output: [4, 5]
