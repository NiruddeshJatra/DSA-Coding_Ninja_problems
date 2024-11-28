# Time Complexity: O(n^2 * log(k)), where n is the length of `arr` and k is the input value.  
# - Generating all subarray sums takes O(n^2).  
# - Each insertion or removal operation in the heap takes O(log(k)), and since we perform these operations for all subarray sums, the total is O(n^2 * log(k)).

# Space Complexity: O(k).  
# - The size of the heap is at most k, so it uses O(k) space.

# INTUITION:  
# The task is to find the k-th largest subarray sum from all possible subarrays of the array.  
# - We generate all subarray sums by iterating over all possible starting and ending indices.  
# - To efficiently keep track of the k largest sums, we use a min-heap of size k.  
#   - If the heap grows beyond size k, the smallest element is removed to ensure that only the k largest sums are retained.  
# - At the end, the root of the heap (minimum value in the heap) is the k-th largest subarray sum.

# This approach ensures that we do not need to sort all subarray sums, making it more efficient for large arrays and large k values.

# ALGORITHM:  
# 1. Initialize an empty min-heap to store the k largest subarray sums.  
# 2. Iterate through all possible starting indices of subarrays.  
# 3. For each starting index, calculate the sum of all subarrays ending at subsequent indices:  
#    - Push each subarray sum into the heap.  
#    - If the heap size exceeds k, remove the smallest element to maintain its size as k.  
# 4. Return the root of the heap, which is the k-th largest subarray sum.

import heapq

def getKthLargest(arr, k):
    minHeap = []

    # Generate all subarray sums
    for start in range(len(arr)):
        currentSum = 0
        for end in range(start, len(arr)):
            currentSum += arr[end]

            # Maintain a heap of size k
            heapq.heappush(minHeap, currentSum)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

    # The root of the heap is the k-th largest sum
    return minHeap[0]

# Example Usage:
# Input: arr = [3, 2, 1], k = 2
# Output: 5
# Explanation: The subarray sums are [3, 5, 6, 2, 3, 1]. The 2nd largest sum is 5.
