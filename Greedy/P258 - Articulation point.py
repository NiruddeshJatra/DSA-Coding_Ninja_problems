# Time Complexity:
# - O(V + E) where V is the number of vertices and E is the number of edges
# - DFS visits each vertex once and traverses each edge once
# - Building adjacency list takes O(E)

# Space Complexity:
# - O(V + E) for adjacency list representation of graph
# - O(V) for lowestReachable array and articulationPoints set
# - O(V) for recursion stack in worst case (linear graph)

# INTUITION:
# A vertex is an articulation point if removing it disconnects the graph.
# We can find these using DFS by tracking:
# 1. The earliest visited vertex (by DFS time) reachable from each subtree
# 2. Whether a subtree can reach ancestors above current vertex
#
# Example:
#      1
#    /   \
#   2     3
#   |     |
#   4 --- 5
#
# Here, vertex 1 is an articulation point because removing it separates 2-4 from 3-5.
# When we DFS from 1->2->4, vertex 4 can reach vertex 5 through a back edge.
# However, this path can't reach higher than vertex 1, making 1 an articulation point.

# ALGO:
# 1. Use DFS to traverse graph, tracking for each vertex:
#    - Its discovery time
#    - Lowest discovery time reachable via back edges
# 2. A non-root vertex is articulation point if:
#    - Any of its children in DFS tree can't reach above it using back edges
# 3. Root is articulation point if:
#    - It has more than one child in DFS tree
# 4. Use back edges to update lowest reachable times

from collections import defaultdict
from typing import List, Set

def findArticulationPoints(numNodes: int, connections: List[List[int]]) -> List[int]:
   # Build undirected graph using adjacency list
   graph = defaultdict(list)
   for src, dst in connections:
       graph[src].append(dst)
       graph[dst].append(src)

   # Initialize discovery times array 
   discoveryTime = [numNodes + 1] * (numNodes + 1)  # Use numNodes+1 as unvisited marker
   articulationPoints = set()

   def dfsTraversal(currentNode: int, time: int, parent: int) -> int:
       if discoveryTime[currentNode] == numNodes + 1:  # Node not visited
           discoveryTime[currentNode] = time
           childrenCount = 0

           # Visit all neighbors
           for neighbor in graph[currentNode]:
               if neighbor == parent:  # Skip parent 
                   continue
                   
               if discoveryTime[neighbor] == numNodes + 1:  # Unvisited neighbor
                   childrenCount += 1
                   lowestTime = dfsTraversal(neighbor, time + 1, currentNode)
                   discoveryTime[currentNode] = min(discoveryTime[currentNode], lowestTime)
                   
                   # Non-root articulation point check
                   if parent != -1 and lowestTime >= time:
                       articulationPoints.add(currentNode)
               else:  # Back edge - update with neighbor's discovery time
                   discoveryTime[currentNode] = min(discoveryTime[currentNode], 
                                                  discoveryTime[neighbor])
           
           # Root articulation point check
           if parent == -1 and childrenCount > 1:
               articulationPoints.add(currentNode)
       
       return discoveryTime[currentNode]

   # Handle possibly disconnected components
   for node in range(1, numNodes + 1):
       if discoveryTime[node] == numNodes + 1:
           dfsTraversal(node, 0, -1)
   
   return sorted(list(articulationPoints))

def main():
   testCases = int(input())
   for _ in range(testCases):
       numNodes, numEdges = map(int, input().split())
       edges = []
       for _ in range(numEdges):
           u, v = map(int, input().split())
           edges.append([u, v])
       
       result = findArticulationPoints(numNodes, edges)
       print(*result)

if __name__ == '__main__':
   main()
