# Time Complexity:
# - O(N * K), where N is the length of the array and K is (totalSum + d) / 2.
# - We iterate through each element in the array and for each element, we update O(K) states.

# Space Complexity:
# - O(K), as we use a single array of size K+1 to store the number of ways to form each sum.

# INTUITION:
# This problem asks for the number of ways to partition the array into two subsets s1 and s2 such that s1 - s2 = d.
# We can transform this problem into finding subsets with a specific sum using the following logic:
# 
# Let's denote:
# - s1 + s2 = totalSum (sum of all elements)
# - s1 - s2 = d (our target difference)
# 
# From these equations:
# s1 = (totalSum + d) / 2
# 
# So the problem reduces to finding the number of subsets with sum equal to (totalSum + d) / 2.
# 
# There's an important constraint: (totalSum + d) must be even for s1 to be an integer.
# If (totalSum + d) is odd, there can't be any valid partition.
# 
# For example, with nums = [1, 1, 2, 3] and d = 1:
# totalSum = 7, s1 = (7 + 1) / 2 = 4
# We need to find subsets with sum 4, which are [1,3] and [1,1,2]
# Therefore, there are 2 ways to partition the array with difference 1.

# ALGO:
# 1. Calculate totalSum (sum of all elements in the array).
# 2. Check if (totalSum + d) is odd. If yes, return 0 (no valid partition).
# 3. Calculate target sum k = (totalSum + d) / 2.
# 4. Initialize a DP array 'prev' of size k+1 with zeros, and set prev[0] = 1.
# 5. For each number 'num' in the array:
#    a. Skip if num > k (can't contribute to sum k)
#    b. For each possible sum 'j' from k down to num:
#       i. Update prev[j] += prev[j-num] (add the number of ways to form j-num)
# 6. Return prev[k], which represents the number of ways to form sum k.

from typing import List

def countPartitions(n: int, d: int, nums: List[int]) -> int:
   totalSum = sum(nums)
   
   # Check if we can have a valid partition
   # If (totalSum + d) is odd, we can't have integer values for s1 and s2
   if (totalSum + d) % 2 != 0:
       return 0
   
   # If totalSum < d, we can't have s1 - s2 = d where s1, s2 ≥ 0
   if totalSum < d:
       return 0
       
   # Calculate the target sum for subset s1
   targetSum = (totalSum + d) // 2
   
   # Initialize our DP array
   waysToFormSum = [0] * (targetSum + 1)
   MOD = 10**9 + 7
   
   # Base case: there's 1 way to form sum 0 (by taking no elements)
   waysToFormSum[0] = 1
   
   # Process each element in the array
   for currentNum in nums:
       # Skip if current number is greater than target sum
       if currentNum > targetSum:
           continue
       
       # Update DP array from right to left to avoid counting the same element multiple times
       for currentSum in range(targetSum, currentNum - 1, -1):
           # Add the number of ways to form (currentSum - currentNum)
           waysToFormSum[currentSum] = (waysToFormSum[currentSum] + waysToFormSum[currentSum - currentNum]) % MOD
   
   # Return the number of ways to form the target sum
   return waysToFormSum[targetSum]
