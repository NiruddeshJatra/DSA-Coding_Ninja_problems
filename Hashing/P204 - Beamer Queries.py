# Time Complexity:
# - O(N + QK) where N is array length, Q is queries, K is average query range
#   - Building Counter: O(N)
#   - Processing Q queries, each handling K elements: O(QK)

# Space Complexity:
# - O(N) for Counter and results array
#   - Counter stores up to N elements
#   - Results array stores Q answers

# INTUITION:
# To check if removing elements leaves exactly 3 distinct:
# - Use Counter to track frequencies
# - For each query range, temporarily remove elements 
# - Check if remaining distinct count is 3
# - Restore frequencies after each query

# ALGO:
# 1. Build frequency Counter of array
# 2. For each query [l,r]:
#    - Remove elements in range temporarily
#    - Count elements reduced to zero
#    - Check if remaining distinct is 3
#    - Restore frequencies
# 3. Return results array

from typing import List
from collections import Counter

def beamerQueries(n: int, q: int, a: List[int], queries: List[List[int]]) -> List[int]:
   freq = Counter(a)
   distinctCount = len(freq)
   ans = []

   for l, r in queries:
       tempRemoved = 0
       
       # Temporarily remove elements in range
       for i in range(l, r+1):
           freq[a[i]] -= 1
           if freq[a[i]] == 0:
               tempRemoved += 1
       
       # Check if exactly 3 distinct remain
       if distinctCount - tempRemoved == 3:
           ans.append(1)
       else:
           ans.append(0)
           
       # Restore frequencies
       for i in range(l, r+1):
           freq[a[i]] += 1

   return ans
