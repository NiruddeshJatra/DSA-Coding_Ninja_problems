# Time Complexity:
# - O(n log n), where n is the number of elements in the array
# - Dominated by the sorting operation of the array
# - The while loop runs at most n/K times, which is O(n)
# - Overall complexity is O(n log n) due to sorting
# Space Complexity:
# - O(1) auxiliary space if we don't count the input array
# - The sorting is done in-place, so no extra space for sorting
# - Only a few variables are used: remaining_elements, min_total, max_total, current_index

# INTUITION:
# The problem involves selecting elements from an array with some constraint related to K
# Key insights:
# - We sort the array to have access to smallest and largest elements efficiently
# - We select elements in a pattern where we skip K elements after each selection
# - We track both minimum and maximum possible totals by selecting from opposite ends
# - The algorithm handles the case where K=0 as a special case (select all elements)

# Example:
# array = [1, 3, 5, 7, 9], K = 2
# After sorting: [1, 3, 5, 7, 9]
# Selection pattern with K=2 (skip 2 elements after each selection):
# - Select index 0 (value 1) for min, index 4 (value 9) for max
# - Remaining elements = 5-2 = 3, next selection at index 1
# - Select index 1 (value 3) for min, index 3 (value 7) for max
# - Remaining elements = 3-2 = 1, next selection at index 2
# - Select index 2 (value 5) for both min and max
# Result: min_total = 1+3+5 = 9, max_total = 9+7+5 = 21

# ALGO:
# 1. Handle special case: if K=0, return (sum of all elements, sum of all elements)
# 2. Sort the array in ascending order to enable efficient min/max selection
# 3. Initialize tracking variables:
#    - remaining_elements: tracks how many elements are left to consider
#    - min_total, max_total: accumulate the sums for minimum and maximum cases
#    - current_index: tracks current position in the selection pattern
# 4. While there are elements remaining and we haven't exceeded array bounds:
#    - Add smallest available element (from start) to min_total
#    - Add largest available element (from end) to max_total
#    - Move to next selection position
#    - Reduce remaining elements by K (skip K elements)
# 5. Return tuple of (min_total, max_total)

from sys import *
from collections import *
from math import *
from typing import *

def problemSelection(score_array: List[int], skip_count: int) -> tuple[int, int]:
    # Special case: if no skipping, select all elements
    if skip_count == 0:
        total_sum = sum(score_array)
        return (total_sum, total_sum)

    # Sort array to enable efficient min/max element selection
    score_array.sort()
    
    remaining_elements = len(score_array)
    min_total = max_total = 0
    current_index = 0

    # Select elements with skip pattern until no more valid selections
    while remaining_elements > 0 and current_index < remaining_elements:
        # Select smallest available element for minimum total
        min_total += score_array[current_index]
        
        # Select largest available element for maximum total  
        max_total += score_array[-current_index - 1]
        
        # Move to next selection position
        current_index += 1
        
        # Reduce remaining elements by skip count
        remaining_elements -= skip_count

    return (min_total, max_total)
