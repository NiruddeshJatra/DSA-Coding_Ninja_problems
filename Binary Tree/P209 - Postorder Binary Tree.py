# Time Complexity:
# - O(N), where N is number of nodes in the tree
#   - Each node is pushed and popped from both stacks once
#   - Stack operations (push/pop) are O(1)
# Space Complexity:
# - O(N), using two stacks
#   - stack1 stores nodes during traversal
#   - stack2 stores nodes in reversed postorder
# INTUITION:
# Using two stacks gives us postorder traversal because:
# 1. First stack helps traverse in Root->Left->Right order
# 2. Second stack reverses this to get Left->Right->Root
# 3. When we pop from stack2, we get postorder traversal
# This avoids complex iterative logic of single stack solution
# ALGO:
# 1. Push root to first stack
# 2. While first stack not empty:
#    - Pop node and push to second stack
#    - Push left child to first stack (if exists)
#    - Push right child to first stack (if exists)
# 3. Pop from second stack and print
#    This gives postorder traversal (Left->Right->Root)
from typing import Optional
from queue import Queue
from sys import stdin, setrecursionlimit

class BinaryTreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def preOrder(root: Optional[BinaryTreeNode]) -> None:
   # Handle empty tree
   if not root:
       return
       
   traversalStack = []  # First stack for traversal
   resultStack = []     # Second stack for reversing order
   
   # Start traversal with root
   traversalStack.append(root)
   
   # Process nodes using first stack
   while traversalStack:
       currentNode = traversalStack.pop()
       resultStack.append(currentNode)
       
       # Push children in order (left first)
       if currentNode.left:
           traversalStack.append(currentNode.left)
       if currentNode.right:
           traversalStack.append(currentNode.right)
   
   # Print nodes in reversed order
   while resultStack:
       node = resultStack.pop()
       print(node.data, end=" ")
