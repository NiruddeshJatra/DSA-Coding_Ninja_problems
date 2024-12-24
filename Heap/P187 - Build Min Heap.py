# Time Complexity:
# - Building the min-heap: O(N), where N is the number of elements in the heap.
#   - Each non-leaf node is heapified, and the cost of heapifying each node is proportional to its height. 
#   - This results in a linear time complexity for building the heap.

# Space Complexity:
# - O(1) additional space, as the heap is modified in place.

# INTUITION:
# A min-heap is a binary tree-based structure where the smallest element is always at the root. To build a min-heap 
# efficiently, we start heapifying from the last non-leaf node (bottom-up approach). This ensures that every subtree 
# satisfies the heap property.

# ALGO:
# 1. Define a helper function `heapify_down(index)` that ensures the subtree rooted at `index` satisfies the heap property:
#    - Compare the current node with its left and right children.
#    - Swap the current node with the smallest child if the heap property is violated, and recursively heapify the affected subtree.
# 2. Start from the last non-leaf node (`n // 2 - 1`) and move upwards to the root, calling `heapify_down` for each node.
#    - The last non-leaf node is determined because all nodes after it are leaf nodes, which inherently satisfy the heap property.
# 3. The input list `heap` is modified in place to satisfy the min-heap property.

from os import *
from sys import *
from collections import *
from math import *

def buildMinHeap(heap):
    def heapify_down(index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            heapify_down(smallest)

    n = len(heap)
    # Start from the last non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(i)
