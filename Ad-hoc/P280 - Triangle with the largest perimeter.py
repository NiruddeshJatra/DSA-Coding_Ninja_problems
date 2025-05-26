# Time Complexity:
# - O(n log n), where n is the number of elements in the array
# - Dominated by the sorting operation in descending order
# - The for loop runs at most (n-2) times, which is O(n)
# - Overall complexity is O(n log n) due to sorting
# Space Complexity:
# - O(1) auxiliary space if we don't count the input array
# - The sorting is done in-place, so no extra space for sorting
# - Only a few variables are used: loop index and temporary calculations

# INTUITION:
# The problem finds the maximum perimeter of a valid triangle from given side lengths
# Key insights:
# - A valid triangle must satisfy the triangle inequality: sum of any two sides > third side
# - For maximum perimeter, we want the largest possible valid triangle
# - By sorting in descending order, we can greedily check from largest to smallest
# - For three sides a ≥ b ≥ c, we only need to check if a < b + c (other inequalities are automatically satisfied)
# - The first valid triangle we find will have the maximum perimeter

# Example:
# side_lengths = [4, 6, 3, 7, 2], array_size = 5
# After sorting in descending order: [7, 6, 4, 3, 2]
# Check triplets:
# - (7, 6, 4): Is 7 < 6 + 4? Yes, 7 < 10 ✓ Valid triangle
# - Perimeter = 7 + 6 + 4 = 17
# - This is the first valid triangle, so it has maximum perimeter
# Return 17

# ALGO:
# 1. Sort the array in descending order to prioritize larger side lengths
# 2. Iterate through all possible triplets starting from the largest elements:
#    - Take three consecutive elements as potential triangle sides
#    - Check triangle inequality: largest_side < sum of other two sides
#    - Since array is sorted, we only need to check one inequality condition
# 3. Return the perimeter of the first valid triangle found (guaranteed to be maximum)
# 4. If no valid triangle exists, return 0

from os import *
from sys import *
from collections import *
from math import *

def maxPerimeterTriangle(side_lengths, array_size):
    # Sort in descending order to check largest possible triangles first
    side_lengths.sort(reverse=True)

    # Check all possible consecutive triplets for valid triangles
    for current_index in range(array_size - 2):
        largest_side = side_lengths[current_index]
        middle_side = side_lengths[current_index + 1]
        smallest_side = side_lengths[current_index + 2]
        
        # Check triangle inequality: largest side < sum of other two sides
        if largest_side < middle_side + smallest_side:
            # Found valid triangle, return its perimeter (guaranteed to be maximum)
            return largest_side + middle_side + smallest_side

    # No valid triangle found
    return 0
