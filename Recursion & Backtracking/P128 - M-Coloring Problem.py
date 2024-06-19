"""
### Problem
Given an undirected graph represented by an adjacency matrix `mat` of size `n x n`, determine if the graph can be colored using at most `m` colors such that no two adjacent nodes have the same color. If possible, return "YES"; otherwise, return "NO".

### Intuition
To solve the graph coloring problem, we use backtracking to try assigning colors to each node. We start with the first node and attempt to color it with one of the available `m` colors. We then move to the next node and repeat the process. If we find that we cannot color a node without violating the coloring rules, we backtrack and try a different color for the previous node.

### Approach
1. **Safety Check**: Define a helper function `isSafe` to check if a given color can be assigned to a node without violating the coloring rules.
2. **Backtracking Function**: Define a recursive function `backtrack` to try coloring the nodes one by one:
   - If all nodes are colored successfully, return True.
   - For each node, try assigning each of the `m` colors.
   - If a color is valid (checked using `isSafe`), assign it and proceed to the next node.
   - If the assignment leads to a solution, return True.
   - If no valid color assignment is found, reset the color and backtrack.
3. **Special Case for One Color**: If only one color is available (`m == 1`), check if the graph has any edges. If it does, return "NO" because it's impossible to color the graph with one color if there are edges. If there are no edges, return "YES".
4. **Initialization**: Initialize the colors list to store the color assigned to each node and start the backtracking process from the first node.
5. **Return**: If the backtracking function returns True, return "YES"; otherwise, return "NO".

### Time Complexity
The time complexity is O(m^n) in the worst case, where `n` is the number of nodes, and `m` is the number of colors. This is because we try each of the `m` colors for each of the `n` nodes.

### Space Complexity
The space complexity is O(n) due to the recursion stack and the colors list used to store the color assignments.

### Algorithm
1. Define the `isSafe` function to check if a color can be assigned to a node.
2. Define the `backtrack` function to try coloring the graph using backtracking.
3. Handle the special case where only one color is available.
4. Initialize the colors list and start the backtracking process.
5. Return the result based on the backtracking function's output.
"""

from typing import List

def graphColoring(mat: List[List[int]], m: int) -> str:
    n = len(mat)
    colors = [0] * n

    def isSafe(node, color):
        for i in range(n):
            if mat[node][i] == 1 and colors[i] == color:
                return False
        return True

    def backtrack(node):
        if node == n:
            return True

        for color in range(1, m + 1):
            if isSafe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0

        return False

    # Special case for m == 1
    if m == 1:
        for i in range(n):
            for j in range(i + 1, n):
                if mat[i][j] == 1:
                    return "NO"
        return "YES"

    if backtrack(0):
        return "YES"
    return "NO"
