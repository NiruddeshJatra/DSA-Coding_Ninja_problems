# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - Each node is pushed and popped at most twice
#   - Stack operations (push/pop) are O(1)
# Space Complexity:
# - O(H), where H is height of tree
#   - In worst case (skewed tree): H = N
#   - In balanced tree: H = log N
#   - Stack stores nodes along current path
# INTUITION:
# Single stack postorder is tricky because we need to:
# 1. Go left as far as possible first
# 2. Process right subtree before root
# 3. Track when right subtree is complete
# Solution uses stack to track nodes and their right children,
# revisiting nodes when right subtree needs processing
# ALGO:
# 1. While root exists:
#    - Push right child if exists (process later)
#    - Push current node
#    - Move to left child
# 2. Pop node from stack:
#    - If node has right child at top of stack:
#      * Pop right child and push node back
#      * Process right subtree
#    - Else:
#      * Add node's value to result
#      * Mark node as processed
# 3. Continue until stack empty
from typing import List, Optional

class TreeNode:
   def __init__(self, val):
       self.val = val
       self.left = None
       self.right = None

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
   # Handle empty tree
   if not root:
       return []
       
   result = []
   stack = []
   
   while True:
       # Traverse left as far as possible
       while root:
           if root.right:
               stack.append(root.right)  # Save right child
           stack.append(root)            # Save current node
           root = root.left
           
       root = stack.pop()  # Get last node pushed
       
       # Check if we need to process right subtree
       if stack and root.right and root.right == stack[-1]:
           stack.pop()           # Remove right child
           stack.append(root)    # Push root back
           root = root.right    # Process right subtree
       else:
           result.append(root.val)  # Process current node
           root = None              # Mark as processed
           
       if not stack:
           break
           
   return result
