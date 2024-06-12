"""
### Problem
Given an array of integers `arr` and an integer `k`, find the number of unique combinations in the array that sum up to `k`. Each number in the array may only be used once in the combination.

### Intuition
To solve this problem, we use a backtracking approach. The idea is to recursively explore all possible combinations of elements in the array and count those that sum up to `k`. By iterating through the `arr` and including or excluding each element, we can generate all possible combinations and their sums.

### Approach
1. **Sorting**: First, we sort the array to facilitate efficient pruning of the search space.
2. **Backtracking**: We define a recursive function `backtrack` that will try to build combinations starting from a given index:
   - **Base Case**: If the current sum equals `k`, increment the count of valid combinations.
   - **Pruning**: If the current sum exceeds `k`, terminate that path early.
3. **Recursive Exploration**: For each element in the array starting from the current index:
   - Add the element to the current sum and recursively call `backtrack` with the next index.
   - Skip further exploration if adding the element exceeds the target.
4. **Nonlocal Variable**: We use a nonlocal variable `ans` to keep track of the number of valid combinations found.

### Time Complexity
The time complexity is \(O(2^n)\) in the worst case, where \(n\) is the number of elements in `arr`, due to the exploration of all subsets. Sorting the array adds a complexity of \(O(n \log n)\).

### Space Complexity
The space complexity is \(O(n)\) due to the recursion stack and the space needed to store intermediate sums.

### Algorithm
1. Initialize `ans` as 0 to count valid combinations.
2. Define the `backtrack` function:
   - If the current sum equals `k`, increment `ans`.
   - If the current sum exceeds `k`, return to prune this path.
3. Sort the `arr`.
4. Call `backtrack` starting from index 0 with an initial sum of 0.
5. Return the count of valid combinations.
"""

from typing import List

def findWays(arr: List[int], k: int) -> int:
    ans = 0
    
    def backtrack(start, curSum):
        nonlocal ans
        if curSum >= k:
            if curSum == k:
                ans += 1
            return

        for i in range(start, len(arr)):
            tempSum = curSum + arr[i]
            if tempSum <= k:
                backtrack(i + 1, tempSum)
            else:
                break

    arr.sort()
    backtrack(0, 0)
    return ans
