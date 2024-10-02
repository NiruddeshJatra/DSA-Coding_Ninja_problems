'''
Following is the structure of the Node class already defined.
'''

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


def sortList(head):
    # Create dummy nodes for 0, 1, and 2 and their heads
    zero, one, two = Node(), Node(), Node()
    
    # Pointers to traverse the lists starting from dummy nodes
    zeroHead = zero
    oneHead = one
    twoHead = two
    
    current = head
    
    # Traverse the original list and link nodes to the appropriate list
    while current:
        if current.data == 0:
            zero.next = current
            zero = zero.next
        elif current.data == 1:
            one.next = current
            one = one.next
        else:  # current.data == 2
            two.next = current
            two = two.next
        
        current = current.next  # Move to the next node
    
    # Connect the three lists: zero -> one -> two
    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    
    # Ensure the last node points to None
    two.next = None
    
    # Return the head of the merged list, which is zeroHead.next
    return zeroHead.next
