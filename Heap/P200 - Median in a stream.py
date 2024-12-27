# Time Complexity:
# - O(N log N) where N is the length of array
#   - For each element in array:
#     * Two heap operations (push/pop): O(log N)
#   - Total N elements: O(N log N)
#   - Final median calculation: O(1)

# Space Complexity:
# - O(N) where N is length of array
#   - Two heaps each storing roughly N/2 elements
#   - small heap stores lower half of numbers
#   - large heap stores upper half of numbers

# INTUITION:
# To find median of array efficiently:
# - Split numbers into two halves using heaps
# - small (max heap) stores lower half
# - large (min heap) stores upper half
# - Keep heaps balanced (diff in size ≤ 1)
# The median will be either:
# - Average of tops when heaps equal size
# - Top of large heap when sizes differ

# ALGO:
# 1. Initialize two heaps:
#    - small: max heap for lower half
#    - large: min heap for upper half
# 2. For each number in array:
#    - If heaps equal size:
#      * Add to small, move max to large
#    - Else:
#      * Add to large, move min to small
# 3. Find median:
#    - If equal size: average of tops
#    - If unequal: top of large heap

import heapq
def findMedian(arr, n):
   # Initialize heaps
   small = []  # max heap (using negatives)
   large = []  # min heap
   
   # Process each number
   for num in arr:
       if len(small) == len(large):
           # Add to small, move largest to large
           heapq.heappush(large, -heapq.heappushpop(small, -num))
       else:
           # Add to large, move smallest to small
           heapq.heappush(small, -heapq.heappushpop(large, num))
   
   # Calculate median
   if len(small) == len(large):
       return (-small[0] + large[0]) // 2
   else:
       return large[0]
