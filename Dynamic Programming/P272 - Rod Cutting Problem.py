# Time Complexity:
# - O(N^2), where N is the length of the rod.
# - We have N states for the items (rod lengths) and N states for the remaining rod length.

# Space Complexity:
# - O(N), as we use a single array of size N+1 to store the maximum price for each length.

# INTUITION:
# The rod cutting problem is a variation of the unbounded knapsack problem. We have a rod of length N
# and we need to cut it into pieces such that the total price is maximized.
#
# Each piece of length i has a price price[i-1]. We can cut the rod into pieces of different lengths,
# and we need to find the optimal way to maximize the total price.
#
# The key insight is that for each possible rod length i (1 to N), we have two choices:
# 1. Not include a piece of current length (notTake): carry forward the best price from previous lengths
# 2. Include a piece of current length (take): add its price and recursively solve for remaining length
#
# Since we can use multiple pieces of the same length (e.g., two pieces of length 2), this is similar
# to the unbounded knapsack problem.
#
# For example, with price = [1, 5, 8, 9, 10, 17, 17, 20] and N = 8:
# - For rod of length 1, max price is 1
# - For rod of length 2, max price is 5 (one piece of length 2)
# - For rod of length 3, max price is 8 (one piece of length 3)
# - And so on, building up to the solution for length N

# ALGO:
# 1. Initialize a DP array 'prev' of size n+1 with zeros.
# 2. Base case: Fill in values for the first rod length (length 1) for all possible remaining lengths.
# 3. For each subsequent rod length:
#    a. For each remaining rod length from 0 to n:
#       i. Calculate the value if we don't take this rod length (notTake)
#       ii. Calculate the value if we take this rod length, if possible (take)
#          - For rod cutting, we use prev[w - rodLen] to allow multiple pieces of the same length
#       iii. Update the DP array with the maximum of these two values
# 4. Return prev[n], which represents the maximum price achievable for rod length n.

def cutRod(price, n):
   # Initialize the DP array
   maxPrice = [0] * (n + 1)
   
   # Base case: Fill in values for rod length 1
   # For each remaining length w, we can take as many pieces of length 1 as possible
   for remainingLength in range(n + 1):
       maxPrice[remainingLength] = remainingLength * price[0]
   
   # Process each subsequent rod length
   for pieceIndex in range(1, n):
       # Calculate the actual rod length represented by this index
       currentPieceLength = pieceIndex + 1
       
       # For rod cutting (unbounded knapsack), we process lengths from left to right
       # This allows us to consider multiple pieces of the same length
       for remainingLength in range(n + 1):
           # Value if we don't take a piece of the current length
           notTake = maxPrice[remainingLength]
           
           # Value if we take a piece of the current length (if possible)
           take = 0
           if currentPieceLength <= remainingLength:
               # For rod cutting, we use the updated value to allow multiple pieces
               take = price[pieceIndex] + maxPrice[remainingLength - currentPieceLength]
           
           # Update the DP array with the maximum value
           maxPrice[remainingLength] = max(notTake, take)
   
   # Return the maximum price achievable for rod length n
   return maxPrice[n]
