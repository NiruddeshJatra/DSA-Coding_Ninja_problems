# Time Complexity:
# - O(V + E) where V is number of vertices and E is number of edges
# - Each vertex is enqueued/dequeued once in BFS
# - Each edge is examined once when exploring neighbors
# - Path reconstruction takes O(V) in worst case

# Space Complexity:
# - O(V) for queue, visited set, and parent dictionary
# - O(E) for adjacency list representation
# - O(V) for result path in worst case
# - Overall space: O(V + E)

# INTUITION:
# Imagine finding your way through a maze where:
# - Each intersection is a node
# - Each pathway is an edge
# - You want shortest path from start to end
# - You can leave breadcrumbs to trace your path back
#
# BFS is perfect because:
# - Explores like a ripple spreading out from start
# - First time we reach end is guaranteed shortest path
# - By tracking parent nodes, we can reconstruct path
# - Like following breadcrumbs back to start

# ALGORITHM:
# 1. Build undirected graph using adjacency list
# 2. BFS from source node:
#    - Track visited nodes to avoid cycles
#    - Store parent of each node for path reconstruction
#    - Stop when target found (optimization)
# 3. Reconstruct path:
#    - Start from target node
#    - Follow parent pointers back to source
#    - Reverse path to get source-to-target order

def shortestPath(edges, vertices, edgeCount, source, target):
   # Track visited nodes and parent relationships
   visited = set()
   parentNode = {}
   
   # Build undirected graph adjacency list
   adjacencyList = defaultdict(list)
   for startNode, endNode in edges:
       adjacencyList[startNode].append(endNode)
       adjacencyList[endNode].append(startNode)
   
   # Initialize BFS from source
   parentNode[source] = -1  # Source has no parent
   visited.add(source)
   queue = deque([source])
   
   # BFS traversal
   while queue:
       currentNode = queue.popleft()
       
       # Process all unvisited neighbors
       for neighborNode in adjacencyList[currentNode]:
           if neighborNode not in visited:
               visited.add(neighborNode)
               queue.append(neighborNode)
               parentNode[neighborNode] = currentNode
               
           # Early exit if target found
           if neighborNode == target:
               break
   
   # Reconstruct path from target to source
   path = []
   currentNode = target
   path.append(target)
   
   # Follow parent pointers back to source
   while currentNode != source:
       currentNode = parentNode[currentNode]
       path.append(currentNode)
   
   # Return path in correct order (source to target)
   return path[::-1]
