# Time Complexity: O(n), where n is the number of nodes in the doubly linked list.
# We traverse the list once and perform constant-time operations for each node, 
# so the time complexity is linear.

# Space Complexity: O(1), as we are not using any additional data structures or space 
# apart from a few pointers.

# INTUITION:
# The problem is to delete all occurrences of a given value `k` from a doubly linked list.
# Since we need to traverse the entire list to find all occurrences of `k`, 
# a single pass through the list is sufficient. We update the pointers accordingly 
# to remove the nodes containing `k`.

# ALGO:
# 1. Initialize a pointer `cur` to traverse the list starting from the head.
# 2. If the current node contains the value `k`, update the pointers of the previous and next nodes 
#    to bypass the current node, effectively removing it from the list.
# 3. If the node to be deleted is the head of the list, update the head to point to the next node.
# 4. If the node to be deleted is the last node, set the previous node's `next` pointer to None.
# 5. Continue traversing the list until all occurrences of `k` are removed.
# 6. Return the updated head of the list.

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# Don't change the code above.

def deleteAllOccurrences(head: Node, k: int) -> Node:
    cur = head
    
    # Step 1: Traverse the list
    while cur:
        # Step 2: If current node data is k, delete the node
        if cur.data == k:
            if cur == head:
                # Step 3: If current node is the head, update the head pointer
                if cur.next:
                    head = cur.next
                    head.prev = None
                else:
                    head = None  # If the list becomes empty
            elif not cur.next:
                # Step 4: If current node is the last node, update the previous node's next pointer
                cur.prev.next = None
            else:
                # Step 5: General case, update previous and next pointers to bypass the current node
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
        cur = cur.next  # Move to the next node
    
    # Step 6: Return the modified head of the list
    return head
