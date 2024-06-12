"""
### Problem
Given an array of integers `arr` and an integer `k`, find the number of unique combinations in the array that sum up to `k`. Each number in the array may only be used once in the combination.

### Intuition
To solve this problem, we use a backtracking approach. The idea is to recursively explore all possible combinations of elements in the array and count those that sum up to `k`. By iterating through the `arr` and including or excluding each element, we can generate all possible combinations and their sums.

### Approach
1. Initialize an empty list `temp` to store the current combination and a variable `ans` to count valid combinations.
2. Define a helper function `backtrack` that takes the current starting index:
   - If the sum of the current combination is equal to `k`, increment the count of valid combinations.
   - Iterate through the `arr` starting from the given index.
   - Include the current element in the combination and recursively call `backtrack` for the next index.
   - Exclude the current element from the combination to backtrack.
3. Call the `backtrack` function starting from index 0.
4. Return the count of valid combinations.

### Time Complexity
The time complexity is \(O(2^n)\), where \(n\) is the number of elements in `arr`. This is because we generate all possible subsets (which is \(2^n\) subsets).

### Space Complexity
The space complexity is \(O(n)\) due to the space needed to store the current combination in the `temp` list.

### Algorithm
1. Initialize `ans` as 0 to count valid combinations.
2. Initialize `temp` as an empty list to store the current combination.
3. Define the `backtrack` function:
   - If the sum of the current combination is equal to `k`, increment `ans`.
   - Iterate through `arr` starting from the current index.
   - Add the current element to `temp`.
   - Recursively call `backtrack` with the next index.
   - Remove the last element from `temp` to backtrack.
4. Call `backtrack` starting from index 0.
5. Return the count of valid combinations.
"""

from typing import List

def findWays(arr: List[int], k: int) -> int:
    temp = []
    ans = 0

    def backtrack(start):
        nonlocal ans  # Indicate that ans is defined in the enclosing scope
        if sum(temp[:]) == k:
            ans += 1
            return

        for i in range(start, len(arr)):
            temp.append(arr[i])
            backtrack(i+1)
            temp.pop()

    backtrack(0)
    return ans
