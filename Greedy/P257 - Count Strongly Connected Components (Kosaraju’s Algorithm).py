# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex and edge is visited once in first DFS
# - Each vertex and edge is visited once in second DFS

# Space Complexity:
# - O(V + E) for graph and reversed graph adjacency lists
# - O(V) for visited sets and stack
# - O(V) for recursion stack in worst case

# INTUITION:
# Kosaraju's Algorithm for finding Strongly Connected Components (SCCs)
# A strongly connected component is a portion of a directed graph where every vertex
# can reach every other vertex.
#
# Example:
# Graph: 0 -> 1 -> 2 -> 3
#        ^         |
#        '---------'
# 
# First DFS gives stack order: [3, 2, 1, 0]
# Second DFS on reversed graph finds SCCs:
# - Start at 3: just {3}
# - Start at 2: {2}
# - Start at 1: {1}
# - Start at 0: {0}
# Result: 4 SCCs

# ALGO:
# 1. First DFS:
#    - Visit all nodes in original graph
#    - Build stack of nodes in order of completion
# 2. Build reversed graph
# 3. Second DFS:
#    - Pop nodes from stack
#    - For each unvisited node, explore its component in reversed graph
#    - Each exploration finds one SCC
# 4. Return count of SCCs

from collections import defaultdict

def stronglyConnectedComponents(v: int, edges: List[List[int]]) -> int:
   # Track visited nodes and finishing order
   visited = set()
   finishingOrder = []
   
   # Build directed graph
   graph = defaultdict(set)
   for source, destination in edges:
       graph[source].add(destination)
   
   def firstDFS(node: int) -> None:
       """First DFS to build stack of nodes in order of completion"""
       visited.add(node)
       for neighbor in graph[node]:
           if neighbor not in visited:
               firstDFS(neighbor)
       finishingOrder.append(node)
   
   # Run first DFS on all unvisited nodes
   for vertex in range(v):
       if vertex not in visited:
           firstDFS(vertex)
   
   # Build reversed graph
   reversedGraph = defaultdict(set)
   for source, destination in edges:
       reversedGraph[destination].add(source)
   
   # Track visited nodes for second DFS
   secondVisited = set()
   
   def secondDFS(node: int) -> None:
       """Second DFS to explore SCCs in reversed graph"""
       secondVisited.add(node)
       for neighbor in reversedGraph[node]:
           if neighbor not in secondVisited:
               secondDFS(neighbor)
   
   # Count SCCs by exploring nodes in reverse finishing order
   sccCount = 0
   while finishingOrder:
       node = finishingOrder.pop()
       if node not in secondVisited:
           secondDFS(node)
           sccCount += 1
   
   return sccCount
