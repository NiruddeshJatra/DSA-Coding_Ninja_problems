# Time Complexity:
# - O(N * K), where N is the length of the array and K is the target sum.
# - We iterate through each element in the array and for each element, we potentially update O(K) states.

# Space Complexity:
# - O(K), as we use a single array of size K+1 to store the number of ways to form each sum.

# INTUITION:
# This problem asks for the number of ways to form a sum K using elements from the given array.
# It's a variation of the classic subset sum problem, but instead of finding if a subset exists,
# we need to count all possible subsets.
#
# The key insight is to use dynamic programming with a 1D array where prev[j] represents the 
# number of ways to form sum j using the elements considered so far. By processing the array elements
# one by one and updating our DP array from right to left (to avoid counting the same element multiple times),
# we can count all valid combinations.
#
# For example, with arr = [1, 2, 3] and k = 3, we would have:
# Initial: prev = [1, 0, 0, 0]
# After 1: prev = [1, 1, 0, 0]
# After 2: prev = [1, 1, 1, 1]
# After 3: prev = [1, 1, 1, 2]
# So there are 2 ways to form sum 3: [1,2] and [3].

# ALGO:
# 1. Initialize a DP array 'prev' of size K+1 with zeros, and set prev[0] = 1 (there's 1 way to form sum 0: empty set).
# 2. For each number 'num' in the array:
#    a. Skip if num > k (can't contribute to sum K)
#    b. For each possible sum 'j' from K down to num:
#       i. Update prev[j] += prev[j-num] (add the number of ways to form j-num)
# 3. Return prev[K], which represents the number of ways to form sum K.

from typing import List
from collections import defaultdict

def findWays(arr: List[int], k: int) -> int:
   # Initialize our DP array (prev[j] = number of ways to form sum j)
   waysToFormSum = [0] * (k + 1)
   MOD = 10**9 + 7
   
   # Base case: there's 1 way to form sum 0 (by taking no elements)
   waysToFormSum[0] = 1
   
   # Process each element in the array
   for currentNum in arr:
       # Skip if current number is greater than target sum
       if currentNum > k:
           continue
       
       # Update DP array from right to left to avoid counting the same element multiple times
       for currentSum in range(k, currentNum - 1, -1):
           # Add the number of ways to form (currentSum - currentNum)
           waysToFormSum[currentSum] = (waysToFormSum[currentSum] + waysToFormSum[currentSum - currentNum]) % MOD
   
   # Return the number of ways to form sum k
   return waysToFormSum[k]
