import heapq
def getFourthLargest(arr, n):
    heap = []
    if len(arr) < 4:
        return -2147483648

    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > 4:
            heapq.heappop(heap)

    return heap[0]
