# Time Complexity:
# - O(V * E) where V is number of vertices and E is number of edges
# - Main loop runs V-1 times and processes all E edges in each iteration
# - This is less efficient than Dijkstra's but can handle negative weights

# Space Complexity:
# - O(V) for the distance array storing shortest distances to each vertex
# - O(1) additional space as we only use a few variables

# INTUITION:
# Unlike Dijkstra's which greedily picks minimum distance node, Bellman-Ford relaxes all edges V-1 times.
# Why V-1 iterations? Because shortest path can have at most V-1 edges.
# Each iteration guarantees shortest paths using up to k edges are found.
# Example: For graph with edges [(1,2,-1), (2,3,-2), (1,3,2)]:
# - First iteration finds direct paths from source
# - Second iteration finds better 2-edge paths (like 1->2->3 with cost -3)

# ALGO:
# 1. Initialize distances array with infinity except source = 0
# 2. Repeat V-1 times:
#    - For each edge (u,v,w):
#      * If distance[v] > distance[u] + weight
#      * Update distance[v] to shorter path
# 3. Return final distances array
# Note: To detect negative cycles, run one more iteration. If any distance decreases,
# negative cycle exists.

from typing import List
from collections import defaultdict
from math import inf

def bellmonFord(numVertices: int, numEdges: int, source: int, edges: List[List[int]]) -> List[int]:
   # Initialize distances array with infinity
   shortestDistances = [float('inf')] * (numVertices + 1)
   shortestDistances[source] = 0
   
   # Relax all edges V-1 times
   for iteration in range(numVertices - 1):
       # Process all edges
       for sourceVertex, targetVertex, weight in edges:
           # If we can find a shorter path, update distance
           if shortestDistances[sourceVertex] != float('inf') and \
              shortestDistances[targetVertex] > shortestDistances[sourceVertex] + weight:
               shortestDistances[targetVertex] = shortestDistances[sourceVertex] + weight
   
   # Optional: Detect negative cycles
   # for sourceVertex, targetVertex, weight in edges:
   #     if shortestDistances[sourceVertex] != float('inf') and \
   #        shortestDistances[targetVertex] > shortestDistances[sourceVertex] + weight:
   #         return None  # Negative cycle exists
   
   return shortestDistances
