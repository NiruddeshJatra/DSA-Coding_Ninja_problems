# Time Complexity: O(n), where n is the length of the input string `s`.
# Space Complexity: O(1)

# INTUITION:
# We are using a sliding window approach to find the longest substring with at most `k` distinct characters.
# The window expands to the right until the number of distinct characters exceeds `k`.
# Then, we shrink the window from the left to satisfy the constraint, and update the answer with the maximum length of the valid substring.

# ALGORITHM:
# 1. Initialize variables `l` (left pointer), `r` (right pointer), `maxf` (maximum frequency of a character), `ans` (answer), and `freq` (dictionary to store character frequencies).
# 2. Iterate through the string `s` using a sliding window approach:
#    - Update the frequency of the current character `s[r]` in `freq` and update `maxf` accordingly.
#    - Shrink the window by incrementing `l` until the number of distinct characters in the window exceeds `k`.
#    - Update `ans` with the maximum length of the valid substring.
# 3. Return `ans`.

def longestRepeatingSubstring(s: str, k: int) -> int:
    l, r = 0, 0
    maxf, ans = 0, 0
    freq = {}
        
    while r < len(s):
        freq[s[r]] = 1 + freq.get(s[r], 0)
        maxf = max(maxf, freq[s[r]])
            
        while (r-l+1) - maxf > k:
            freq[s[l]] -= 1
            l += 1
                
        ans = max(ans, r - l + 1)
        r += 1
            
    return ans
