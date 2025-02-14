# Time Complexity:
# - O(V³) where V is number of vertices
# - Three nested loops each iterating through all vertices
# - Much slower than Dijkstra's/Bellman-Ford but finds all-pairs shortest paths

# Space Complexity:
# - O(V²) for the distance matrix storing shortest paths between all pairs
# - Each cell (i,j) stores shortest distance from vertex i to j

# INTUITION:
# Floyd-Warshall finds shortest paths between ALL pairs of vertices.
# Key idea: For vertices i,j, if path through vertex k is shorter than direct path,
# update distance[i][j].
# Example: If direct i->j costs 10, but i->k costs 4 and k->j costs 5,
# we update i->j to cost 9.
# For graph with edges [(1,2,3), (2,3,4), (1,3,8)]:
# When k=2, path 1->2->3 costs 7, shorter than direct path 1->3 costing 8.

# ALGO:
# 1. Initialize distance matrix:
#    - Set diagonal to 0 (distance to self)
#    - Set direct edges to their weights
#    - Set all other cells to infinity
# 2. For each vertex k:
#    - For each pair of vertices (i,j):
#      * If path i->k->j is shorter than current i->j
#      * Update distance[i][j]
# 3. Return specific source->destination distance

from typing import List

def floydWarshall(numVertices: int, numEdges: int, source: int, 
                 destination: int, edges: List[List[int]]) -> int:
   # Initialize distance matrix with infinity
   INF = int(1e9)  # Use large value for infinity
   shortestPaths = [[INF] * (numVertices + 1) for _ in range(numVertices + 1)]
   
   # Set distance to self = 0
   for vertex in range(1, numVertices + 1):
       shortestPaths[vertex][vertex] = 0
   
   # Set initial distances from edges
   for sourceVertex, targetVertex, weight in edges:
       shortestPaths[sourceVertex][targetVertex] = weight
   
   # Process all vertices as intermediate
   for intermediate in range(1, numVertices + 1):
       for start in range(1, numVertices + 1):
           for end in range(1, numVertices + 1):
               # If path through intermediate vertex is shorter
               if (shortestPaths[start][intermediate] != INF and 
                   shortestPaths[intermediate][end] != INF and 
                   shortestPaths[start][end] > 
                   shortestPaths[start][intermediate] + shortestPaths[intermediate][end]):
                   # Update with shorter path
                   shortestPaths[start][end] = (shortestPaths[start][intermediate] + 
                                              shortestPaths[intermediate][end])
   
   # Return shortest path from source to destination
   return shortestPaths[source][destination]
