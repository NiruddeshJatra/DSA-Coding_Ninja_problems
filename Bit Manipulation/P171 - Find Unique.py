# Time Complexity: O(n), where n is the size of the input array `arr`.  
# - We iterate through all the elements in the array once, performing a constant-time XOR operation for each element.  
# - Therefore, the time complexity is linear with respect to the size of the array.

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space, regardless of the input size.  
# - The variable `ans` is the only additional space required.

# INTUITION:  
# The XOR operation has the following properties:  
# 1. `a ^ a = 0`: XOR of a number with itself results in 0.  
# 2. `a ^ 0 = a`: XOR of a number with 0 results in the number itself.  
# 3. XOR is commutative and associative, meaning the order of operations does not matter.  

# Given an array where every element appears twice except for one, the XOR operation allows us to isolate the unique number.  
# When we XOR all elements together, pairs of duplicate numbers cancel each other out, leaving only the unique number.

# ALGO:  
# 1. Initialize a variable `ans` to 0.  
# 2. Iterate through each element in the array `arr`.  
# 3. XOR the current element with `ans` and update `ans` with the result.  
# 4. After completing the loop, `ans` will hold the unique number.  
# 5. Return `ans`.

import sys

def findUnique(arr, n):
    ans = 0
    for num in arr:
        ans ^= num  # XOR all elements in the array

    return ans
