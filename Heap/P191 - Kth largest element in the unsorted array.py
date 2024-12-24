import heapq
from sys import stdin, stdout


def kthLargest(arr, size, k):
    heap = []

    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
