from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    def inOrder(root, arr):
        if not root:
            return
        inOrder(root.left, arr)
        arr.append(root.data)
        inOrder(root.right, arr)

    def preOrder(root, arr):
        if not root:
            return
        arr.append(root.data)
        preOrder(root.left, arr)
        preOrder(root.right, arr)

    def postOrder(root, arr):
        if not root:
            return
        postOrder(root.left, arr)
        postOrder(root.right, arr)
        arr.append(root.data)


    inOrderedArr = []
    inOrder(root, inOrderedArr)
    preOrderedArr = []
    preOrder(root, preOrderedArr)
    postoderedArr = []
    postOrder(root, postoderedArr)

    return [inOrderedArr, preOrderedArr, postoderedArr]






