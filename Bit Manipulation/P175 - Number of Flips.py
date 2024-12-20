# Time Complexity: O(log(n)), where n is the result of `a ^ b`.  
# - In each iteration, the least significant set bit in `res` is cleared, which takes O(1) time.  
# - The number of iterations is equal to the number of set bits in `res`, which is at most log(n).

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space.  
# - Only the variables `res` and `count` are used.

# INTUITION:  
# The task is to find the minimum number of bit flips required to convert the integer `a` to `b`.  
# By using the XOR operation `a ^ b`, we identify all positions where the bits of `a` and `b` differ:  
# - The result of `a ^ b` has a 1 in every position where `a` and `b` have differing bits.  
# To count the differing bits, we use the bitwise operation `res & (res - 1)`:
# - This operation clears the least significant set bit in `res` in each iteration.  
# - By incrementing a counter for each cleared bit, we can efficiently count the total number of differing bits.

# ALGO:  
# 1. Compute `res = a ^ b`, which gives the positions of differing bits.  
# 2. Initialize `count` to 0.  
# 3. While `res` is not zero:  
#    - Increment `count` by 1.  
#    - Use `res = res & (res - 1)` to clear the least significant set bit.  
# 4. Return the final value of `count`.

def numberOfFlips(a: int, b: int) -> int:
    res = a ^ b  # XOR to find differing bits
    count = 0    # Initialize count of differing bits to 0

    # Loop until res becomes 0
    while res:
        res &= res - 1  # Clear the least significant set bit
        count += 1      # Increment the count for each set bit

    return count  # Return the total count of differing bits
