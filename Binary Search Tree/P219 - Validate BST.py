# Time Complexity:
# - O(N), where N is the number of nodes in the tree
# - We need to visit each node exactly once
# - Each node requires constant time comparisons

# Space Complexity:
# - O(H), where H is the height of the tree 
# - Space used by recursion stack
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST

# INTUITION:
# A valid BST must satisfy these conditions at every node:
# 1. All values in left subtree must be less than node's value
# 2. All values in right subtree must be greater than node's value
# 3. Both left and right subtrees must be valid BSTs
# We can check this by passing valid ranges down the tree

# ALGORITHM:
# 1. Use helper function that tracks valid range for each node
# 2. Initially range is (-inf, inf) at root
# 3. For left child:
#    - Upper bound becomes parent's value
#    - Lower bound stays same
# 4. For right child:
#    - Lower bound becomes parent's value
#    - Upper bound stays same
# 5. Return false if any node violates its range


from os import *
from sys import *
from collections import *
from math import *

# Binary Tree node structure
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def validateBST(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.data < high):
            return False
        return helper(node.left, low, node.data) and helper(node.right, node.data, high)

    return helper(root, float('-inf'), float('inf'))
