# Time Complexity:
# - O(E * log V) where E is number of edges and V is number of vertices
# - Each edge is processed once, and heap operations take O(log V)
# - Similar to standard Prim's but also tracks parent nodes for MST construction

# Space Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - O(E) for adjacency list
# - O(V) for visited set and heap
# - O(V) for storing MST edges

# INTUITION:
# Like standard Prim's, but we need to track parent nodes to construct actual MST edges.
# We store (weight, vertex, parent) in min heap instead of just (weight, vertex).
# Example: For graph with edges [(1,2,2), (2,3,3), (1,3,4)]:
# - Start at 1, add edges (2,1) and (3,1) to heap
# - Pop (2,2,1), add edge [1,2,2] to MST
# - Pop (3,3,2), add edge [2,3,3] to MST
# Result is list of [parent, child, weight] for each MST edge

# ALGO:
# 1. Build adjacency list for undirected graph
# 2. Initialize min heap with (0, startNode, -1)
# 3. While heap not empty and MST incomplete:
#    - Pop minimum weight edge (weight, node, parent)
#    - If node not visited:
#      * Add to visited set
#      * If parent exists, add [parent, node, weight] to MST
#      * Push edges to unvisited neighbors with current node as parent
# 4. Return list of MST edges

from typing import List
from collections import defaultdict
import heapq

def calculatePrimsMST(numVertices: int, numEdges: int, edges: List[List[int]]) -> List[List[int]]:
   # Build adjacency list (undirected graph)
   adjacencyList = defaultdict(list)
   for startVertex, endVertex, weight in edges:
       adjacencyList[startVertex].append((endVertex, weight))
       adjacencyList[endVertex].append((startVertex, weight))
   
   # Initialize variables for Prim's algorithm
   startNode = 1  # Assuming 1-based indexing
   minHeap = [(0, startNode, -1)]  # (weight, vertex, parent)
   visitedVertices = set()
   mstEdges = []  # Store [parent, child, weight] for each MST edge
   
   # Run Prim's algorithm
   while minHeap and len(visitedVertices) < numVertices:
       currentWeight, currentVertex, parentVertex = heapq.heappop(minHeap)
       
       # Skip if vertex already in MST
       if currentVertex in visitedVertices:
           continue
           
       # Add vertex to MST
       visitedVertices.add(currentVertex)
       
       # Add edge to MST if not the start vertex
       if parentVertex != -1:
           mstEdges.append([parentVertex, currentVertex, currentWeight])
       
       # Add edges to unvisited neighbors
       for neighborVertex, edgeWeight in adjacencyList[currentVertex]:
           if neighborVertex not in visitedVertices:
               heapq.heappush(minHeap, (edgeWeight, neighborVertex, currentVertex))
   
   return mstEdges
