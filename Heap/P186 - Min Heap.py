# Time Complexity:
# - Insertion (insert): O(log(N)), where N is the current number of elements in the heap.
#   - Each insertion involves adding the new element at the end and then heapifying up, which takes O(log(N)) time.
# - Deletion (delete): O(log(N)), where N is the current number of elements in the heap.
#   - Each deletion involves removing the root and then heapifying down, which takes O(log(N)) time.
# - Processing all queries: O(Q * log(N)), where Q is the number of queries, since each query is either an insert or a delete.

# Space Complexity: O(N), where N is the maximum number of elements in the heap.
# - The heap is stored in a list, which requires O(N) space.

# INTUITION:
# A min-heap is a binary tree-based data structure where the smallest element is always at the root. 
# It supports efficient insertion and deletion of the smallest element. The heap is implemented using a list, 
# and elements are organized such that every parent node is smaller than its child nodes.
# This problem requires implementing a min-heap to handle a series of queries involving insertions and deletions 
# of the minimum element.

# ALGO:
# 1. Initialize an empty list `heap` to represent the min-heap.
# 2. Define helper functions:
#    - `heapify_up`: Ensures the heap property is maintained after an insertion by swapping the inserted element 
#      with its parent as needed.
#    - `heapify_down`: Ensures the heap property is maintained after a deletion by swapping the root element 
#      with its smaller child as needed.
# 3. Define operations:
#    - `insert(val)`: Adds the value `val` to the heap and calls `heapify_up`.
#    - `delete()`: Removes and returns the smallest element (root) from the heap and calls `heapify_down`.
# 4. Process the input queries:
#    - For `query[0] == 0`: Insert the value `query[1]` into the heap.
#    - For `query[0] == 1`: Delete the minimum element from the heap and append it to the result list.
# 5. Return the result list containing the values returned by deletion queries.

from sys import *
from collections import *
from math import *

def minHeap(N, Q: [[]]):
    heap = []

    def heapify_up(index):
        parent = (index - 1) // 2
        while index > 0 and heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(index):
        left = index * 2 + 1
        right = left + 1
        smallest = index
        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right
        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            heapify_down(smallest)

    def insert(val):
        heap.append(val)
        heapify_up(len(heap) - 1)

    def delete():
        minVal = heap[0]
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        heapify_down(0)
        return minVal

    # Process queries and collect results
    result = []
    for query in Q:
        if query[0] == 0:  # Insert query
            insert(query[1])
        elif query[0] == 1:  # Delete query
            result.append(delete())

    return result
