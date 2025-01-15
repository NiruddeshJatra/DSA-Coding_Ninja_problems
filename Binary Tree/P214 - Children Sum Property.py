# Time Complexity:
# - O(N) where N is number of nodes in the tree
# - Each node is visited exactly twice (pre-order and post-order)

# Space Complexity:
# - O(H) where H is height of tree for recursion stack
# - O(log N) for balanced tree
# - O(N) for skewed tree

# INTUITION:
# The problem requires modifying the tree such that:
# 1. Each parent should be >= sum of its children
# 2. After recursive calls, parent becomes sum of modified children
# Using pre-order + post-order traversal is optimal because:
# - Pre-order ensures parent value is adequate before processing children
# - Post-order updates parent to reflect final children values
# This two-pass approach guarantees both conditions are met

# ALGORITHM:
# Pre-order part (top-down):
# 1. Calculate sum of children
# 2. If sum > parent: update parent to sum
# 3. If sum ≤ parent: update children to parent value
# 4. Recurse on left and right subtrees
#
# Post-order part (bottom-up):
# 5. After recursion, recalculate sum of (modified) children
# 6. Set parent value to this sum if node has any children

class BinaryTreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def changeTree(root): 
   if not root:
       return
   
   # Calculate initial sum of children
   childrenSum = 0
   if root.left:
       childrenSum += root.left.data
   if root.right:
       childrenSum += root.right.data
   
   # Pre-order: Handle parent-child relationship
   if childrenSum > root.data:
       # If children sum is greater, increase parent
       root.data = childrenSum
   else:
       # If parent is greater/equal, increase children
       if root.left:
           root.left.data = root.data
       if root.right:
           root.right.data = root.data
   
   # Recurse on children
   changeTree(root.left)
   changeTree(root.right)
   
   # Post-order: Update parent to be sum of modified children
   totalSum = 0
   if root.left:
       totalSum += root.left.data
   if root.right:
       totalSum += root.right.data
   
   # Update parent if it has any children
   if root.left or root.right:
       root.data = totalSum
