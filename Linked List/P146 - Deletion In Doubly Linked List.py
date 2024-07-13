def deleteNode(head, pos):
    current_node = head
    i = 0
    while current_node.next and i != pos:
        current_node = current_node.next
        i += 1
    if current_node.next == None:
        current_node.prev.next = None
    else:
        current_node.data = current_node.next.data
        current_node.next = current_node.next.next
        current_node.next.prev = current_node

    return head
