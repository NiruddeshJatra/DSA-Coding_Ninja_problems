# Time Complexity: O(N * log(N))
# Space Complexity: O(N)

# ALGO:
# 1. Initialize variables for tracking maximum and second maximum characters.
# 2. Iterate through each substring of length K.
#     2.1 Count the occurrences of each character in the substring.
#     2.2 Find the most frequent and second most frequent characters in the substring.
#     2.3 Update the total cost based on the counts of these characters.
# 3. Return the total cost.

from collections import Counter

def differenceInConsecutive(n: int, k: int, s: str) -> int:
    totalCost = 0
    i, j = 0, k
    prevMaxSubarrChars = []
    while j <= n:
        subarr = s[i:j]
        charCount = Counter(subarr)
        sortedCharCount = dict(sorted(charCount.items(), key=lambda x: x[1], reverse=True))
        subarrChars = list(sortedCharCount.keys())
        
        curMaxSubarrChar = subarrChars[0]
        if prevMaxSubarrChars and curMaxSubarrChar in prevMaxSubarrChars:
            # If the current max character is in the previous max characters list,
            # choose the next character from subarrChars
            curMaxSubarrChars.remove(curMaxSubarrChar)
            curMaxSubarrChar = subarrChars[1] if subarrChars[1:] else subarrChars[0]
        
        # Update the previous max characters list
        prevMaxSubarrChars = [char for char in subarrChars if sortedCharCount[char] == sortedCharCount[curMaxSubarrChar]]

        totalCost += len(subarr) - subarr.count(curMaxSubarrChar)
        i += k
        j += k
    
    return totalCost
