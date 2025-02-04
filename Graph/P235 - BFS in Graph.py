# Time Complexity:
# - O(V + E) where V is the number of vertices and E is the number of edges
# - Each vertex is added to queue once and each edge is traversed once
# - Queue operations (append/popleft) take O(1) time

# Space Complexity:
# - O(V) for the queue in worst case when all vertices are at same level
# - O(V) for the visited set to track processed nodes
# - O(V) for the result array storing traversal order

# INTUITION:
# BFS explores the graph level by level using a queue data structure.
# It processes all nodes at the current depth before moving to nodes at the next depth.
# Example: For graph: 0--1--3
#                     |     |
#                     2--4--5
# BFS from node 0 could give [0,1,2,3,4,5] exploring level-wise:
# Level 0: [0]
# Level 1: [1,2]
# Level 2: [3,4]
# Level 3: [5]

# ALGO:
# 1. Initialize queue with starting node 0
# 2. While queue is not empty:
#    - Remove first node from queue
#    - Add it to result array
#    - Add all unvisited neighbors to queue
#    - Mark neighbors as visited
# 3. Return the BFS traversal order

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
   # Initialize data structures
   traversalOrder = []
   visitedNodes = set([0])  # Start from node 0
   nodeQueue = deque([0])
   
   # Process nodes level by level
   while nodeQueue:
       currentNode = nodeQueue.popleft()
       traversalOrder.append(currentNode)
       
       # Process all unvisited neighbors
       for neighborNode in adj[currentNode]:
           if neighborNode not in visitedNodes:
               nodeQueue.append(neighborNode)
               visitedNodes.add(neighborNode)
   
   return traversalOrder
