# Time Complexity:
# - O(H), where H is the height of the BST
# - findMin traverses left path to leftmost node
# - findMax traverses right path to rightmost node
# - Best case O(logN) for balanced tree
# - Worst case O(N) for skewed tree

# Space Complexity:
# - O(1) as we only use constant extra space
# - Only storing two values for min and max
# - Iterative approach avoids recursion stack

# INTUITION:
# In a BST:
# 1. Smallest value is the leftmost node
# 2. Largest value is the rightmost node
# 3. We can find these by following left/right pointers
#    until we hit null
# 4. No need to explore other paths since BST properties
#    guarantee these are min/max

# ALGORITHM:
# 1. findMin helper:
#    - Start from root
#    - Keep going left until null
#    - Return last node's value
# 2. findMax helper:
#    - Start from root
#    - Keep going right until null
#    - Return last node's value
# 3. Return Pair with min and max values

def getMinAndMax(root):
   def findMin(node):
       currentNode = node
       while currentNode.left:
           currentNode = currentNode.left
       return currentNode.data
       
   def findMax(node):  
       currentNode = node
       while currentNode.right:
           currentNode = currentNode.right
       return currentNode.data
       
   return Pair(findMin(root), findMax(root))
