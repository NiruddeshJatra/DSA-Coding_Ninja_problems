# Time Complexity:
# - O(H), where H is the height of the binary search tree
# - In worst case (skewed tree), it could be O(N) where N is number of nodes
# - In balanced BST, it would be O(log N)

# Space Complexity:
# - O(1) as we only use constant extra space
# - No recursion stack space is used as we use iteration

# INTUITION:
# We can leverage the BST property where all nodes in left subtree are smaller and all nodes in right subtree
# are larger than current node. By comparing X with current node's value, we can decide which subtree to traverse
# and keep track of the smallest value greater than or equal to X.

# ALGO:
# 1. Initialize ceil as -1 to handle case when no ceiling exists
# 2. While root is not null:
#    - If current node's value is >= X:
#      - Update ceil to current value as it's a potential candidate
#      - Move to left subtree to find smaller ceiling value
#    - If current node's value < X:
#      - Move to right subtree as ceiling must be larger than current value
# 3. Return ceil value

from os import *
from sys import *
from collections import *
from math import *

class TreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def findCeil(root: TreeNode, targetValue: int) -> int:
   ceilingValue = -1
   
   while root:
       if targetValue <= root.data:
           ceilingValue = root.data
           root = root.left
       else:
           root = root.right
           
   return ceilingValue
