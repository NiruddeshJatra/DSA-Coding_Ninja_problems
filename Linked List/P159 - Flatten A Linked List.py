# Time Complexity: O(N), where N is the total number of nodes across all levels.
# Each node is visited once during the flattening process and merging, leading to a linear time complexity.

# Space Complexity: O(1) if we disregard the recursive stack space, as we are using a constant amount of extra space.
# The recursive stack space can go up to O(N) in the worst case due to recursion depth.

# INTUITION:
# The problem is to flatten a multi-level linked list, where each node can have a 'next' and a 'child' pointer.
# We aim to bring all nodes to a single level, maintaining a sorted order by merging lists level by level.

# ALGO:
# 1. Define a helper function `merge` to combine two sorted lists (using the 'child' pointer as the next pointer in this context).
# 2. In `flattenLinkedList`, recursively flatten the list starting from the 'next' pointer to the end.
# 3. Use the `merge` function to combine the current level with the already flattened 'next' levels.
# 4. Return the final flattened, sorted list starting from the 'head'.

class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.
def merge(a: Node, b: Node) -> Node:
    dummy = Node(0)  # Initialize a dummy node for the merged list
    cur = dummy

    # Merge nodes from lists 'a' and 'b' in sorted order
    while a and b:
        if a.data < b.data:
            cur.child = a
            a = a.child
        else:
            cur.child = b
            b = b.child
        cur.next = None  # Ensure 'next' pointers are not used
        cur = cur.child

    # Attach remaining nodes
    cur.child = a if a else b
    return dummy.child  # Return the merged list starting from the first real node


def flattenLinkedList(head: Node) -> Node:
    if not head or not head.next:  # Base case: single node or end of list
        return head

    # Step 1: Recursively flatten the 'next' levels
    flattenedChild = flattenLinkedList(head.next)

    # Step 2: Merge the current node's list with the flattened 'next' list
    return merge(head, flattenedChild)
