# Time Complexity:
# - O(m * n) where m and n are the lengths of the input strings text1 and text2.
# - We need to iterate through each character of both strings once to fill the DP table.
# - Each cell computation takes constant time O(1).

# Space Complexity:
# - O(m * n) for the DP table that stores the length of the common substring ending at each position.

# INTUITION:
# This problem asks for the Longest Common Substring (different from subsequence!). A substring must be 
# contiguous in both original strings. This is what distinguishes it from the Longest Common Subsequence problem.
#
# The key insight is that we need to track how long our matching sequence is at each comparison point.
# Whenever characters match, we can extend the previous diagonal match by 1.
# However, when characters don't match, we must reset our counter to 0 since we're looking for 
# continuous, unbroken matches.
#
# Consider the strings "ABCDE" and "XBCDF":
# - 'A' vs 'X': No match, so length = 0
# - 'B' vs 'B': Match! Length = 1
# - 'C' vs 'C': Match! Length = 2 (extending the previous match)
# - 'D' vs 'D': Match! Length = 3 (extending further)
# - 'E' vs 'F': No match, so length = 0 (reset)
# The longest common substring is "BCD" with length 3.

# ALGORITHM:
# 1. Create a 2D DP table where dp[i][j] represents the length of the longest common substring 
#    ending at text1[i-1] and text2[j-1].
# 2. Fill the table according to the recurrence relation:
#    a. If text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1] (extend previous match)
#    b. Else: dp[i][j] = 0 (reset counter since we need contiguous matches)
# 3. Keep track of the maximum length seen so far, which is the answer.
# 4. Return the maximum length as the result.

def lcs(text1: str, text2: str) -> int:
   # Get the lengths of both input strings
   m, n = len(text1), len(text2)
   
   # Create a DP table to store the length of common substrings
   # dp[i][j] represents the length of the longest common substring
   # ending at text1[i-1] and text2[j-1]
   dp = [[0] * (n + 1) for _ in range(m + 1)]
   
   # Variable to track the maximum length of common substring found
   maxLength = 0
   
   # Fill the DP table
   for i in range(1, m + 1):
       for j in range(1, n + 1):
           # If current characters match
           if text1[i-1] == text2[j-1]:
               # Extend the previous match by 1
               dp[i][j] = 1 + dp[i-1][j-1]
               # Update the maximum length if needed
               maxLength = max(maxLength, dp[i][j])
           else:
               # Reset to 0 as we need continuous matches for a substring
               dp[i][j] = 0
   
   # Return the length of the longest common substring
   return maxLength
