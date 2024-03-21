# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# INTUITION:
# The function 'minWindow' finds the minimum window in string 's' that contains all characters in string 't'.
# It uses a two-pointer approach to maintain a sliding window and iterates through string 's', updating the window 
# boundaries to find the minimum window containing all characters of 't'.

# ALGORITHM:
# 1. Initialize pointers 'l', 'r', and 'k' to 0, and an empty string 'ans'.
# 2. Iterate through string 's' using the right pointer 'r':
#    2.1 If the character at 's[r]' matches the character at index 'k' of string 't', increment 'k'.
#    2.2 If 'k' becomes equal to the length of string 't', it means all characters of 't' have been found in 's':
#        2.2.1 Update 'l' to the current position of 'r' and decrement 'k' to find the starting index of the window.
#        2.2.2 Iterate backward from 'l' until 'k' becomes -1:
#              2.2.2.1 If the character at 's[l]' matches the character at index 'k' of string 't', decrement 'k'.
#              2.2.2.2 Decrement 'l'.
#        2.2.3 Increment 'l' by 1 to exclude the starting character.
#        2.2.4 Update 'ans' with the minimum window if 'ans' is empty or the current window is smaller.
#        2.2.5 Reset 'k' to 0 and move 'r' to the next character after 'l'.
#    2.3 Increment 'r'.
# 3. Return 'ans', which represents the minimum window containing all characters of string 't'.

def minWindow(s, t):
    l, r, k = 0, 0, 0
    ans = ""
    while r < len(s) and k < len(t):
        if s[r] == t[k]:
            k += 1
        
        if k == len(t):
            l = r
            k = len(t) - 1
            while k >= 0:
                if s[l] == t[k]:
                    k -= 1
                l -= 1

            l += 1
            if not ans or len(ans) > (r-l+1):
                ans = s[l:r+1]
            
            k, r = 0, l + 1

        r += 1

    return ans
