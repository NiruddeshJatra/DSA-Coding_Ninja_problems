import heapq

def findMedian(arr, n):
    result = []
    minHeap = []  # store large numbers
    maxHeap = []  # store small numbers

    for num in arr:
        heapq.heappush(maxHeap, -num)

        if (minHeap and maxHeap and minHeap[0] < (-1 * maxHeap[0])):
            val = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)

        if len(minHeap) > len(maxHeap) + 1:
            val = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)

        if len(maxHeap) > len(minHeap) + 1:
            val = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)

        if len(minHeap) > len(maxHeap):
            result.append(minHeap[0])
        elif len(maxHeap) > len(minHeap):
            result.append(-maxHeap[0])
        else:
            result.append((minHeap[0] + -maxHeap[0]) //2)

    for median in result:
        print(median, end=" ")
