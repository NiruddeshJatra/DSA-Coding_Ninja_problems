from typing import List

def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
   # Time Complexity:
   # - O(n²) where n is the length of the input array
   # - We use nested loops, with the outer loop running n times and inner loop running up to i times
   
   # Space Complexity:
   # - O(n) for the dp and prev arrays used to track LIS lengths and indices
   
   # INTUITION:
   # This function not only finds the length of the Longest Increasing Subsequence (LIS),
   # but also reconstructs and returns the actual subsequence itself. The key insight is that
   # we need to track not just the length of the LIS ending at each position, but also
   # the previous element in that subsequence.
   #
   # For example, with array [5, 2, 8, 6, 3, 6, 9, 7]:
   # - For index 0 (value 5): dp[0] = 1, prev[0] = -1 (just the single element)
   # - For index 1 (value 2): dp[1] = 1, prev[1] = -1 (can't extend from 5 since 2 < 5)
   # - For index 2 (value 8): dp[2] = 2, prev[2] = 1 (can extend from 2)
   # - For index 3 (value 6): dp[3] = 2, prev[3] = 1 (can extend from 2)
   # - And so on...
   #
   # At the end, we find the index with the maximum dp value (the end of the LIS),
   # then trace back using the prev array to reconstruct the entire subsequence.
   
   # ALGO:
   # 1. Initialize two arrays:
   #    a. dp[i] represents the length of the LIS ending at index i
   #    b. prev[i] represents the index of the previous element in the LIS ending at index i
   # 2. For each position i, check all previous positions j:
   #    a. If arr[i] > arr[j] and including arr[i] after arr[j] gives a longer subsequence,
   #       update dp[i] and prev[i]
   # 3. Find the index with the maximum dp value (the end of the LIS)
   # 4. Reconstruct the LIS by following the prev array from this index
   # 5. Reverse the result (since we built it backwards) and return it
   
   # Initialize dp array - dp[i] stores length of LIS ending at index i
   dp = [1] * n
   
   # Initialize prev array - prev[i] stores the previous index in the LIS
   prev = [-1] * n
   
   # Fill the dp and prev arrays
   for i in range(n):
       for j in range(i):
           # If current element is greater than previous element and
           # including it leads to a longer subsequence
           if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
               dp[i] = dp[j] + 1  # Update the length of LIS
               prev[i] = j        # Store the previous index in the LIS
   
   # Find the index where the LIS ends (the index with maximum dp value)
   maxLengthIndex = 0
   for i in range(n):
       if dp[i] > dp[maxLengthIndex]:
           maxLengthIndex = i
   
   # Reconstruct the LIS by following the prev array
   result = []
   currentIndex = maxLengthIndex
   
   # Trace back through the prev array until we reach the start of the LIS
   while currentIndex != -1:
       result.append(arr[currentIndex])  # Add current element to result
       currentIndex = prev[currentIndex] # Move to previous element in the LIS
   
   # Since we built the subsequence backwards, reverse it before returning
   return result[::-1]
