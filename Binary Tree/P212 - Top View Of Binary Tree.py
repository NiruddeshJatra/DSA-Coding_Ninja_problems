# Time Complexity:
# - O(N log N), where N is the number of nodes in the binary tree
# - BFS traversal takes O(N) time to visit each node once
# - Sorting column keys takes O(W log W) where W is width of tree
# - Overall complexity dominated by sort: O(N log N)

# Space Complexity:
# - O(N) total space used:
#   * O(N) for the columns dictionary
#   * O(W) for the queue where W is max width of tree
#   * O(W) for result array where W is number of columns
# - In worst case (skewed tree), W = N making it O(N)

# INTUITION:
# Top view sees only the first node in each vertical column from root.
# Using BFS with column tracking is ideal because:
# 1. Level order traversal ensures we see top nodes first
# 2. Column distance naturally tracks: left = col-1, right = col+1
# 3. Only need to store first node seen in each column
# 4. BFS guarantees top nodes are processed before lower nodes

# ALGO:
# 1. Handle empty tree case
# 2. Use BFS with queue storing [node, column] pairs
# 3. For each node:
#    - Add value to its column list
#    - Process left child with column-1
#    - Process right child with column+1
# 4. Take first value from each column (sorted by column)
# 5. Return array of top view values

from collections import defaultdict, deque
from typing import List, Optional

def getTopView(root):
   # Handle empty tree
   if not root:
       return []

   result = []
   columnMap = defaultdict(list)
   nodeQueue = deque()
   
   # Start BFS with root at column 0
   nodeQueue.append([root, 0])
   
   # Process nodes level by level
   while nodeQueue:
       levelSize = len(nodeQueue)
       
       for _ in range(levelSize):
           currentNode, column = nodeQueue.popleft()
           
           # Add node value to its column
           columnMap[column].append(currentNode.val)
           
           # Add children to queue with updated columns
           if currentNode.left:
               nodeQueue.append([currentNode.left, column - 1])
           if currentNode.right:
               nodeQueue.append([currentNode.right, column + 1])
   
   # Get first node from each column in sorted order
   for column in sorted(columnMap.keys()):
       result.append(columnMap[column][0])
       
   return result
