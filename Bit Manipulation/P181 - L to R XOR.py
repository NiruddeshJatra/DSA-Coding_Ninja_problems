# Time Complexity: O(log(n)), where n is the value of R.
# - The XOR function runs in constant time O(1) for each input `n`.
# - Since XOR is called twice (for L-1 and R), the overall time complexity is O(log(n)) because the function is applied only once to each argument.

# Space Complexity: O(1).
# - The algorithm uses a constant amount of space regardless of the input size.

# INTUITION:
# The problem asks for the XOR of all numbers between L and R. Directly XORing all numbers in this range would take O(R - L) time, 
# which could be inefficient. Instead, we utilize the properties of the XOR operation to derive a more efficient solution.
# XOR has a cyclical pattern every 4 numbers. The key insight is that the XOR from 0 to n follows a predictable cycle based on n % 4:
#   - If n % 4 == 0, XOR(0 to n) = n
#   - If n % 4 == 1, XOR(0 to n) = 1
#   - If n % 4 == 2, XOR(0 to n) = n + 1
#   - If n % 4 == 3, XOR(0 to n) = 0
# By leveraging this cyclical property, we can compute the XOR from L to R efficiently.

# ALGO:
# 1. Define a helper function `XOR(n)` to compute the XOR of all numbers from 0 to n based on the cyclical pattern described.
# 2. Compute the XOR of numbers from 0 to R using XOR(R).
# 3. Compute the XOR of numbers from 0 to L-1 using XOR(L-1).
# 4. The result is the XOR of all numbers from L to R, which can be obtained by XORing the two previous results:
#    XOR(L to R) = XOR(0 to R) ^ XOR(0 to L-1).

from typing import *

class Solution:
    def findXOR(self, L: int, R: int) -> int:
        def XOR(n):
            # This function returns the XOR of all numbers from 0 to n based on n % 4.
            if n % 4 == 1:
                return 1
            elif n % 4 == 2:
                return n + 1
            elif n % 4 == 3:
                return 0
            else:
                return n

        # XOR(L to R) = XOR(0 to R) ^ XOR(0 to L-1)
        return XOR(L - 1) ^ XOR(R)
