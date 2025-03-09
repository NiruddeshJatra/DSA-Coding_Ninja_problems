# Time Complexity:
# - O(N*K), where N is the number of elements in the array and K is the target sum.
# - We fill a DP table of size N*K, doing constant work for each cell.

# Space Complexity:
# - O(N*K) in the original implementation using a dictionary.
# - Can be optimized to O(K) using rolling arrays as we only need the previous row.

# INTUITION:
# The problem asks us to determine if there exists a subset of the array that sums to K.
# This is a classic dynamic programming problem where at each step, we have two choices:
# 1. Include the current element in our subset
# 2. Exclude the current element from our subset
#
# For example, if arr = [1, 2, 3] and k = 5, we can trace the possible combinations:
# - Include 1, then include 2, then include 3 => 1+2+3=6 (exceeds k)
# - Include 1, then include 2, exclude 3 => 1+2=3 (less than k)
# - Include 1, exclude 2, include 3 => 1+3=4 (less than k)
# - Exclude 1, include 2, include 3 => 2+3=5 (equal to k) => True

# ALGO:
# 1. Create a DP table where dp[i][j] represents whether there's a subset of the first i elements that sums to j.
# 2. Initialize base cases:
#    - For target sum 0, answer is always True (empty subset)
#    - For the first element, check if it equals the target
# 3. For each element and each possible target sum:
#    - Either exclude the current element (take value from previous row)
#    - Or include the current element (check if (target - current element) was possible with previous elements)
# 4. Return the value for the entire array and target sum K.

def subsetSumToK(n, k, arr):
    # Create a 2D DP table of size (n x (k+1))
    dp = [[False for _ in range(k+1)] for _ in range(n)]
    
    # Base case: Empty subset can always form sum 0
    for i in range(n):
        dp[i][0] = True
    
    # Base case: Check if first element can form the target
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    # Fill the DP table
    for i in range(1, n):
        for target in range(1, k+1):
            # Option 1: Exclude the current element
            notTake = dp[i-1][target]
            
            # Option 2: Include the current element (if possible)
            take = False
            if arr[i] <= target:
                take = dp[i-1][target - arr[i]]
            
            # Can achieve target if either option works
            dp[i][target] = notTake or take
    
    return dp[n-1][k]

# Space-optimized version using only two rows
def subsetSumToK_optimized(n, k, arr):
    # Create two rows for DP
    prev = [False] * (k+1)
    curr = [False] * (k+1)
    
    # Base case: Empty subset can always form sum 0
    prev[0] = True
    
    # Base case for first element
    if arr[0] <= k:
        prev[arr[0]] = True
    
    # Fill the DP table
    for i in range(1, n):
        # Base case for current row
        curr[0] = True
        
        for target in range(1, k+1):
            # Option 1: Exclude the current element
            notTake = prev[target]
            
            # Option 2: Include the current element (if possible)
            take = False
            if arr[i] <= target:
                take = prev[target - arr[i]]
            
            # Can achieve target if either option works
            curr[target] = notTake or take
        
        # Update previous row for next iteration
        prev = curr.copy()
    
    return prev[k]
