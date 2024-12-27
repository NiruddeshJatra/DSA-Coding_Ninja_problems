# Time Complexity:
# - O(1), as we only perform constant time operations (min, subtraction, comparison)
#   - No loops or iterative operations are involved

# Space Complexity:
# - O(1), only using a few primitive variables (minCol, diff)
#   - No additional data structures are needed

# INTUITION:
# The problem appears to be about finding if we can make a majority color in a sequence where:
# - 'b' represents the count of blue elements
# - 'r' represents the count of red elements
# - 'k' represents the number of elements we can change
# By taking the minimum of blue and red colors, we can determine if we can make the other color dominant
# by changing 'k' elements.

# ALGO:
# 1. Find the minimum count between blue and red colors (minCol)
# 2. Calculate how many more changes we need (diff) by subtracting minCol from k
# 3. If diff is greater than minCol:
#    - Return 1 (we can make a majority)
#    - Because we can change enough of the minority color to make the other color dominant
# 4. Otherwise:
#    - Return 0 (we cannot make a majority)
#    - Because we don't have enough changes to overcome the balance

def majorityColor(b: int, r: int, k: int) -> int:
   # Find the minimum between blue and red colors
   minCol = min(b, r)
   # Calculate how many more changes we need
   diff = k - minCol
   # If we can change more than the minimum color count
   if diff > minCol:
       return 1
   return 0
