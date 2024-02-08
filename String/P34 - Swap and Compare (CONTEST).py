# Time Complexity: O(n), where n is the length of the strings 's' and 't'.
# Space Complexity: O(1), constant space complexity.

# INTUITION:
# The function aims to compare corresponding characters of the strings 's' and 't' lexicographically.
# It iterates through the strings and checks if the character in 's' is smaller than the character in 't' at each position.
# If such a position is found, it indicates that 's' can be made lexicographically smaller than 't'.
# In this case, the function returns 1.
# If no such position is found after iterating through the strings, it means 's' cannot be made lexicographically smaller than 't'.
# In this case, the function returns 0.

# ALGORITHM:
# 1. Iterate through the strings 's' and 't' simultaneously using a loop with the range from 0 to n-1.
# 2. Check if the character in 's' at index i is lexicographically smaller than the character in 't' at index i.
# 3. If such a character is found, return 1 to indicate that 's' can be made lexicographically smaller than 't'.
# 4. If no such character is found after iterating through the strings, return 0 to indicate that 's' cannot be made lexicographically smaller than 't'.

from typing import List

def makeStringSmaller(n: int, s: str, t: str) -> int:
    for i in range(n):
        if s[i] < t[i]:
            return 1
    return 0
