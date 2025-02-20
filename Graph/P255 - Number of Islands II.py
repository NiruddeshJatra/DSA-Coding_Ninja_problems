# Time Complexity:
# - O(Q × α(Q)) where Q is the number of queries
# - Each query involves up to 4 union operations
# - Each union/find operation takes amortized O(α(Q)) time where α is the inverse Ackermann function

# Space Complexity:
# - O(Q) for storing parent dictionary and result array
# - Each land cell takes O(1) space in the parent dictionary

# INTUITION:
# We need to add land cells one by one and track the number of islands.
# When a new land cell is added, it either:
# 1. Forms a new island (if no adjacent land cells)
# 2. Joins existing island(s) (merging them if multiple adjacent)
#
# Example:
# n=3, m=3, queries=[(0,0), (1,1), (0,1)]
# (0,0): New island, count=1
#   [1][0][0]
#   [0][0][0]
#   [0][0][0]
#
# (1,1): New island, count=2
#   [1][0][0]
#   [0][1][0]
#   [0][0][0]
#
# (0,1): Connects islands, count=1
#   [1][1][0]
#   [0][1][0]
#   [0][0][0]

# ALGO:
# 1. Initialize empty parent dictionary and island count
# 2. For each query (x,y):
#    - If cell already exists, continue
#    - Add new cell to parent dictionary
#    - Increment island count
#    - Check all 4 adjacent cells:
#      * If adjacent cell exists, union with current cell
#      * Each successful union decrements island count
# 3. Return array of island counts after each query

def numOfIslandsII(n: int, m: int, q: List[List[int]]) -> List[int]:
   # Dictionary to track parent of each land cell
   parent = {}
   # Current count of islands
   islandCount = 0
   # Directions for checking adjacent cells
   directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   # Result array to store island count after each query
   result = []
   
   def findParent(node):
       # Path compression: point each node directly to root
       if parent[node] != node:
           parent[node] = findParent(parent[node])
       return parent[node]
       
   def union(cell1, cell2):
       nonlocal islandCount
       parentOfCell1 = findParent(cell1)
       parentOfCell2 = findParent(cell2)
       
       # If different islands, merge them
       if parentOfCell1 != parentOfCell2:
           parent[parentOfCell2] = parentOfCell1
           islandCount -= 1  # Decrease island count when merging
   
   # Process each query
   for x, y in q:
       # Skip if cell already exists
       if (x, y) in parent:
           result.append(islandCount)
           continue
       
       # Add new land cell
       parent[(x, y)] = (x, y)
       islandCount += 1
       
       # Check all adjacent cells
       for dx, dy in directions:
           newX, newY = x + dx, y + dy
           # If adjacent cell is valid and exists
           if 0 <= newX < n and 0 <= newY < m and (newX, newY) in parent:
               union((x, y), (newX, newY))
       
       result.append(islandCount)
   
   return result
