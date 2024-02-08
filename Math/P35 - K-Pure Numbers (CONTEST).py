# Time Complexity: O(1)
# Space Complexity: O(1)

# INTUITION:
# The function aims to calculate the number of k-pure numbers in the range [1, n].
# A k-pure number x is a number that is divisible by k and (x/k) not divisible by k.

# ALGORITHM:
# 1. Calculate the number of integers in the range [1, n] that are divisible by k using integer division n//k.
# 2. Calculate the number of integers in the range [1, n] that are divisible by k^2 using integer division n//(k^2).
# 3. The difference between the two values obtained in steps 1 and 2 represents the number of k-pure numbers in the range [1, n].
# 4. Return this difference as the result.

from typing import List

def kPure(n: int, k: int) -> int:
    return n // k - n // (k ** 2)
