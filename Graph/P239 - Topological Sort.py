# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - We visit each vertex exactly once through DFS
# - For each vertex, we process its adjacency list once
# - Overall, we process each edge exactly once across all DFS calls

# Space Complexity:
# - O(V) for the recursion stack in worst case (for a linear graph)
# - O(V) for visited set and result array
# - O(E) for adjacency list representation
# - Overall space: O(V + E)

# INTUITION:
# Think of planning tasks where certain tasks must be completed before others.
# For example, to graduate college:
# 1. Must take Calculus 1 before Calculus 2
# 2. Must take Physics 1 before Physics 2
# 3. Must take Programming 101 before Data Structures
#
# Topological sort helps us find a valid ordering where all prerequisites
# are completed before dependent tasks. We can visualize it as:
# - Start from any task with no prerequisites
# - Complete it and remove it from consideration
# - Look for new tasks that now have no remaining prerequisites
# - Repeat until all tasks are ordered

# ALGORITHM:
# 1. Build adjacency list representation from edges
# 2. Use DFS to explore graph:
#    - Start from any unvisited node
#    - Recursively visit all unvisited neighbors
#    - After exploring all neighbors, add current node to result
#    - This ensures prerequisites are added after dependents
# 3. Reverse final result to get correct ordering
#    (since we added prerequisites last in DFS)

from collections import defaultdict

def topologicalSort(edges, vertices, edgesCount):
   def dfs(currentNode):
       # Mark current node as visited
       visited.add(currentNode)
       
       # Recursively explore all unvisited neighbors
       for neighborNode in adjacencyList[currentNode]:
           if neighborNode not in visited:
               dfs(neighborNode)
               
       # After exploring all neighbors, add current node
       # This ensures all prerequisites are processed first
       sortedOrder.append(currentNode)
       
   # Create adjacency list representation for efficient neighbor access
   adjacencyList = defaultdict(set)
   for sourceNode, targetNode in edges:
       adjacencyList[sourceNode].add(targetNode)
   
   # Track visited nodes to avoid cycles and reprocessing
   visited = set()
   # Store nodes in topologically sorted order
   sortedOrder = []
   
   # Process all nodes to handle disconnected components
   for node in range(vertices):
       if node not in visited:
           dfs(node)
   
   # Reverse to get correct ordering
   # (DFS adds prerequisites after dependents)
   return sortedOrder[::-1]
