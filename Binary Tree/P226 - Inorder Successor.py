# Time Complexity:
# - O(N) where N is the number of nodes in the binary tree
# - We perform a reverse inorder traversal visiting each node once

# Space Complexity:
# - O(H) where H is the height of the binary tree for recursion stack
# - In worst case (skewed tree), it could be O(N)
# - In balanced tree, it would be O(log N)

# INTUITION:
# Using reverse inorder traversal (right->root->left) helps find successor efficiently.
# When we find target node during traversal, the next node visited in normal inorder traversal 
# would be its successor. By using reverse order and tracking when we find target, we can 
# identify successor in a single pass.

# ALGO:
# 1. Perform reverse inorder traversal (right->root->left)
# 2. Track two states:
#    - successor: store potential successor value
#    - found: indicates if target node is found
# 3. While traversing:
#    - If current node != target and target not found yet:
#      Update successor (as this could be successor of target)
#    - If current node = target:
#      Mark as found and return (successor will have correct value)
# 4. Return successor value

from sys import stdin
import queue

class BinaryTreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def inorderSuccesor(root: BinaryTreeNode, targetKey: int) -> int:
   successor = None
   targetFound = False
   
   def reverseInorderTraversal(currentNode: BinaryTreeNode) -> None:
       nonlocal successor, targetFound
       
       if not currentNode:
           return
           
       # Process right subtree
       reverseInorderTraversal(currentNode.right)
       
       # Process current node
       if targetKey != currentNode.data and not targetFound:
           successor = currentNode.data
       else:
           targetFound = True
           return
           
       # Process left subtree
       reverseInorderTraversal(currentNode.left)
       
   reverseInorderTraversal(root)
   return successor

# Helper function to build tree from input array
def buildTree(arr: List[int]) -> BinaryTreeNode:
   if len(arr) == 0 or arr[0] == -1:
       return None
       
   root = BinaryTreeNode(arr[0])
   nodeQueue = queue.Queue()
   nodeQueue.put(root)
   i = 0
   
   while not nodeQueue.empty():
       currentNode = nodeQueue.get()
       i += 1
       
       # Handle left child
       if arr[i] != -1:
           leftNode = BinaryTreeNode(arr[i])
           currentNode.left = leftNode
           nodeQueue.put(leftNode)
           
       i += 1
       # Handle right child
       if arr[i] != -1:
           rightNode = BinaryTreeNode(arr[i])
           currentNode.right = rightNode
           nodeQueue.put(rightNode)
           
   return root

# Main driver code
testCases = int(input())

for _ in range(testCases):
   inputArray = [int(x) for x in input().strip().split()]
   targetNode = int(input().strip())
   
   root = buildTree(inputArray)
   result = inorderSuccesor(root, targetNode)
   
   print("NULL" if result is None else result)
