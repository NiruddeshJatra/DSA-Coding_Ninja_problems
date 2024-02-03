# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(n)

# ALGO:
# 1. Initialize a hashmap to store cumulative sums and their corresponding indices.
# 2. Initialize variables max_length and curr_sum.
# 3. Iterate through the array, updating the curr_sum and checking if it exists in the hashmap.
#    - If curr_sum exists in the hashmap, calculate the length of the subarray with zero sum.
#    - Update max_length if needed.
#    - If curr_sum doesn't exist in the hashmap, add it to the hashmap with its current index.
# 4. Return max_length, which represents the length of the longest subarray with zero sum.

def LongestSubsetWithZeroSum(arr):
    sumIndicesMap = {0:-1}
    maxLen, currentSum = 0, 0
    for i,num in enumerate(arr):
        currentSum += num
        if currentSum in sumIndicesMap:
            subarrLen = i - sumIndicesMap[currentSum]
            maxLen = max(maxLen, subarrLen)
        else:
            sumIndicesMap[currentSum] = i
    return maxLen
