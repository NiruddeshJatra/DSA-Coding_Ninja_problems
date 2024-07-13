class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    previous_node = head
    current_node = previous_node.next
    while current_node:
        if previous_node.data == current_node.data:
            previous_node.next = current_node.next
        else:
            previous_node = current_node
        current_node = previous_node.next

    return head
