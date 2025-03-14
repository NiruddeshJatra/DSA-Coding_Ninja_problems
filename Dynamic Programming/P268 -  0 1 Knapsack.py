# Time Complexity:
# - O(N * W), where N is the number of items and W is the maximum weight capacity.
# - We process N items and for each item, we consider W different weight capacities.

# Space Complexity:
# - O(W), as we use a single array of size W+1 to store the maximum value for each weight.
# - This is an optimization of the standard O(N*W) solution using a 2D DP array.

# INTUITION:
# This is the classic 0/1 Knapsack problem: we have N items, each with a weight and value,
# and we need to find the maximum value we can achieve with a knapsack of capacity W.
#
# The key insight is to use dynamic programming where we consider each item one by one
# and for each item, we decide whether to include it in our knapsack or not. For each
# weight capacity, we take the maximum of:
# 1. Not including the current item (take the value from previous calculation)
# 2. Including the current item (add its value to the best value achieved with remaining capacity)
#
# We optimize the space complexity by using a 1D array instead of a 2D array, updating
# the array from right to left to avoid using values that have already been updated.
#
# For example, with weights=[1,2,3], values=[10,15,40], and capacity=6:
# Initial: prev = [0, 10, 10, 10, 10, 10, 10]
# After item 1: prev = [0, 10, 15, 25, 25, 25, 25]
# After item 2: prev = [0, 10, 15, 25, 40, 50, 55]
# So the max value is 55.

# ALGO:
# 1. Initialize a 1D DP array 'prev' of size maxWeight+1 with zeros.
# 2. Base case: Fill in values for the first item for all possible weights.
# 3. For each subsequent item:
#    a. For each weight from maxWeight down to 0:
#       i. Calculate the value if we don't take this item (notTake)
#       ii. Calculate the value if we take this item, if possible (take)
#       iii. Update prev[w] with the maximum of these two values
# 4. Return prev[maxWeight], which represents the maximum value achievable.

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def knapsack01(weights, values, numItems, maxCapacity):
   # Initialize the DP array for the first item
   dpValues = [0] * (maxCapacity + 1)
   
   # Base case: Fill in values for the first item
   for capacity in range(weights[0], maxCapacity + 1):
       dpValues[capacity] = values[0]
   
   # Process each subsequent item
   for itemIndex in range(1, numItems):
       # Update DP array from right to left to avoid using values that were already updated
       for capacity in range(maxCapacity, -1, -1):
           # Value if we don't take the current item
           valueWithoutItem = dpValues[capacity]
           
           # Value if we take the current item (if possible)
           valueWithItem = float('-inf')
           if weights[itemIndex] <= capacity:
               valueWithItem = values[itemIndex] + dpValues[capacity - weights[itemIndex]]
           
           # Update the DP array with the maximum value
           dpValues[capacity] = max(valueWithoutItem, valueWithItem)
   
   # Return the maximum value achievable with the given capacity
   return dpValues[maxCapacity]

# Process test cases
testCases = int(input())
for _ in range(testCases):
   numItems = int(input())
   weights = list(map(int, input().split()))
   values = list(map(int, input().split()))
   maxCapacity = int(input())
   
   maxValue = knapsack01(weights, values, numItems, maxCapacity)
   print(maxValue)
