# Time Complexity:
# - O(N log K), where N is the total number of elements in all arrays, and K is the number of arrays.
#   - Each element is pushed and popped from the heap once, and each heap operation takes O(log K).

# Space Complexity:
# - O(K), for the heap that stores one element from each of the K arrays at any time.

# INTUITION:
# The goal is to merge K sorted arrays into a single sorted array. By using a min-heap, we can efficiently track the smallest 
# element among the heads of all arrays. This allows us to construct the resulting merged array in sorted order.

# ALGO:
# 1. Initialize an empty min-heap.
# 2. Add the first element of each array (along with its value, array index, and element index) to the heap.
# 3. Extract the smallest element from the heap, append it to the result array, and push the next element from the same array (if it exists) into the heap.
# 4. Repeat the process until the heap is empty.
# 5. Return the merged sorted array.

from sys import *
from collections import *
from math import *
import heapq

def mergeKSortedArrays(kArrays, k: int):
    heap = []
    
    # Add the first element of each array to the heap
    for i in range(len(kArrays)):
        if kArrays[i]:  # Check if the array is non-empty
            heapq.heappush(heap, (kArrays[i][0], i, 0))

    ans = []

    # Process elements from the heap
    while heap:
        value, i, j = heapq.heappop(heap)
        ans.append(value)
        j += 1
        if j < len(kArrays[i]):  # If there are more elements in the array
            heapq.heappush(heap, (kArrays[i][j], i, j))

    return ans
