# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    current_node = head
    i = 0
    while current_node is not None and current_node.data != n:
        current_node = current_node.next
        i += 1
    
    if current_node is None:
        return -1

    return i
    
