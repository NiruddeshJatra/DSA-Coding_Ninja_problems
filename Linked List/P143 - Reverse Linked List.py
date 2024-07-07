"""
### Problem
Given the head of a singly linked list, reverse the list and return its new head.

### Intuition
Reversing a singly linked list involves changing the direction of the pointers so that each node points to its previous node rather than its next node.

### Approach
1. **Initialize Pointers**:
   - Use two pointers, `prev` and `cur`. `prev` will point to the previous node (initially `None`), and `cur` will point to the current node (initially the head of the list).

2. **Iterate Through the List**:
   - Traverse the list using the `cur` pointer.
   - For each node, store the next node in a temporary variable `front`.
   - Reverse the current node's pointer to point to `prev`.
   - Move the `prev` pointer to the current node and the `cur` pointer to the next node (`front`).

3. **Return the New Head**:
   - After the loop, `prev` will point to the new head of the reversed list.

### Time Complexity
O(n), where n is the number of nodes in the linked list. Each node is visited once.

### Space Complexity
O(1), as only a constant amount of space is used for the pointers.

### Code
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    prev = None
    cur = head

    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front

    return prev
