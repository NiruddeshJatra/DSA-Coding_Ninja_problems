'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    current_node = head
    while current_node is not None and current_node.data != k:
        current_node = current_node.next
    
    if current_node is None:
        return 0

    return 1
