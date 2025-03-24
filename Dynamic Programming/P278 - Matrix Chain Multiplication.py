def matrixMultiplication(arr, n):
   # Time Complexity:
   # - O(n³), where n is the number of matrices
   # - We have three nested loops: one for iterating through different ranges, 
   #   and two for finding the minimum cost of matrix multiplication
   
   # Space Complexity:
   # - O(n²) for the dynamic programming memoization table
   
   # INTUITION:
   # Matrix Chain Multiplication is a classic dynamic programming problem that solves 
   # the optimization of multiplying a sequence of matrices with minimum computational cost.
   #
   # Consider matrices A(10x30), B(30x5), C(5x60):
   # Possible multiplication orders:
   # 1. (AB)C: 10*30*5 + 10*5*60 = 150 + 3000 = 3150 operations
   # 2. A(BC): 30*5*60 + 10*30*60 = 9000 + 18000 = 27000 operations
   #
   # The goal is to find the sequence of multiplications that minimizes total operations.
   
   # ALGO:
   # 1. Use dynamic programming to store minimum multiplication costs for different matrix ranges
   # 2. Build solutions for smaller ranges and use them to solve larger ranges
   # 3. Iterate through different possible split points to find minimum cost
   
   # Recursive Memoization Solution
   def f(i, j):
       # Base case: single matrix, no multiplication needed
       if i == j:
           return 0
       
       # If solution already computed, return memoized result
       if dp[i][j] != -1:
           return dp[i][j]
       
       # Initialize minimum cost to infinity
       mini = float('inf')
       
       # Try all possible ways to split matrix chain
       for k in range(i, j):
           # Calculate cost of current split:
           # 1. Cost of left subchain multiplication
           # 2. Cost of right subchain multiplication
           # 3. Cost of multiplying these two resultant matrices
           steps = (arr[i-1] * arr[k] * arr[j]) + f(i, k) + f(k+1, j)
           
           # Update minimum cost
           mini = min(mini, steps)
       
       # Memoize and return result
       dp[i][j] = mini
       return dp[i][j]
   
   # Initialize memoization table with -1
   dp = [[-1] * (n + 1) for _ in range(n + 1)]
   
   # Call recursive function to find minimum multiplication cost
   return f(1, n-1)

def matrixMultiplication(arr, n):
   # Tabulation (Bottom-Up) Solution
   
   # Time Complexity:
   # - O(n³), where n is the number of matrices
   # - Three nested loops for computing minimum multiplication costs
   
   # Space Complexity:
   # - O(n²) for the dynamic programming table
   
   # INTUITION:
   # Similar to recursive solution, but we build the solution iteratively
   # Bottom-up approach fills the dp table from smaller subproblems to larger ones
   
   # Initialize DP table with 0
   dp = [[0] * (n + 1) for _ in range(n + 1)]
   
   # Iterate through different range lengths
   for length in range(2, n):
       for i in range(1, n-length+1):
           j = i + length - 1
           
           # Initialize minimum cost to infinity
           mini = float('inf')
           
           # Try all possible split points for current range
           for k in range(i, j):
               # Calculate total cost of current split
               steps = (arr[i-1] * arr[k] * arr[j]) + dp[i][k] + dp[k+1][j]
               
               # Update minimum cost
               mini = min(mini, steps)
           
           # Store minimum cost for current range
           dp[i][j] = mini
   
   # Return minimum cost for multiplying entire matrix chain
   return dp[1][n-1]
