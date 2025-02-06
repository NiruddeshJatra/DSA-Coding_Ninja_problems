# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is visited once via queue
# - Each edge is checked at most twice (once from each end)
# - Building adjacency list takes O(E)

# Space Complexity:
# - O(V + E) for adjacency list
# - O(V) for visited set and parent dictionary
# - O(V) for queue in worst case when all nodes are at same level

# INTUITION:
# For undirected graphs, a cycle exists if we find an already visited node
# that's not the parent of current node. Using BFS:
# - Track parent of each node to avoid false cycles
# - If we find visited node that's not parent, we found a back edge (cycle)
# Example: For edges [(1,2), (2,3), (3,1)]:
# When at node 3, we find node 1 is visited but not parent of 3
# So path 1-2-3-1 forms a cycle

# ALGO:
# 1. Build undirected adjacency list from edges
# 2. For each unvisited node:
#    - Do BFS starting from that node
#    - Keep track of parent for each visited node
#    - If we find visited non-parent neighbor, cycle exists
#    - Continue until all components checked
# 3. Return "Yes" if cycle found, "No" otherwise

def cycleDetection(edges: List[List[int]], numVertices: int, numEdges: int) -> str:
   def hasCycle(startNode: int) -> bool:
       """Check if cycle exists in component using BFS"""
       visitedNodes.add(startNode)
       nodeQueue = deque([startNode])
       parentMap = {startNode: -1}
       
       while nodeQueue:
           currentNode = nodeQueue.popleft()
           
           # Check all neighbors
           for neighborNode in adjacencyList[currentNode]:
               if neighborNode not in visitedNodes:
                   nodeQueue.append(neighborNode)
                   visitedNodes.add(neighborNode)
                   parentMap[neighborNode] = currentNode
               # If neighbor visited and not parent, cycle found
               elif parentMap[currentNode] != neighborNode:
                   return True
                   
       return False
   
   # Initialize data structures    
   visitedNodes = set()
   adjacencyList = defaultdict(set)
   
   # Build undirected graph
   for source, destination in edges:
       adjacencyList[source].add(destination)
       adjacencyList[destination].add(source)
   
   # Check each component
   for vertex in range(1, numVertices + 1):
       if vertex not in visitedNodes:
           if hasCycle(vertex):
               return "Yes"
               
   return "No"
