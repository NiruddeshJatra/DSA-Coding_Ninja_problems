# Time Complexity:
# - O(N log N + K log K) where N is length of arrays and K is number of combinations needed
#   - Sorting two arrays: O(N log N)
#   - K heap operations, each O(log K): O(K log K)
#   - Each element can be pushed to heap at most once
#   - Overall complexity: O(N log N + K log K)

# Space Complexity:
# - O(K) additional space
#   - Heap stores at most K+2 elements at any time
#   - Set visited stores at most K+2 pairs
#   - Result array stores K elements
#   - Overall O(K)

# INTUITION:
# To find K max sum combinations:
# - Sort both arrays to start with maximum possible sum
# - Use max heap to track potential combinations
# - Similar to merge k sorted lists, but in 2D
# - For each sum, next potential maximum will be:
#   * Either using previous element from first array
#   * Or previous element from second array
# Track visited pairs to avoid duplicates

# ALGO:
# 1. Sort both arrays in ascending order
# 2. Initialize max heap with maximum possible sum (last elements)
# 3. Initialize visited set to track processed pairs
# 4. For K iterations:
#    - Pop maximum sum from heap
#    - Add two potential next maximum sums to heap:
#      * Using previous element from first array
#      * Using previous element from second array
#    - Track visited pairs
#    - Add current max to result
# 5. Return result array with K maximum sums

from typing import List
import heapq

def kMaxSumCombination(a: List[int], b: List[int], n: int, k: int) -> List[int]:
   # Initialize result array
   result = []
   
   # Sort arrays to get maximum elements at end
   a.sort()
   b.sort()
   
   # Initialize max heap and add maximum possible sum
   maxHeap = []
   heapq.heappush(maxHeap, (-(a[-1] + b[-1]), (n - 1, n - 1)))
   
   # Track visited pairs
   visited = set()
   visited.add((n - 1, n - 1))

   # Process K combinations
   while k > 0:
       # Get current maximum sum
       val, (i, j) = heapq.heappop(maxHeap)
       result.append(-val)
       k -= 1

       # Add potential next maximum using previous element from first array
       if i > 0 and (i-1, j) not in visited:
           heapq.heappush(maxHeap, (-(a[i-1] + b[j]), (i-1, j)))
           visited.add((i-1, j))
       
       # Add potential next maximum using previous element from second array
       if j > 0 and (i, j-1) not in visited:
           heapq.heappush(maxHeap, (-(a[i] + b[j-1]), (i, j-1)))
           visited.add((i, j-1))

   return result
