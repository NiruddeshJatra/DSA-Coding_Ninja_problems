# Time Complexity:
# - O(N * W), where N is the number of items and W is the maximum weight capacity.
# - We iterate through N items and for each item, we consider W different weight capacities.

# Space Complexity:
# - O(W), as we use a single array of size W+1 to store the maximum profit for each weight.
# - This is an optimization of the standard O(N*W) solution using a 2D DP array.

# INTUITION:
# The unbounded knapsack problem is similar to the 0/1 knapsack, but here we can take
# multiple instances of the same item (unlimited supply). We need to find the maximum profit
# we can achieve with a knapsack of capacity W.
#
# The key insight is that for each item, we have two choices:
# 1. Not include the current item (notTake): carry forward the best profit from previous items
# 2. Include the current item (take): add its profit and recursively solve for remaining weight
#
# Unlike the 0/1 knapsack where we move to the next item after taking one, here we stay on the 
# same item as we can take it multiple times. This is reflected in the dp state transition.
#
# However, there's a key issue in the provided code: when calculating 'take', we're using prev[w - weight[i]] 
# which means we're only considering one instance of the current item. For unbounded knapsack, we should 
# use the updated value (current[w - weight[i]]) to allow multiple instances.
#
# For example, with weights=[2,4,6], profits=[5,11,13], and capacity=10:
# We should be able to take multiple instances of weight 2 (profit 5) to get profit 25.

# ALGO:
# 1. Initialize a 1D DP array 'prev' of size maxWeight+1 with zeros.
# 2. Base case: Fill in values for the first item for all possible weights.
# 3. For each subsequent item:
#    a. Create a new array 'curr' or use 'prev' directly (since we process all weights)
#    b. For each weight from 0 to maxWeight:
#       i. Calculate the value if we don't take this item (notTake)
#       ii. Calculate the value if we take this item, if possible (take)
#          - For unbounded knapsack, we use curr[w - weight[i]] to allow multiple instances
#       iii. Update the DP array with the maximum of these two values
# 4. Return prev[maxWeight], which represents the maximum profit achievable.

from typing import List

def unboundedKnapsack(n: int, maxWeight: int, profit: List[int], weight: List[int]) -> int:
   # Initialize the DP array
   dpProfit = [0] * (maxWeight + 1)
   
   # Base case: Fill in values for the first item
   # For each weight w, we can take as many instances of item 0 as possible
   for w in range(maxWeight + 1):
       dpProfit[w] = (w // weight[0]) * profit[0]
   
   # Process each subsequent item
   for itemIndex in range(1, n):
       # For unbounded knapsack, we process weights from left to right
       # This allows us to consider multiple instances of the current item
       for w in range(maxWeight + 1):
           # Value if we don't take the current item
           notTake = dpProfit[w]
           
           # Value if we take the current item (if possible)
           take = 0
           if weight[itemIndex] <= w:
               # For unbounded knapsack, we use the updated value to allow multiple instances
               take = profit[itemIndex] + dpProfit[w - weight[itemIndex]]
           
           # Update the DP array with the maximum value
           dpProfit[w] = max(notTake, take)
   
   # Return the maximum profit achievable with the given weight capacity
   return dpProfit[maxWeight]
