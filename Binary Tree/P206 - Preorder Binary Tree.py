# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - Each node is pushed and popped exactly once
#   - Stack operations (push/pop) are O(1)
# Space Complexity:
# - O(H), where H is height of tree
#   - In worst case (skewed tree): H = N
#   - In balanced tree: H = log N
#   - Stack stores at most one path from root to leaf
# INTUITION:
# Iterative preorder using stack is efficient because:
# 1. Stack mimics recursion call stack
# 2. Processing order (Root->Left->Right) can be achieved by:
#    - Push right child first (processed last)
#    - Push left child second (processed second)
#    - Process current node immediately
# 3. Stack naturally handles backtracking
# ALGO:
# 1. Initialize stack with root node
# 2. While stack not empty:
#    - Pop node from stack (process root)
#    - Print node's data
#    - Push right child if exists (will be processed later)
#    - Push left child if exists (will be processed next)
#    - Order of pushing ensures Left before Right
# 3. Continue until all nodes processed
from typing import Optional

class BinaryTreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def preOrder(root: Optional[BinaryTreeNode]) -> None:
   # Handle empty tree
   if not root:
       return
       
   stack = [root]
   
   while stack:
       # Process current node
       currentNode = stack.pop()
       print(currentNode.data, end=" ")
       
       # Push right first (will be processed last)
       if currentNode.right:
           stack.append(currentNode.right)
           
       # Push left second (will be processed next)
       if currentNode.left:
           stack.append(currentNode.left)
