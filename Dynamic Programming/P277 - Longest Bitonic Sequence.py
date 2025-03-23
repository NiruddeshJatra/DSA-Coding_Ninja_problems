from typing import List

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
   # Time Complexity:
   # - O(n²) where n is the length of the input array
   # - We use nested loops twice, each with the outer loop running n times and inner loop running up to n times
   
   # Space Complexity:
   # - O(n) for the two dp arrays that track increasing and decreasing subsequence lengths
   
   # INTUITION:
   # A bitonic subsequence is one that first increases and then decreases. To find the longest such subsequence,
   # we can break this problem into two parts:
   # 1. Find the longest increasing subsequence (LIS) ending at each position
   # 2. Find the longest decreasing subsequence (LDS) starting at each position
   # 
   # For any position i, the length of the longest bitonic subsequence with peak at position i will be:
   # LIS ending at i + LDS starting at i - 1 (we subtract 1 because the element at position i is counted twice)
   #
   # For example, with array [1, 11, 2, 10, 4, 5, 2, 1]:
   # - dp1 (LIS ending at each index): [1, 2, 2, 3, 3, 4, 2, 2]
   # - dp2 (LDS starting at each index): [4, 3, 3, 2, 2, 1, 1, 1]
   # - At index 0: bitonic length = 1 + 4 - 1 = 4 (subsequence: [1, 11, 4, 2, 1])
   # - At index 5: bitonic length = 4 + 1 - 1 = 4 (subsequence: [1, 2, 4, 5])
   # The maximum length is 4.
   
   # ALGO:
   # 1. Initialize two arrays:
   #    a. dp1[i] represents the length of the LIS ending at index i
   #    b. dp2[i] represents the length of the LDS starting at index i
   # 2. Fill the dp1 array (LIS calculation) by iterating forward:
   #    a. For each position i, check all previous positions j
   #    b. If arr[i] > arr[j], update dp1[i] if it gives a longer subsequence
   # 3. Fill the dp2 array (LDS calculation) by iterating backward:
   #    a. For each position i, check all future positions j
   #    b. If arr[i] > arr[j], update dp2[i] if it gives a longer subsequence
   # 4. For each position i, calculate the length of the bitonic subsequence with peak at i:
   #    length = dp1[i] + dp2[i] - 1
   # 5. Return the maximum of these lengths
   
   # Initialize arrays for tracking lengths of increasing and decreasing subsequences
   dp1 = [1] * n  # dp1[i] = length of LIS ending at index i
   dp2 = [1] * n  # dp2[i] = length of LDS starting at index i
   
   # Variable to track the maximum bitonic subsequence length
   maxLength = 1
   
   # Calculate LIS (Longest Increasing Subsequence) ending at each position
   for i in range(n):
       for j in range(i):
           # If the current element is greater than a previous element
           # and including it leads to a longer increasing subsequence
           if arr[i] > arr[j] and dp1[j] + 1 > dp1[i]:
               dp1[i] = dp1[j] + 1
   
   # Calculate LDS (Longest Decreasing Subsequence) starting at each position
   # by traversing the array in reverse
   for i in range(n-1, -1, -1):
       for j in range(n-1, i, -1):
           # If the current element is greater than a future element
           # and including it leads to a longer decreasing subsequence
           if arr[i] > arr[j] and dp2[j] + 1 > dp2[i]:
               dp2[i] = dp2[j] + 1
       
       # Calculate the length of the bitonic subsequence with peak at position i
       # We subtract 1 because the element at position i is counted in both dp1 and dp2
       bitonicLength = dp1[i] + dp2[i] - 1
       
       # Update the maximum length found so far
       maxLength = max(maxLength, bitonicLength)
   
   return maxLength
