from typing import List
from collections import defaultdict, deque

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
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
           columnMap[column].append(currentNode.data)
           
           # Add children to queue with updated columns
           if currentNode.left:
               nodeQueue.append([currentNode.left, column - 1])
           if currentNode.right:
               nodeQueue.append([currentNode.right, column + 1])
   
   # Get last node from each column in sorted order
   for column in sorted(columnMap.keys()):
       result.append(columnMap[column][-1])
       
   return result
