"""
### Problem
Given a list of integers `nums`, find all possible subset sums. The solution should return a list of all subset sums sorted in non-decreasing order.

### Intuition
To solve this problem, we use a backtracking approach. The idea is to recursively explore all possible subsets and calculate their sums. By iterating through the `nums` list and including or excluding each element, we can generate all possible subsets and their corresponding sums.

### Approach
1. Initialize an empty list `ans` to store the sums of subsets and an empty list `temp` to store the current subset.
2. Define a helper function `backtrack` that takes the current starting index:
   - Append the sum of the current subset to the result list.
   - Iterate through the `nums` starting from the given index.
   - Include the current element in the subset and recursively call `backtrack` for the next index.
   - Exclude the current element from the subset to backtrack.
3. Call the `backtrack` function starting from index 0.
4. Return the sorted list of subset sums.

### Time Complexity
The time complexity is \(O(2^n \log(2^n))\), where \(n\) is the number of elements in `nums`. This is because we generate all possible subsets (which is \(2^n\) subsets) and then sort the list of sums.

### Space Complexity
The space complexity is \(O(2^n)\) due to the space needed to store the sums of all subsets in the `ans` list.

### Algorithm
1. Initialize `ans` as an empty list to store subset sums.
2. Initialize `temp` as an empty list to store the current subset.
3. Define the `backtrack` function:
   - Append the sum of the current subset to `ans`.
   - Iterate through `nums` starting from the current index.
   - Add the current element to `temp`.
   - Recursively call `backtrack` with the next index.
   - Remove the last element from `temp` to backtrack.
4. Call `backtrack` starting from index 0.
5. Return the sorted list of subset sums.
"""

from typing import List

def subsetSum(nums: List[int]) -> List[int]:
    ans, temp = [], []
    
    def backtrack(start):
        ans.append(sum(temp[:]))

        for i in range(start, len(nums)):
            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()

    backtrack(0)
    return sorted(ans)
