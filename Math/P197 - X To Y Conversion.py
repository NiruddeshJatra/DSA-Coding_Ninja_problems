# Time Complexity:
# - O(1), as we only perform constant time operations:
#   - Basic arithmetic operations (subtraction, division, modulo)
#   - One square root calculation
#   - All operations are independent of input size

# Space Complexity:
# - O(1), only using a single variable 'p' for calculation
#   - No additional data structures or recursive calls are used

# INTUITION:
# This problem appears to be about finding minimum number of steps to convert x to y where:
# - In each step i, we can add i to the current number
# - The pattern forms arithmetic sequence with increasing differences
# - If we look at the sum pattern: 1 + 2 + 3 + ... + n = n(n+1)/2
# - The total difference (y-x) must be divisible by 3 for a valid solution
# - We can use the quadratic formula derived from arithmetic sequence to find n

# ALGO:
# 1. Check if (y-x) is divisible by 3, if not return -1 (impossible case)
# 2. Calculate p = (y-x)/3
# 3. If p = 2, return -1 (special case where no solution exists)
# 4. Use the quadratic formula to find n:
#    - n(n+1)/2 = p
#    - n^2 + n - 2p = 0
#    - n = (-1 + sqrt(1 + 8p))/2
# 5. Return the calculated n

def xToYconversion(x: int, y: int) -> int:
   # Check if difference is divisible by 3
   if (y-x) % 3 != 0:
       return -1
   
   # Calculate p value
   p = (y-x)//3
   # Special case where no solution exists
   if p == 2:
       return -1

   # Use quadratic formula to find number of steps
   return (-1 + int((1 + 8*p) ** 0.5)) // 2
