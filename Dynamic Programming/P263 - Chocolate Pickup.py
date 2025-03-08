from typing import List

def maximumChocolates(m: int, n: int, grid: List[List[int]]) -> int:
    """
    Intuition:
    Imagine two friends starting at the top row of a chocolate grid and moving to the bottom. 
    They can move left, right, or stay in the same column. 
    The goal is to maximize the chocolates collected by both friends without double-counting chocolates if they land on the same cell.

    We use dynamic programming, working from the bottom row to the top, and keep track of the maximum chocolates collected 
    for every possible position of both friends. For each cell, we check all possible movements for both friends 
    (left, stay, right) and take the maximum value.
    
    Approach:
    - Create a DP array `front` to store results for the current row.
    - Start from the last row and move upward, updating the DP array.
    - For each cell (i, j1) and (i, j2) (positions of the two friends), check all 9 possible movement combinations.
    - If both friends land on the same cell, count the chocolates only once.
    - Take the maximum value of all possible movements and update the DP array.
    - The final result will be stored in `front[0][n-1]`, representing the maximum chocolates collected starting from the first row.
    
    Time Complexity: O(m * n * n * 9) -> O(m * n^2)
    Space Complexity: O(n^2)
    """
    front = [[0] * (n + 1) for _ in range(n + 1)]

    for j1 in range(n):
        for j2 in range(n):
            front[j1][j2] = 0

    for i in range(m - 1, -1, -1):
        cur = [[0] * (n + 1) for _ in range(n + 1)]
        for j1 in range(n):
            for j2 in range(n):
                for dj1 in [-1, 0, 1]:
                    for dj2 in [-1, 0, 1]:
                        value = (
                            grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                        )
                        if 0 <= j1 + dj1 < n and 0 <= j2 + dj2 < n:
                            value += front[j1 + dj1][j2 + dj2]
                        cur[j1][j2] = max(cur[j1][j2], value)

        front = cur

    return front[0][n - 1]

# Let me know if you'd like me to refine this further or add examples! 🚀
