# Time Complexity:
# - O(H), where H is the height of the BST
# - Best case O(logN) for balanced BST
# - Worst case O(N) for skewed BST where tree is a left chain
# - We only traverse down left edges to find minimum

# Space Complexity:
# - O(1), only using constant extra space
# - We just maintain a single pointer as we traverse left

# INTUITION:
# In a Binary Search Tree:
# 1. Left subtree contains smaller values than current node
# 2. Therefore smallest value must be leftmost node
# 3. Just need to keep going left until we hit null
# 4. No need to look at right subtrees as they have larger values

# ALGORITHM:
# 1. If tree is empty, return -1
# 2. Start at root node
# 3. While left child exists:
#    - Move to left child
# 4. Return data value at leftmost node

def minVal(node):
   if not node:
       return -1
       
   currentNode = node
   while currentNode.left:
       currentNode = currentNode.left
       
   return currentNode.data
