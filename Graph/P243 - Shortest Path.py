# Time Complexity:
# - O(V + E) in best case with BFS
# - O(V * E) in worst case with DFS due to revisiting nodes
# - DFS is not optimal for shortest path - should use BFS
# - Current DFS implementation may exceed time limits on large graphs

# Space Complexity:
# - O(V) for distance array and recursion stack
# - O(E) for adjacency list representation
# - Overall space: O(V + E)

# INTUITION:
# Think of finding shortest route between two cities on a map where:
# - Each city is a node
# - Roads between cities are edges
# - All roads have same length (unweighted)
#
# BFS would be better because:
# - It explores nodes level by level (like ripples in a pond)
# - First time we reach destination is guaranteed shortest path
# - DFS might take longer routes before finding shortest
#
# However, this solution uses DFS with distance updates:
# - Track minimum distance to each node seen so far
# - Only explore path if we found shorter distance
# - Not optimal but will eventually find shortest path

# ALGORITHM:
# 1. Build adjacency list for undirected graph
# 2. Initialize distances array with infinity (except source = 0)
# 3. DFS from source node:
#    - For each neighbor, check if current path is shorter
#    - If shorter, update distance and explore from neighbor
#    - Continue until destination reached or all paths explored
# 4. Return final distance to destination

from collections import defaultdict

def shortestPath(vertices, edges, edgesList, source, destination):
   def dfsExplore(currentNode):
       # Base case: reached destination
       if currentNode == destination:
           return
           
       # Explore all neighbors
       for neighborNode in adjacencyList[currentNode]:
           # Only explore if we found shorter path
           newDistance = distanceFromSource[currentNode] + 1
           if newDistance < distanceFromSource[neighborNode]:
               distanceFromSource[neighborNode] = newDistance
               dfsExplore(neighborNode)
   
   # Initialize distances array
   # Using vertices+1 to handle 1-based indexing if present
   distanceFromSource = [float('inf')] * (vertices + 1)
   distanceFromSource[source] = 0
   
   # Build undirected graph adjacency list
   adjacencyList = defaultdict(set)
   for startNode, endNode in edgesList:
       adjacencyList[startNode].add(endNode)
       adjacencyList[endNode].add(startNode)
   
   # Find shortest path using DFS
   dfsExplore(source)
   
   # Return -1 if destination not reachable
   return distanceFromSource[destination] if distanceFromSource[destination] != float('inf') else -1
