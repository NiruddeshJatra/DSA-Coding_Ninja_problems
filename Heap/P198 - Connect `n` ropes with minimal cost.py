# Time Complexity:
# - O(N log N) where N is the number of ropes
#   - Heapifying initial array: O(N)
#   - N-1 operations, each involving:
#     * Two heap pops: O(log N)
#     * One heap push: O(log N)
#   - Overall: O(N log N)

# Space Complexity:
# - O(1) additional space
#   - Using input array as heap
#   - Only using primitive variables (cost, curLen)

# INTUITION:
# This is a greedy problem where:
# - We want to minimize total cost of connecting ropes
# - Cost of connecting ropes equals sum of their lengths
# - Best strategy is to always connect shortest ropes first
# Using min heap gives us efficient access to shortest ropes
# and maintains order as we combine ropes

# ALGO:
# 1. Convert input array into min heap
# 2. For N-1 times (to connect N ropes):
#    - Pop two shortest ropes from heap
#    - Add their lengths to get new rope length
#    - Add this length to total cost
#    - Push new rope back to heap
# 3. Return total cost

import heapq

def connectRopes(arr, n):
   # Initialize total cost
   cost = 0
   
   # Convert array to min heap
   heapq.heapify(arr)
   
   # Connect ropes n-1 times
   for i in range(n-1):
       # Get two shortest ropes and combine
       curLen = heapq.heappop(arr) + heapq.heappop(arr)
       # Add to heap as new rope
       heapq.heappush(arr, curLen)
       # Add to total cost
       cost += curLen
   
   return cost
