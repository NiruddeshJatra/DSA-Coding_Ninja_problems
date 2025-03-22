# Time Complexity:
# - O(m * n) where m and n are the lengths of the input strings s1 and s2.
# - We need to fill the entire DP table of size (m+1) × (n+1), and each cell computation is O(1).
# - The backtracking procedure to construct the LCS string takes O(m + n) time.

# Space Complexity:
# - O(m * n) for the DP table that stores the length of the LCS at each step.
# - O(m + n) in the worst case for the output string (if the entire strings are a common subsequence).

# INTUITION:
# The Longest Common Subsequence (LCS) problem asks us to find the longest subsequence that appears in both strings.
# Unlike substrings, subsequences don't need to be contiguous - they just need to maintain relative order.
#
# The key insight is that we can build the LCS incrementally by comparing characters from both strings:
# 1. If the current characters match, we extend the LCS we've found so far.
# 2. If they don't match, we take the longer of two possible LCSs:
#    a. The LCS excluding the current character from s1
#    b. The LCS excluding the current character from s2
#
# Think of it like this: At each step, we're asking "Should I include this matching pair of characters in my LCS,
# or can I find a longer sequence by skipping some characters?"
#
# Example: Finding LCS of "ABCDE" and "ACE"
# - 'A' matches in both → include in LCS
# - 'B' doesn't match 'C' → need to decide whether to skip 'B' or 'C'
# - Skipping 'B' gives us a match with 'C' → include 'C' in LCS
# - Continue this process → LCS is "ACE"

# ALGORITHM:
# 1. Create a DP table where dp[i][j] = length of LCS of s1[0...i-1] and s2[0...j-1].
# 2. Fill the table using the recurrence relation:
#    a. If s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1] (extend LCS)
#    b. Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (take the better option)
# 3. Use backtracking to construct the actual LCS string:
#    a. Start from dp[m][n] and work backwards
#    b. If characters match, include the character and move diagonally up-left
#    c. If not, move in the direction of the larger value (either up or left)
# 4. Reverse the constructed string (since we built it backwards) and return it.

def findLCS(m: int, n: int, s1: str, s2: str) -> str:
   # Step 1: Create a DP table to store lengths of LCS
   dp = [[0] * (n + 1) for _ in range(m + 1)]
   
   # Step 2: Fill the DP table
   for i in range(1, m + 1):
       for j in range(1, n + 1):
           # If current characters match, extend the LCS
           if s1[i-1] == s2[j-1]:
               dp[i][j] = 1 + dp[i-1][j-1]
           else:
               # Take the maximum of two possible scenarios
               dp[i][j] = max(dp[i-1][j], dp[i][j-1])
   
   # Step 3: Backtrack to build the LCS string
   lcsString = ''
   i, j = m, n
   
   while i > 0 and j > 0:
       # If characters match, include this character in LCS
       if s1[i-1] == s2[j-1]:
           lcsString += s1[i-1]
           i -= 1
           j -= 1
       # If not, move in the direction of the larger value
       elif dp[i-1][j] > dp[i][j-1]:
           # LCS came from top cell, move up
           i -= 1
       else:
           # LCS came from left cell, move left
           j -= 1
   
   # Step 4: Reverse the string since we built it backwards
   return lcsString[::-1]
