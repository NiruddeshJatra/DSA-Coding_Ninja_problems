# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - We need to visit each vertex once through DFS
# - At each vertex, we process all its edges once
# - The matrix representation means E = V^2 in worst case
# - Therefore worst case becomes O(V^2)

# Space Complexity:
# - O(V) for the recursion stack in worst case
# - O(V) for visited set and colored dictionary
# - O(V^2) for adjacency list representation from matrix
# - Overall space: O(V^2)

# INTUITION:
# Imagine you're planning a party and want to avoid inviting people who don't get along.
# You decide to split guests into two groups (let's say Team Red and Team Blue).
# For this to work:
# - If Alice and Bob don't get along, they must be on different teams
# - If Bob and Charlie don't get along, and Bob is on Team Blue, Charlie must be on Team Red
# - If this continues to work for all relationships, the graph is bipartite
#
# In graph theory terms:
# - Team Red and Team Blue represent our two colors (0 and 1)
# - Each edge represents a "conflict" requiring different colors
# - If we can color all vertices without any adjacent vertices sharing a color,
#   the graph is bipartite

# ALGORITHM:
# 1. Convert edge matrix to adjacency list for easier traversal
# 2. Use DFS with coloring:
#    - Start with any unvisited node, color it 0 (Team Red)
#    - Visit all neighbors, color them 1 (Team Blue)
#    - Continue DFS, alternating colors (using abs(color-1))
#    - If we ever find adjacent nodes with same color, return False
# 3. Check all components (some nodes might be disconnected)
# 4. Return True if all nodes can be properly colored

def isGraphBirpartite(edges):
   def dfs(currentNode, currentColor):
       # Mark node as visited and assign color
       visited.add(currentNode)
       colorAssignment[currentNode] = currentColor
       
       # Check all neighbors
       for neighborNode in adjacencyList[currentNode]:
           if neighborNode not in visited:
               # Try to color neighbor with opposite color
               # abs(currentColor-1) alternates between 0 and 1
               if not dfs(neighborNode, abs(currentColor - 1)):
                   return False
           # If neighbor already colored, check for conflicts
           elif colorAssignment[neighborNode] == currentColor:
               return False
               
       return True
   
   # Build adjacency list from matrix representation
   adjacencyList = defaultdict(set)
   for i in range(len(edges)):
       for j in range(len(edges[0])):
           if edges[i][j] == 1:  # Only add actual edges
               adjacencyList[i].add(j)
               adjacencyList[j].add(i)
   
   # Track visited nodes and their colors
   visited = set()
   colorAssignment = {}
   
   # Check all components of graph
   # Start with color 0 (Team Red) for each component
   for node in range(len(edges)):
       if node not in visited:
           if not dfs(node, 0):
               return False
   
   return True
