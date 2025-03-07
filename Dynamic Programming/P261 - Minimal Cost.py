# Time Complexity:
# - O(N * K), where N is the number of stones and K is the maximum jump length.
# - We iterate through each stone and for each stone, we check up to K previous stones.

# Space Complexity:
# - O(N), for the dp array that stores the minimum cost to reach each stone.

# INTUITION:
# The problem is about finding the minimum cost for the frog to reach the last stone.
# At each stone, the frog can jump up to K stones back, and the cost is determined by the height difference.
# We use dynamic programming to store the minimum cost to reach each stone, building up the solution step by step.

# Example:
# heights = [10, 30, 40, 20], k = 2
# dp[0] = 0 (start at stone 0)
# dp[1] = |30 - 10| = 20
# dp[2] = min(|40 - 30| + dp[1], |40 - 10| + dp[0]) = min(10 + 20, 30) = 30
# dp[3] = min(|20 - 40| + dp[2], |20 - 30| + dp[1]) = min(20 + 30, 10 + 20) = 30

# ALGO:
# 1. Initialize a dp array of size N with infinity, except dp[0] = 0 (starting point).
# 2. For each stone i, try jumping back up to K stones.
# 3. Update dp[i] with the minimum cost to reach stone i.
# 4. Return dp[n-1], which contains the minimum cost to reach the last stone.

from typing import List

def minimizeCost(n: int, k: int, heights: List[int]) -> int:
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(heights[i] - heights[i - j]))
        
    return dp[n - 1]
