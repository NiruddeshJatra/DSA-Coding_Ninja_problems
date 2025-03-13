# Time Complexity:
# - O(N*S), where N is the number of elements in the array and S is the sum of all elements.
# - We have N elements and for each element, we consider targets from S/2 down to the element's value.
# - We also iterate through the dp array once at the end to find the minimum difference.

# Space Complexity:
# - O(S) since we only need to keep track of targets from 0 to S/2.
# - We use a boolean array to store possible sums.

# INTUITION:
# The problem asks us to find the minimum absolute difference between the sums of two subsets
# when we partition the array into two non-empty subsets.
#
# If we have a total sum of 'totalSum' and one subset sums to 's1', then the other subset
# must sum to 'totalSum - s1'. The difference between the two subsets would be:
# |s1 - (totalSum - s1)| = |2*s1 - totalSum|
#
# Our goal is to find a valid s1 that minimizes this difference. The best approach is to try
# to make s1 as close as possible to totalSum/2.
#
# For example, with array [1,6,11,5]:
# - Total sum = 23
# - Possible subset sums: 0, 1, 5, 6, 7, 11, 12, 16, 17, 18, 23
# - Closest to totalSum/2 = 11.5 would be 11 and 12
# - If s1 = 11, difference = |2*11 - 23| = |22 - 23| = 1

# ALGO:
# 1. Calculate the total sum of the array.
# 2. Use dynamic programming to find all possible subset sums up to totalSum/2:
#    - Use a boolean array where dp[j] = True if we can form a sum j.
#    - Start with dp[0] = True (empty subset has sum 0).
#    - For each number in the array, update the dp table from right to left.
# 3. Iterate through the dp array to find the subset sum that minimizes |2*s1 - totalSum|.
# 4. Return the minimum difference.

from typing import List

def minSubsetSumDifference(nums: List[int], n: int) -> int:
    # Calculate the total sum of the array
    totalSum = sum(nums)
    
    # Our goal is to find subset sums as close as possible to totalSum/2
    targetSum = totalSum // 2
    
    # Initialize dp array: dp[j] is True if we can form a subset with sum j
    dp = [False] * (targetSum + 1)
    dp[0] = True  # Empty subset can form sum 0
    
    # Fill the dp array
    for num in nums:
        # Iterate backwards to avoid counting the same number multiple times
        for j in range(targetSum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    # Find the largest possible subset sum not exceeding totalSum/2
    # This will give us the minimum difference
    closestSum = 0
    for i in range(targetSum, -1, -1):
        if dp[i]:
            closestSum = i
            break
    
    # Calculate the minimum subset sum difference
    # One subset sums to closestSum, the other to (totalSum - closestSum)
    return totalSum - 2 * closestSum
    
    # Alternative approach: check all possible subset sums
    # minDifference = float('inf')
    # for i in range(len(dp)):
    #     if dp[i]:
    #         currentDifference = abs(totalSum - 2 * i)
    #         minDifference = min(minDifference, currentDifference)
    # return minDifference
