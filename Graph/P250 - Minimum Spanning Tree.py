# Time Complexity:
# - O(E * log V) where E is number of edges and V is number of vertices
# - Each edge is processed once and heap operations take O(log V)
# - Similar to Dijkstra's but tracks MST instead of shortest paths

# Space Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - O(E) for adjacency list storing all edges
# - O(V) for visited set and heap storing vertices

# INTUITION:
# Prim's algorithm grows MST one vertex at a time, always adding minimum weight edge
# that connects MST to a new vertex.
# Key idea: Keep track of edges connecting MST vertices to non-MST vertices in min heap.
# Example: For graph with edges [(0,1,2), (1,2,3), (0,2,4)]:
# - Start at 0, add edges (0,1,2) and (0,2,4) to heap
# - Pop (0,1,2), add 1 to MST, add edge (1,2,3) to heap
# - Pop (1,2,3), add 2 to MST
# Final MST has weight 5 using edges (0,1) and (1,2)

# ALGO:
# 1. Build adjacency list with undirected edges
# 2. Initialize min heap with (0, startNode)
# 3. While heap not empty and MST incomplete:
#    - Pop minimum weight edge
#    - If end vertex not in MST:
#      * Add to MST
#      * Add weight to total
#      * Push all edges to non-MST vertices
# 4. Return total MST weight

from collections import defaultdict
import heapq
from typing import List

class Edge:
   def __init__(self, start: int, end: int, weight: int):
       self.start = start
       self.end = end
       self.weight = weight

def minimumSpanningTree(edges: List[Edge], numVertices: int, numEdges: int) -> int:
   # Build adjacency list (undirected graph)
   adjacencyList = defaultdict(list)
   for edge in edges:
       startVertex = edge.start
       endVertex = edge.end
       weight = edge.weight
       # Add edges in both directions
       adjacencyList[startVertex].append((endVertex, weight))
       adjacencyList[endVertex].append((startVertex, weight))
   
   # Initialize variables for Prim's algorithm
   minHeap = [(0, 0)]  # (weight, vertex)
   visitedVertices = set()
   totalWeight = 0
   
   # Run Prim's algorithm
   while minHeap and len(visitedVertices) < numVertices:
       currentWeight, currentVertex = heapq.heappop(minHeap)
       
       # Skip if vertex already in MST
       if currentVertex in visitedVertices:
           continue
           
       # Add vertex to MST
       visitedVertices.add(currentVertex)
       totalWeight += currentWeight
       
       # Add edges to unvisited neighbors
       for neighborVertex, edgeWeight in adjacencyList[currentVertex]:
           if neighborVertex not in visitedVertices:
               heapq.heappush(minHeap, (edgeWeight, neighborVertex))
   
   return totalWeight
