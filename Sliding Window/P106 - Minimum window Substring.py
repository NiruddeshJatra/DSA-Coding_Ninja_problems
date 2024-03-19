# Time Complexity: O(n)
# Space Complexity: O(m), where m is the length of string b

# INTUITION:
# This function aims to find the minimum substring of string 'a' that contains all characters of string 'b'.
# It uses a sliding window approach with two pointers to maintain the substring containing all characters of 'b'
# and minimize its length.

# ALGORITHM:
# 1. Initialize a dictionary 'tCount' to store the count of characters in string 'b'.
# 2. Iterate through string 'b' and populate 'tCount' with character counts.
# 3. Initialize the left pointer 'l' to 0, the answer string 'ans' to an empty string, and 'tLength' to the length of 'b'.
# 4. Iterate through string 'a' using a right pointer 'r':
#    4.1 If the character at index 'r' of 'a' exists in 'tCount':
#        4.1.1 Decrease the count of the character in 'tCount'.
#        4.1.2 If the count becomes zero or positive, decrease 'tLength'.
#    4.2 While 'tLength' is 0 (indicating all characters of 'b' are found):
#        4.2.1 Update 'ans' if it's empty or if the current substring is shorter than the existing 'ans'.
#        4.2.2 If the character at index 'l' of 'a' exists in 'tCount':
#              - Increase the count of the character in 'tCount'.
#              - If the count becomes positive, increase 'tLength'.
#        4.2.3 Move the left pointer 'l' to the right.
# 5. Return the minimum length substring 'ans'.

def minSubstring(a: str, b: str) -> str:
    tCount = {}
    for c in b:
        tCount[c] = 1 + tCount.get(c, 0)
            
    l = 0
    ans = ""
    tLength = len(b)
    for r in range(len(a)):
        if a[r] in tCount:
            tCount[a[r]] -= 1
            if tCount[a[r]] >= 0:
                tLength -= 1
                              
        while tLength == 0:
            if not ans or len(ans) > (r-l+1):
                ans = a[l:r+1]
                
            if a[l] in tCount:
                tCount[a[l]] += 1
                if tCount[a[l]] > 0:
                    tLength += 1
                    
            l += 1
                
    return ans
