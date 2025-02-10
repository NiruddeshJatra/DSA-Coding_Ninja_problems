# Time Complexity:
# - O(V + E) for DAG traversal in best case
# - O(V * E) in worst case with DFS due to potential revisits
# - Should use topological sort + relaxation for optimal O(V + E)
# - Current DFS implementation may exceed time limits

# Space Complexity:
# - O(V) for distance array and recursion stack
# - O(E) for adjacency list storing weighted edges
# - Overall space: O(V + E)

# INTUITION:
# Imagine planning a road trip where:
# - Cities are nodes in a directed graph
# - Roads only go one way (directed edges)
# - Each road has a travel time (edge weight)
# - Want shortest time from start city to all others
#
# Better approach would be:
# 1. Find order to process cities (topological sort)
# 2. Process each city in that order, updating distances
# But current DFS approach:
# - Tries all paths from start city
# - Updates distances when shorter path found
# - Works but not optimal for large graphs

# ALGORITHM:
# 1. Build adjacency list with weights for directed graph
# 2. Initialize distances (0 for start, infinity for others)
# 3. DFS from start node:
#    - For each neighbor, calculate potential new distance
#    - If shorter path found, update distance
#    - Continue DFS from neighbor
# 4. Convert unreachable nodes (inf) to -1
# 5. Return distances array

from collections import defaultdict
from typing import List

def shortestPathInDAG(vertices: int, edgeCount: int, edgeList: List[List[int]]) -> List[int]:
   def dfsExplore(currentNode):
       # Explore all neighbors with their weights
       for neighborNode, edgeWeight in adjacencyList[currentNode]:
           # Calculate potential new distance
           newDistance = distanceFromSource[currentNode] + edgeWeight
           # Update if shorter path found
           if newDistance < distanceFromSource[neighborNode]:
               distanceFromSource[neighborNode] = newDistance
               dfsExplore(neighborNode)
   
   # Initialize distances array
   distanceFromSource = [float('inf')] * vertices
   distanceFromSource[0] = 0  # Distance to source is 0
   
   # Build weighted adjacency list for directed graph
   adjacencyList = defaultdict(set)
   for sourceNode, targetNode, weight in edgeList:
       adjacencyList[sourceNode].add((targetNode, weight))
   
   # Find shortest paths using DFS
   dfsExplore(0)
   
   # Convert unreachable nodes from inf to -1
   for node in range(vertices):
       if distanceFromSource[node] == float('inf'):
           distanceFromSource[node] = -1
           
   return distanceFromSource
