# Time Complexity:
# - O(1) as we only do constant time comparisons

# Space Complexity:
# - O(1) as we use constant extra space

# INTUITION:
# The problem asks if we can uniquely construct a binary tree given two traversal sequences.
# Key insights:
# 1. Inorder (2) traversal is crucial - it tells us which nodes are left/right of each other
# 2. Any combination with Inorder can uniquely determine a binary tree
# 3. Preorder (1) + Postorder (3) cannot uniquely determine a tree
# This is because:
# - Inorder separates left and right subtrees
# - Pre/Post alone don't give enough structural information
# - Need Inorder to know which nodes belong to which subtree

def uniqueBinaryTree(a: int, b: int) -> int:
    """
    Determines if a binary tree can be uniquely constructed from two traversal sequences
    
    Args:
        a: Type of first traversal (1=preorder, 2=inorder, 3=postorder)
        b: Type of second traversal
        
    Returns:
        boolean: True if unique tree possible, False otherwise
    """
    # If either traversal is inorder (2), we can construct unique tree
    if a == 2 or b == 2:
        return True
        
    # If both traversals are same, we can't construct unique tree
    if a == b:
        return False
        
    # If we have pre(1) and post(3), we can't construct unique tree
    return False
