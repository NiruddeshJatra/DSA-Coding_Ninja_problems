# Time Complexity:
# - O(V + E) where V is the number of vertices and E is the number of edges
# - Each vertex is visited once and each edge is traversed once
# - Building adjacency list takes O(E) time

# Space Complexity:
# - O(V + E) for the adjacency list representation
# - O(V) for the visited set and recursion stack
# - O(V) for the result array

# INTUITION:
# DFS works by exploring as far as possible along each branch before backtracking.
# Using recursion and a visited set allows us to:
# - Traverse deep into the graph systematically 
# - Keep track of visited nodes to avoid cycles
# - Handle disconnected components by checking all vertices
# Example: For graph: 0--1--2, 3--4
#          DFS could give [0,1,2,3,4] exploring one component fully before moving to next

# ALGO:
# 1. Create adjacency list representation from edge list
# 2. Initialize visited set and result array
# 3. For each unvisited vertex:
#    - Mark it as visited
#    - Add it to result
#    - Recursively explore all unvisited neighbors
# 4. Return the DFS traversal order

def depthFirstSearch(V: int, E: int, edges: List[List[int]]) -> List[int]:
   def dfsHelper(currentNode: int) -> None:
       """Helper function for DFS traversal"""
       if currentNode in visitedNodes:
           return
           
       # Process current node
       traversalOrder.append(currentNode)
       visitedNodes.add(currentNode)
       
       # Explore neighbors
       for neighborNode in adjacencyList[currentNode]:
           dfsHelper(neighborNode)

   # Build adjacency list
   adjacencyList = defaultdict(list)
   for sourceNode, destinationNode in edges:
       adjacencyList[sourceNode].append(destinationNode)
       adjacencyList[destinationNode].append(sourceNode)

   visitedNodes = set()
   traversalOrder = []

   # Handle disconnected components
   for vertex in range(V):
       if vertex not in visitedNodes:
           dfsHelper(vertex)

   return traversalOrder
