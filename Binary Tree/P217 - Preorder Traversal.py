# Time Complexity:
# - O(N), where N is the number of nodes in the binary tree
# - Each edge in the tree is traversed at most 2-3 times:
#   1. Finding the predecessor
#   2. Creating the temporary link
#   3. Removing the temporary link

# Space Complexity:
# - O(1), we only use a constant amount of extra space
# - Unlike recursive traversal that uses O(H) stack space
# - Only stores temporary threaded connections using existing right pointers

# INTUITION:
# This is Morris Traversal algorithm for preorder tree traversal without using recursion
# or stack. The key idea is to:
# 1. Create temporary threaded connections from predecessor's right to current node
# 2. These threads help us return to parent after processing left subtree
# 3. By creating/removing these threads, we can traverse without extra space
# 4. For preorder, we process node before going left

# ALGORITHM:
# 1. While current node exists:
#    a. If no left child:
#       - Process current node
#       - Move to right child
#    b. If left child exists:
#       - Find predecessor (rightmost node in left subtree)
#       - If predecessor's right is null:
#          * Process current node
#          * Link predecessor's right to current
#          * Move to left child
#       - If predecessor's right points to current:
#          * Remove the temporary link
#          * Move to right child

class TreeNode:
   def __init__(self, val):
       self.val = val
       self.left = None
       self.right = None

def preorderTraversal(root: TreeNode) -> List[int]:
   result = []
   currentNode = root
   
   while currentNode:
       if not currentNode.left:
           result.append(currentNode.val)
           currentNode = currentNode.right
       else:
           predecessor = currentNode.left
           while predecessor.right and predecessor.right != currentNode:
               predecessor = predecessor.right

           if not predecessor.right:
               result.append(currentNode.val)
               predecessor.right = currentNode
               currentNode = currentNode.left
           else:
               predecessor.right = None
               currentNode = currentNode.right

   return result
