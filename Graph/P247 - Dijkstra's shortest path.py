# Time Complexity:
# - O((V + E) * log V) where V is vertices and E is edges
# - Each vertex extracted from heap once: O(V * log V)
# - Each edge relaxation requires heap operation: O(E * log V)
# - Overall: O((V + E) * log V)

# Space Complexity:
# - O(V) for distance array and heap
# - O(E) for adjacency list representation
# - Overall space: O(V + E)

# INTUITION:
# Imagine finding fastest route between cities where:
# - Cities are vertices
# - Roads are edges
# - Travel times are weights
#
# Dijkstra works like a smart GPS:
# 1. Always explores most promising (shortest) path first
# 2. Updates routes when faster path found
# 3. Never needs to revisit a city once shortest path found
#
# Like water flowing through pipes:
# - Flows through path of least resistance
# - Reaches closer destinations first
# - Eventually finds shortest path to all points

# ALGORITHM:
# 1. Build weighted adjacency list for undirected graph
# 2. Initialize distances (0 for source, infinity others)
# 3. Use priority queue for efficient path selection:
#    - Pop shortest current path
#    - Try all neighbors of current node
#    - If found shorter path, update and add to queue
# 4. Continue until queue empty (all paths processed)

def dijkstra(edges: List[List[int]], vertices: int, edgeCount: int, source: int) -> List[int]:
   # Build adjacency list for undirected weighted graph
   adjacencyList = defaultdict(list)
   for startNode, endNode, weight in edges:
       adjacencyList[startNode].append((endNode, weight))
       adjacencyList[endNode].append((startNode, weight))
   
   # Initialize distances array
   shortestDistances = [float('inf')] * vertices
   shortestDistances[source] = 0
   
   # Priority queue for efficient path selection
   # Format: (distance, node)
   priorityQueue = [(0, source)]
   
   # Process nodes in order of shortest current distance
   while priorityQueue:
       currentDistance, currentNode = heapq.heappop(priorityQueue)
       
       # Skip if we already found shorter path
       if currentDistance > shortestDistances[currentNode]:
           continue
       
       # Try all neighbors of current node
       for neighborNode, edgeWeight in adjacencyList[currentNode]:
           # Calculate potential new distance
           newDistance = shortestDistances[currentNode] + edgeWeight
           
           # If found shorter path, update and add to queue
           if newDistance < shortestDistances[neighborNode]:
               shortestDistances[neighborNode] = newDistance
               heapq.heappush(priorityQueue, (newDistance, neighborNode))
   
   return shortestDistances
