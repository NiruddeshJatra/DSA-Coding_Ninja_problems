# Time Complexity: O(n)
# Space Complexity: O(k)

# INTUITION:
# This function aims to find the length of the longest substring with at most 'k' distinct characters in the string 's'.
# It uses a sliding window approach with two pointers to maintain a substring with at most 'k' distinct characters.

# ALGORITHM:
# 1. Initialize a left pointer 'l' at the beginning of the string.
# 2. Initialize the answer 'ans' to 0.
# 3. Initialize a dictionary 'charCount' to keep track of the count of characters in the current substring.
# 4. Iterate through the string using a right pointer 'r':
#    4.1 Update the count of the character at index 'r' in 'charCount'.
#    4.2 While the count of distinct characters in 'charCount' exceeds 'k':
#        4.2.1 Decrease the count of the character at index 'l' in 'charCount'.
#        4.2.2 If the count of the character at index 'l' becomes 0, remove it from 'charCount'.
#        4.2.3 Move the left pointer 'l' to the right.
#    4.3 Update the answer 'ans' with the maximum length of the current substring.
# 5. Return the maximum length 'ans'.

def kDistinctChars(k, s):
    l = 0
    ans = 0
    charCount = {}
    for r in range(len(s)):
        charCount[s[r]] = 1 + charCount.get(s[r], 0)
        
        while len(charCount) > k:
            charCount[s[l]] -= 1
            if charCount[s[l]] == 0:
                charCount.pop(s[l])
            l += 1

        ans = max(ans, r-l+1)

    return ans
