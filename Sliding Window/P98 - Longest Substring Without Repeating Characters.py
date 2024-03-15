def uniqueSubstrings(input_str):
    # Time Complexity: O(n)
    # Space Complexity: O(1) (assuming constant character set)

    # INTUITION:
    # This function aims to find the length of the longest substring 
    # with unique characters in the given string 'input_str'. 
    # The approach involves using a sliding window technique to maintain 
    # the longest substring with unique characters.

    # ALGO:
    # 1. Initialize variables: 'ans' to store the length of the longest 
    #    substring with unique characters, 'l' as the left pointer of 
    #    the sliding window, and 'charCount' dictionary to count the 
    #    occurrences of each character.
    # 2. Iterate through each index 'r' in the range of the length of 
    #    the input string.
    #    2.1. Update the count of the current character in 'charCount'.
    #    2.2. While the count of the current character in 'charCount' 
    #         is greater than 1:
    #         - Decrement the count of the character at the left pointer 
    #           'l' and move the left pointer to the right.
    #    2.3. Update 'ans' with the maximum length of the current window.
    # 3. Return 'ans'.

    ans, l = 0, 0
    charCount = {}
    
    for r in range(len(input_str)):
        charCount[input_str[r]] = 1 + charCount.get(input_str[r], 0)

        while charCount[input_str[r]] > 1:
            charCount[input_str[l]] -= 1
            l += 1

        ans = max(ans, r - l + 1)

    return ans
