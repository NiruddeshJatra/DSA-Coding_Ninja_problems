# Time Complexity: O(log(n)), where n is the input number.  
# - The algorithm iterates through 32 bits (or log2(n) bits for smaller numbers), calculating the number of set bits contributed by each bit position.  
# - Each iteration involves constant-time arithmetic operations.

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space.  
# - Variables `totalCount`, `cycleLength`, `fullCycle`, `remaining`, and `currentCount` are reused.

# INTUITION:  
# To efficiently count the total number of set bits in all integers from 1 to n,  
# we exploit the repeating pattern in binary representation:  
# - For a given bit position i, the bit toggles between 0 and 1 every `2^(i+1)` cycles.  
# - The contribution of this bit to the total count can be calculated using the number of complete cycles and the remaining numbers in the last incomplete cycle.  
# By iterating through all 32 bits (for 32-bit integers), we accumulate the contributions from each bit position.

# ALGO:  
# 1. Initialize `totalCount` to 0 and set `MOD` to 10^9 + 7 to handle large numbers.  
# 2. For each bit position `i` from 0 to 31:  
#    - Calculate the cycle length for this bit as `2^(i+1)`.  
#    - Determine the number of full cycles within the range 1 to n as `n // cycleLength`.  
#    - Find the remaining numbers after the full cycles as `n % cycleLength`.  
#    - Compute the contribution of this bit position:  
#      - Bits set in full cycles: `fullCycle * (cycleLength // 2)`.  
#      - Bits set in the remaining part: `max(0, remaining - (cycleLength // 2) + 1)`.  
#    - Add the current bit's contribution to `totalCount`, ensuring the result is modulo `MOD`.  
# 3. Return `totalCount` as the final result.

def countSetBits(n):
    totalCount = 0  # Initialize total count of set bits
    MOD = 10**9 + 7  # Modulo value to handle large numbers

    # Loop through all 32 bit positions
    for i in range(32):
        cycleLength = 1 << (i + 1)  # Length of one cycle for the i-th bit
        fullCycle = n // cycleLength  # Number of complete cycles in the range [1, n]
        remaining = n % cycleLength  # Remaining numbers after the last complete cycle

        # Count set bits contributed by this bit position
        currentCount = fullCycle * (cycleLength // 2) + max(0, remaining - (cycleLength // 2) + 1)

        # Update the total count modulo MOD
        totalCount = (totalCount + currentCount) % MOD

    return totalCount  # Return the total count of set bits
