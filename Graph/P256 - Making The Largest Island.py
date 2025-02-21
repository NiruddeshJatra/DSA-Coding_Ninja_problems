# Time Complexity:
# - O(M*N) where M and N are the dimensions of the grid
# - Each cell is visited at most once during painting
# - Each 0 cell is visited once during the second pass to check neighbors

# Space Complexity:
# - O(M*N) for recursion stack in worst case
# - O(K) for componentSize dictionary where K is number of islands
# - Grid is modified in place

# INTUITION:
# This is a graph coloring + flood fill approach to solve the same problem as above.
# Instead of using Union-Find, we:
# 1. Color each connected component (island) with a unique color
# 2. Keep track of the size of each colored component
# 3. Check each 0 cell to see what size island we'd get by converting it
#
# Example:
# [1,0,1]    [2,0,3]
# [0,0,0] -> [0,0,0]  # After coloring
# [1,0,1]    [4,0,5]
#
# Color sizes: {2:1, 3:1, 4:1, 5:1}
# Check center 0: Would connect components 2,3,4,5 -> size 5
# Check other 0s: Would connect 2 components each -> size 3
# Answer: 5

# ALGO:
# 1. Define DFS function to paint connected components
#    - Recursively color all connected 1s with same color
#    - Track size of each colored component
# 2. First pass: Color all islands
#    - Assign unique color to each island
#    - Build map of color -> component size
# 3. Second pass: Try converting each 0
#    - For each 0 cell, check unique colors of neighbors
#    - Calculate total size if converting this cell
#    - Keep track of maximum possible size
# 4. Return maximum size found

from typing import List 
from collections import defaultdict

def maximumIslandSize(grid: List[List[int]]) -> int:
   # Directions array for moving in 4 directions
   DIRECTIONS = [0, 1, 0, -1, 0]
   rows, cols = len(grid), len(grid[0])
   nextColor = 2  # Start colors from 2 to distinguish from 0,1
   colorToSize = defaultdict(int)
   
   def paintComponent(row: int, col: int, color: int) -> None:
       # Base cases: out of bounds or not island cell
       if (row < 0 or row >= rows or 
           col < 0 or col >= cols or 
           grid[row][col] != 1):
           return
       
       # Paint current cell and increment component size
       grid[row][col] = color
       colorToSize[color] += 1
       
       # Recursively paint all 4 neighbors
       for i in range(4):
           paintComponent(row + DIRECTIONS[i], 
                        col + DIRECTIONS[i + 1], 
                        color)
   
   # First pass: Color all islands with unique colors
   for row in range(rows):
       for col in range(cols):
           if grid[row][col] != 1:
               continue
           paintComponent(row, col, nextColor)
           nextColor += 1
   
   # If no components found, return 0
   maxSize = max(colorToSize.values() or [0])
   
   # Second pass: Try converting each 0 cell
   for row in range(rows):
       for col in range(cols):
           if grid[row][col] != 0:
               continue
               
           # Find unique colors of neighboring components
           neighborColors = set()
           for i in range(4):
               newRow, newCol = row + DIRECTIONS[i], col + DIRECTIONS[i + 1]
               if (newRow < 0 or newRow >= rows or 
                   newCol < 0 or newCol >= cols or 
                   grid[newRow][newCol] == 0):
                   continue
               neighborColors.add(grid[newRow][newCol])
           
           # Calculate size if we convert this cell
           potentialSize = 1  # Count current cell
           for color in neighborColors:
               potentialSize += colorToSize[color]
           maxSize = max(maxSize, potentialSize)
   
   return maxSize
