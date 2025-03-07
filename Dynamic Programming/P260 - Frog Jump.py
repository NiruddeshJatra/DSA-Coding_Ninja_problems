# Time Complexity:
# - O(n), where n is the number of stones.
# - We process each stone exactly once in a single pass.

# Space Complexity:
# - O(n) for the dp array that stores the minimum cost to reach each position.

# INTUITION:
# This problem asks for the minimum energy required for a frog to jump from the first stone
# to the last stone. The frog can jump either 1 or 2 stones at a time, and the energy cost
# is the absolute difference between the heights of the stones.
#
# We can use dynamic programming to solve this efficiently. For each position i, we need to determine
# whether it's better to jump from position i-1 or position i-2. The answer is whichever gives the
# minimum total energy cost.
#
# For example, with heights [10, 20, 30, 10]:
# - dp[0] = 0 (starting position)
# - dp[1] = dp[0] + |20-10| = 0 + 10 = 10 (only one way to reach here)
# - dp[2] = min(dp[1] + |30-20|, dp[0] + |30-10|) = min(10+10, 0+20) = 20
# - dp[3] = min(dp[2] + |10-30|, dp[1] + |10-20|) = min(20+20, 10+10) = 20
# So the minimum energy required is 20.

# ALGO:
# 1. Initialize a dp array of size n, where dp[i] represents the minimum energy needed to reach position i.
# 2. Set dp[0] = 0 (no energy needed to start at the first stone).
# 3. For each position i from 1 to n-1:
#    a. Calculate the energy needed to jump from position i-1: dp[i-1] + abs(heights[i] - heights[i-1]).
#    b. If i > 1, calculate the energy needed to jump from position i-2: dp[i-2] + abs(heights[i] - heights[i-2]).
#    c. Set dp[i] to the minimum of these two values.
# 4. Return dp[n-1], which represents the minimum energy needed to reach the last stone.

def frogJump(n: int, heights: List[int]) -> int:
   """
   Calculate the minimum energy required for a frog to jump from the first stone to the last stone.
   
   Args:
       n: Number of stones
       heights: List of heights of each stone
       
   Returns:
       Minimum energy required to reach the last stone
   """
   # Initialize dynamic programming array
   minEnergy = [-1] * n
   
   # Base case: no energy required to start at the first stone
   minEnergy[0] = 0
   
   # Calculate minimum energy for each position
   for position in range(1, n):
       # Option 1: Jump from the previous stone
       energyFromPrevious = minEnergy[position-1] + abs(heights[position] - heights[position-1])
       
       # Option 2: Jump from two stones back (if possible)
       energyFromTwoBack = float('inf')  # Initialize with infinity
       if position > 1:
           energyFromTwoBack = minEnergy[position-2] + abs(heights[position] - heights[position-2])
       
       # Choose the option with minimum energy
       minEnergy[position] = min(energyFromPrevious, energyFromTwoBack)
   
   # Return the minimum energy to reach the last stone
   return minEnergy[n-1]
