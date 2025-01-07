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
# Iterative inorder using stack is efficient because:
# 1. Stack helps track nodes while traversing left
# 2. When we can't go left, we process current node
# 3. Then we explore right subtree
# This naturally follows Left->Root->Right pattern
# ALGO:
# 1. Initialize empty stack and result array
# 2. Start with root node
# 3. While current node exists or stack not empty:
#    - Go left as far as possible, pushing nodes to stack
#    - Pop node from stack (leftmost unprocessed)
#    - Add node's value to result (process root)
#    - Move to right child
# 4. Return result array
from typing import List, Optional

class TreeNode:
   def __init__(self, data=0, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right

def getInOrderTraversal(root: Optional[TreeNode]) -> List[int]:
   # Handle empty tree
   if not root:
       return []
   
   result = []
   stack = []
   current = root
   
   while current or stack:
       # Traverse to leftmost node
       while current:
           stack.append(current)
           current = current.left
       
       # Process current node
       current = stack.pop()
       result.append(current.data)
       
       # Move to right subtree
       current = current.right
   
   return result
