# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST
# - Each iteration moves down one level of the tree

# Space Complexity:
# - O(1), only using constant extra space
# - Iterative approach avoids recursion stack space
# - Only storing current node pointer

# INTUITION:
# Binary Search Tree has the property that for any node:
# 1. Left subtree contains only values less than node
# 2. Right subtree contains only values greater than node
# This allows us to eliminate half the search space each step
# by comparing target value with current node

# ALGORITHM:
# 1. Start from root node
# 2. While current node exists:
#    - If target < current value, go left
#    - If target > current value, go right
#    - If target = current value, return node
# 3. If we exit loop, value not found, return null

'''
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

from typing import List

def searchInBST(root, x):
    while root:
        if x < root.data:
            root = root.left
        elif x > root.data:
            root = root.right
        else:
            return True

    return False
