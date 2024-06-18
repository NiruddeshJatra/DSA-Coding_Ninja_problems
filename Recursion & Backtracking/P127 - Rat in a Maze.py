"""
### Problem
Given a binary maze represented by a 2D list `arr` of size `n x n`, where `1` represents a path and `0` represents a wall, find all possible paths from the top-left corner (0,0) to the bottom-right corner (n-1,n-1). The paths should be returned as a list of strings where each string represents a sequence of moves ('D' for down, 'U' for up, 'R' for right, 'L' for left).

### Intuition
To find all possible paths from the start to the end in a maze, we can use backtracking. Starting from the top-left corner, we explore all possible directions (down, up, right, left) recursively while marking the path taken.

### Approach
1. **Safety Check**: Define a helper function `isSafe` to check if a cell `(r, c)` is within bounds and is a path (`arr[r][c] == 1`).
2. **Backtracking Function**: Define a recursive function `backtrack` to explore all paths:
   - If the current cell is the bottom-right corner `(n-1, n-1)`, append the current path to the result list `ans`.
   - Mark the current cell as visited by setting `arr[r][c]` to 0.
   - Explore all four possible directions (down, up, right, left) and backtrack after exploring each path by removing the last move from `path` and restoring the cell value.
3. **Initialization**: Start the backtracking process from the top-left corner `(0, 0)`.
4. **Return**: Return the list of all possible paths.

### Time Complexity
The time complexity is O(4^(n^2)), as each cell has up to 4 possible moves and there are n^2 cells.

### Space Complexity
The space complexity is O(n^2) due to the recursion stack and the path list used for backtracking.

### Algorithm
1. Define the `isSafe` function to check if a cell is within bounds and is a path.
2. Define the `backtrack` function:
   - If the current cell is the bottom-right corner, append the current path to `ans`.
   - Mark the current cell as visited.
   - Explore all possible directions and backtrack after each move.
3. Initialize and start the backtracking process.
4. Return the result list.
"""

from os import *
from sys import *
from collections import *
from math import *

def searchMaze(arr, n):
    def isSafe(r, c):
        return (0 <= r < n) and (0 <= c < n) and arr[r][c] == 1
    
    ans, path = [], []
    
    def backtrack(r, c):
        if r == n - 1 and c == n - 1:
            ans.append("".join(path))
            return
        
        temp = arr[r][c]
        arr[r][c] = 0
        
        if isSafe(r + 1, c):
            path.append("D")
            backtrack(r + 1, c)
            path.pop()
        
        if isSafe(r - 1, c):
            path.append("U")
            backtrack(r - 1, c)
            path.pop()
        
        if isSafe(r, c + 1):
            path.append("R")
            backtrack(r, c + 1)
            path.pop()
        
        if isSafe(r, c - 1):
            path.append("L")
            backtrack(r, c - 1)
            path.pop()
        
        arr[r][c] = temp
    
    backtrack(0, 0)
    return ans
