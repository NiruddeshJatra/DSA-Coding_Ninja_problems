# Time Complexity:
# - O(E log E) where E is the number of edges, dominated by the sorting of edges
# - The Union-Find operations take O(E α(n)) where α is the inverse Ackermann function, which is practically constant

# Space Complexity:
# - O(V) for the DisjointSet data structure, where V is the number of vertices

# INTUITION:
# Kruskal's algorithm finds the Minimum Spanning Tree (MST) of a connected, undirected graph by
# greedily selecting edges in order of increasing weight, while avoiding cycles. We use a Disjoint Set
# data structure (Union-Find) to efficiently check if adding an edge creates a cycle.
#
# Example:
# Consider a graph with 4 vertices and edges: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)].
# After sorting: [(2,3,4), (0,3,5), (0,2,6), (0,1,10), (1,3,15)]
# - Add (2,3,4) to MST (weight = 4)
# - Add (0,3,5) to MST (weight = 4+5 = 9)
# - Add (0,2,6): Creates cycle, so skip
# - Add (0,1,10) to MST (weight = 9+10 = 19)
# - Add (1,3,15): Creates cycle, so skip
# Final MST weight = 19

# ALGO:
# 1. Sort all edges in non-decreasing order of their weight.
# 2. Initialize an empty MST and a Disjoint Set data structure.
# 3. For each edge in sorted order:
#    a. If including this edge doesn't create a cycle (using Union-Find), add it to the MST
#    b. Otherwise, discard the edge
# 4. Return the sum of weights of all edges in the MST

from typing import List

class DisjointSet:
   def __init__(self, n):
       self.rank = [0] * (n+1)
       self.size = [1] * (n+1)
       self.parent = list(range(n+1))

   def findParent(self, node):
       if self.parent[node] != node:
           self.parent[node] = self.findParent(self.parent[node])  # Path compression
       return self.parent[node]

   def unionByRank(self, i, j):
       parentOfI = self.findParent(i)
       parentOfJ = self.findParent(j)

       if parentOfI == parentOfJ:
           return

       if self.rank[parentOfI] > self.rank[parentOfJ]:
           self.parent[parentOfJ] = parentOfI

       elif self.rank[parentOfJ] > self.rank[parentOfI]:
           self.parent[parentOfI] = parentOfJ

       else:
           self.parent[parentOfI] = parentOfJ
           self.rank[parentOfJ] += 1
       
   def unionBySize(self, i, j):
       parentOfI = self.findParent(i)
       parentOfJ = self.findParent(j)

       if parentOfI == parentOfJ:
           return

       if self.size[parentOfI] > self.size[parentOfJ]:
           self.parent[parentOfJ] = parentOfI
           self.size[parentOfI] += self.size[parentOfJ]

       else:
           self.parent[parentOfI] = parentOfJ
           self.size[parentOfJ] += self.size[parentOfI]


def kruskalMST(n: int, edges: List[List[int]]) -> int:
   # Sort edges by weight to process them in non-decreasing order
   edges.sort(key=lambda x: x[2])
   
   # Initialize total MST weight
   mstWeight = 0
   
   # Create DisjointSet data structure for cycle detection
   disjointSet = DisjointSet(n)
   
   # Process each edge in sorted order
   for source, destination, weight in edges:
       # If adding this edge doesn't create a cycle
       if disjointSet.findParent(source) != disjointSet.findParent(destination):
           # Add edge weight to MST
           mstWeight += weight
           # Union the sets containing the two vertices
           disjointSet.unionBySize(source, destination)
   
   return mstWeight
