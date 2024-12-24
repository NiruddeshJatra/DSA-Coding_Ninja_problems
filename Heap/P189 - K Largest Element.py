# Time Complexity:
# - Building the heap: O(N log K), where N is the size of the array and K is the number of largest elements to find.
#   - Each insertion and removal operation in the heap takes O(log K).
# - Sorting the final heap: O(K log K).

# Space Complexity:
# - O(K), for the heap that stores the K largest elements.

# INTUITION:
# To find the K largest elements in an array efficiently, we use a min-heap of size K. The heap always keeps the K largest elements 
# seen so far, with the smallest of these K elements at the root. This ensures that as we iterate through the array, smaller elements 
# are discarded.

# ALGO:
# 1. Initialize an empty heap.
# 2. Iterate through each number in the array:
#    - Push the number into the heap.
#    - If the size of the heap exceeds K, remove the smallest element (root of the heap).
# 3. At the end of the iteration, the heap contains the K largest elements.
# 4. Sort the heap to return the K largest elements in ascending order.

from os import *
from sys import *
from collections import *
from math import *
import heapq

def Klargest(a, k, n):
    heap = []

    for num in a:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    # Replace the usage of `sorted` to sort the heap
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    return result[::-1]  # Reverse the list to return the K largest elements in ascending order
