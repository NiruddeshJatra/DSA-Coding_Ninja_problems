"""
### Problem
Given an array of integers `arr`, an integer `n` which is the length of the array, and an integer `k`, determine if there exists a subset of `arr` that sums up to `k`.

### Intuition
To determine if a subset with a sum of `k` exists, we use a backtracking approach. By recursively exploring each element in the array, either including or excluding it from the current subset, we can explore all possible subsets and check their sums.

### Approach
1. **Sorting**: First, sort the array to facilitate efficient pruning of the search space.
2. **Backtracking**: Define a recursive function `backtrack` to build subsets:
   - **Base Case**: If the current sum equals `k`, return `True`.
   - **Pruning**: If the current sum exceeds `k`, terminate that path early.
3. **Recursive Exploration**: For each element in the array starting from the current index:
   - Add the element to the current sum and recursively call `backtrack` with the next index.
   - Skip further exploration if adding the element exceeds the target.
4. **Termination**: Return `False` if no valid subset is found.

### Time Complexity
The time complexity is \(O(2^n)\) in the worst case, where \(n\) is the number of elements in `arr`, due to the exploration of all subsets. Sorting the array adds a complexity of \(O(n \log n)\).

### Space Complexity
The space complexity is \(O(n)\) due to the recursion stack.

### Algorithm
1. Define the `backtrack` function:
   - If the current sum equals `k`, return `True`.
   - If the current sum exceeds `k`, return `False` to prune this path.
2. Sort the `arr`.
3. Call `backtrack` starting from index 0 with an initial sum of 0.
4. Return the result of `backtrack`.
"""

from typing import *

def isSubsetPresent(n:int, k: int, arr: List[int]) -> bool:
    def backtrack(start, curSum):
        if curSum >= k:
            if curSum == k:
                return True

        for i in range(start, len(arr)):
            tempSum = curSum + arr[i]
            if tempSum <= k:
                if backtrack(i+1, tempSum):
                    return True
            else:
                break

        return False

    arr.sort()
    return backtrack(0, 0)
