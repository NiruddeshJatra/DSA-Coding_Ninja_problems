# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is visited once
# - Each edge is traversed at most once
# - Building adjacency list takes O(E)

# Space Complexity:
# - O(V + E) for adjacency list
# - O(V) for visited and path sets
# - O(V) for recursion stack in worst case

# INTUITION:
# To detect a cycle in directed graph, we need to find if we can get back to a node
# while exploring its descendants. We use two sets:
# - visited: tracks all nodes we've seen 
# - path: tracks nodes in current DFS path
# Example: For edges [(0,1), (1,2), (2,1)]:
# 0 -> 1 -> 2 -> 1 (cycle detected!)
#      ^---------'

# ALGO:
# 1. Build adjacency list from edges
# 2. For each unvisited node:
#    - Add to visited and current path
#    - DFS through neighbors
#    - If neighbor in current path: cycle found
#    - Remove node from path when done exploring
# 3. Return true if cycle found, false otherwise

def isCyclic(edges: List[List[int]], numVertices: int, numEdges: int) -> bool:
   def hasCycle(currentNode: int) -> bool:
       """Check if cycle exists starting from current node"""
       visitedNodes.add(currentNode)
       currentPath.add(currentNode)
       
       # Check all neighbors
       for neighborNode in adjacencyList[currentNode]:
           if neighborNode not in visitedNodes:
               if hasCycle(neighborNode):
                   return True
           # If neighbor in current path, cycle exists
           elif neighborNode in currentPath:
               return True
       
       # Remove from path when done exploring
       currentPath.remove(currentNode)
       return False
   
   # Initialize data structures    
   visitedNodes = set()
   currentPath = set()
   adjacencyList = defaultdict(set)
   
   # Build adjacency list
   for source, destination in edges:
       adjacencyList[source].add(destination)
   
   # Check each vertex
   for vertex in range(numVertices):
       if vertex not in visitedNodes:
           if hasCycle(vertex):
               return True
               
   return False
