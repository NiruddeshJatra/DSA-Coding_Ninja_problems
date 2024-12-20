# Time Complexity: O(1).  
# - The bitwise operation `1 << (k - 1)` and the bitwise AND (`n & (1 << (k - 1))`) are constant time operations.  
# - Therefore, the overall time complexity is O(1).

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space for variables and computations.  

# INTUITION:  
# To check if the k-th bit of a number `n` (1-based indexing) is set (i.e., equal to 1),  
# we can use a bitwise AND operation between `n` and a number where only the k-th bit is set.  
# For example:  
# - If k = 3, then `1 << (k - 1)` shifts the number `1` two places to the left, creating a binary mask `00000100`.  
# - The bitwise AND between `n` and this mask keeps only the k-th bit of `n`, clearing all other bits.  
# - If the result is non-zero, the k-th bit is set; otherwise, it is not.

# ALGO:  
# 1. Create a mask by left-shifting `1` by `k - 1` positions (`1 << (k - 1)`).  
# 2. Perform a bitwise AND operation between `n` and the mask (`n & (1 << (k - 1))`).  
# 3. If the result is non-zero, return `True` (the k-th bit is set).  
#    Otherwise, return `False` (the k-th bit is not set).  

def isKthBitSet(n: int, k: int) -> bool:
    # Check if the k-th bit is set using a bitwise AND operation
    if n & (1 << (k - 1)):
        return True
    return False
