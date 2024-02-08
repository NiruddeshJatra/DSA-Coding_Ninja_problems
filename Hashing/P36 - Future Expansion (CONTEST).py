# Time Complexity: O(m), where m is the length of the string 's'.
# Space Complexity: O(m), where m is the length of the string 's'.

# INTUITION:
# The function aims to find the minimum number of operations needed to transform the given string 's' into a string of length 'm' such that the most frequently occurring character in the transformed string has a count equal to the length of the original string 's'.
# It uses a Counter to count the frequency of each character in 's' and finds the maximum frequency.
# It then calculates the maximum length the transformed string can have such that the most frequent character occurs exactly 'n' times.
# The function then calculates the number of operations needed to increase the frequency of the most frequent character to reach the maximum length allowed.

# ALGORITHM:
# 1. Count the frequency of each character in the string 's' using Counter and store it in 'counts'.
# 2. Find the maximum frequency of any character in 'counts' and store it in 'mx'.
# 3. Calculate the maximum length 'maxCharLen' the transformed string can have such that the most frequent character occurs exactly 'n' times.
# 4. Initialize 'ans' to 0 to keep track of the number of operations needed.
# 5. While 'mx' is less than 'maxCharLen':
#      - Increment 'ans' by 1.
#      - Multiply 'mx' by 2.
# 6. Return 'ans' as the result.

from typing import List
from collections import Counter

def findMinimumOperations(n: int, m: int, s: str) -> int:
    counts = Counter(s)  # Count the frequency of each character in 's'
    mx = max(counts.values())  # Find the maximum frequency of any character in 's'
    maxCharLen = m - n + mx  # Calculate the maximum length allowed for the transformed string
    ans = 0  # Initialize the number of operations needed to 0
    while mx < maxCharLen:  # While the current maximum frequency is less than the maximum length allowed
        ans += 1  # Increment the number of operations needed
        mx *= 2  # Double the current maximum frequency
    return ans  # Return the number of operations needed

# Example usage:
n = 5
m = 10
s = "abccaa"
print(findMinimumOperations(n, m, s))  # Output: 1
