# Time Complexity: O(log(n)), where n is the input integer.  
# - In each iteration, the least significant set bit is cleared, which takes O(1) time.  
# - The number of iterations is equal to the number of set bits in `n`, which is at most log(n) for binary representation.

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space.  
# - Only the variables `count` and `n` are used.

# INTUITION:  
# The task is to count the number of set bits (1s) in the binary representation of the given integer `n`.  
# A simple way is to repeatedly clear the least significant set bit using the bitwise operation `n & (n - 1)`:
# - This operation clears the lowest set bit in `n` because subtracting 1 flips all bits from the least significant 1 to the end.
# - By repeatedly applying this operation and incrementing a counter, we efficiently count the set bits in `n`.

# ALGO:  
# 1. Initialize `count` to 0.  
# 2. While `n` is not zero:  
#    - Increment `count` by 1.  
#    - Use `n = n & (n - 1)` to clear the least significant set bit.  
# 3. Return the final value of `count`.

def countBits(n):
    count = 0  # Initialize count of set bits to 0

    # Loop until n becomes 0
    while n:
        count += 1  # Increment the count for each set bit
        n = n & (n - 1)  # Clear the least significant set bit

    return count  # Return the total count of set bits
