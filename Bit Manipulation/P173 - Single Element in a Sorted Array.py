# Time Complexity: O(n), where n is the size of the input array `arr`.  
# - We traverse the array once, performing a constant-time XOR operation for each element.  
# - Hence, the time complexity is linear.

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space.  
# - The variable `ans` is the only additional storage required.

# INTUITION:  
# The problem is to find the single non-duplicate element in an array where every other element appears exactly twice.  
# Using the XOR operation provides an efficient way to solve this problem:  
# - XORing a number with itself results in 0 (`x ^ x = 0`).  
# - XORing a number with 0 results in the number itself (`x ^ 0 = x`).  
# - XOR is commutative and associative, so the order of operations does not matter.  
# By XORing all elements in the array, the duplicate elements cancel out, leaving only the single non-duplicate element.

# ALGO:  
# 1. Initialize `ans` to 0.  
# 2. Traverse the array and XOR each element with `ans`.  
# 3. At the end of the traversal, `ans` will contain the single non-duplicate element.

def singleNonDuplicate(arr):
    ans = 0  # Variable to store the result

    # Traverse the array and XOR all elements
    for num in arr:
        ans ^= num

    return ans  # Return the single non-duplicate element
