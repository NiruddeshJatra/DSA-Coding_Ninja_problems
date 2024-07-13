class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert(pos, val, head):
    current_node = head
    
    # Special case: inserting at the head
    if pos == 0:
        new_node = Node(val)
        new_node.next = current_node
        return new_node
    
    # Traverse the list to find the insertion point
    i = 0
    while current_node is not None and i < pos - 1:
        current_node = current_node.next
        i += 1
    
    # If the position is out of bounds, return the original head
    if current_node is None:
        return head
    
    # Insert the new node
    new_node = Node(val)
    new_node.next = current_node.next
    current_node.next = new_node
    
    return head
