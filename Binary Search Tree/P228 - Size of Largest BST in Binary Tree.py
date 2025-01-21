# Time Complexity:
# - O(N) where N is number of nodes in binary tree
# - We visit each node exactly once in postorder traversal

# Space Complexity:
# - O(H) where H is height of tree for recursion stack
# - In balanced tree: O(log N)
# - In skewed tree: O(N) worst case

# INTUITION:
# For each subtree, we need to track 4 things:
# 1. Size of largest BST in subtree
# 2. Min value in subtree (to validate BST property with parent)
# 3. Max value in subtree (to validate BST property with parent) 
# 4. Boolean flag indicating if current subtree is valid BST
# Using postorder traversal (left->right->root), we can build this info bottom-up.

# ALGO:
# 1. Create Node class to store size, min, max values and isValid flag
# 2. For each node in postorder traversal:
#    - Get info from left and right subtrees
#    - If both subtrees are valid BSTs and current node maintains BST property:
#      * size = left.size + right.size + 1
#      * Update min/max considering current node
#      * Mark as valid BST
#    - If BST property violated:
#      * size = max of left/right subtree sizes
#      * Set min/max to infinity
#      * Mark as invalid BST
# 3. Return final size from root

class Node:
   def __init__(self, size: int = 0, minValue: float = float('inf'), 
                maxValue: float = float('-inf'), isValid: bool = True):
       self.size = size
       self.minValue = minValue
       self.maxValue = maxValue
       self.isValid = isValid

def maxSize(root) -> Node:
   # Base case: empty subtree is valid BST
   if not root:
       return Node(0, float('inf'), float('-inf'), True)
   
   # Get information from left and right subtrees
   leftSubtree = maxSize(root.left)
   rightSubtree = maxSize(root.right)
   
   # Check if current subtree forms valid BST
   # Both subtrees must be valid BSTs and current node must maintain BST property
   if (leftSubtree.isValid and rightSubtree.isValid and
       leftSubtree.maxValue < root.data and 
       rightSubtree.minValue > root.data):
       
       # Current subtree is valid BST
       currentSize = leftSubtree.size + rightSubtree.size + 1
       
       # Update min value considering current subtree
       currentMin = root.data if leftSubtree.minValue == float('inf') else leftSubtree.minValue
       
       # Update max value considering current subtree
       currentMax = root.data if rightSubtree.maxValue == float('-inf') else rightSubtree.maxValue
       
       return Node(currentSize, currentMin, currentMax, True)
   else:
       # Current subtree violates BST property
       # Return largest BST found in either subtree
       return Node(
           max(leftSubtree.size, rightSubtree.size),
           float('inf'),
           float('-inf'),
           False
       )

def largestBST(root) -> int:
   return maxSize(root).size
