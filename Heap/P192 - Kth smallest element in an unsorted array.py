# Time Complexity:
# - Building the heap: O(N log K), where N is the size of the array and K is the kth smallest element to find.
#   - Each insertion and removal operation in the heap takes O(log K).

# Space Complexity:
# - O(K), for the max-heap that stores K smallest elements (negative values).

# INTUITION:
# To find the Kth smallest element in an array, we use a max-heap of size K. The heap stores the K smallest elements seen so far, 
# with the largest of these K elements at the root. This ensures that as we iterate through the array, larger elements are discarded.

# ALGO:
# 1. Initialize an empty max-heap.
# 2. Iterate through each number in the array:
#    - Push the negative of the number into the heap to simulate a max-heap using Python's min-heap.
#    - If the size of the heap exceeds K, remove the largest element (root of the heap, stored as the smallest negative number).
# 3. At the end of the iteration, the root of the heap contains the Kth smallest element in its negative form.
# 4. Return the negation of the root to get the Kth smallest element.

import heapq

def kthSmallestElement(arr, n, k):
    heap = []

    for num in arr:
        heapq.heappush(heap, -num)  # Push negative values to create a max-heap
        if len(heap) > k:
            heapq.heappop(heap)  # Remove the largest of the K smallest elements

    return -heap[0]  # The root of the heap is the negative of the Kth smallest element
