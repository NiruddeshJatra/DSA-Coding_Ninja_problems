# Time Complexity: O(n), where n is the number of nodes in the doubly linked list. 
# We traverse the list once and perform constant-time operations like checking and adding to a hashmap for each node.

# Space Complexity: O(n), as we are using a hashmap to store the nodes' data, and the hashmap can grow up to the size of the list.

# INTUITION:
# The goal is to find all pairs of nodes in a doubly linked list whose sum equals `k`. 
# The naive approach would involve checking each pair of nodes, which takes O(n^2) time. 
# However, by using a hashmap, we can store the values we encounter and check if the complement (k - current node’s value) exists, reducing the time complexity to O(n).

# ALGO:
# 1. Initialize an empty hashmap to store the values of the nodes we encounter.
# 2. Traverse the linked list node by node.
# 3. For each node, check if the value `k - cur.data` exists in the hashmap. 
#    If it does, we found a pair that sums up to `k`.
# 4. Store the pair in the result list and continue traversing.
# 5. After traversing the entire list, return the list of pairs.

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# Don't change the code above.

def findPairs(head: Node, k: int) -> [[int]]:
    hashmap = {}  # Step 1: Initialize a hashmap
    ans = []      # Step 2: Initialize an empty list to store the result
    cur = head    # Step 3: Initialize the current pointer to head
    
    # Step 4: Traverse the linked list
    while cur:
        complement = k - cur.data  # Compute the complement of the current node's value
        # Step 5: If the complement exists in the hashmap, we found a pair
        if complement in hashmap:
            ans.append([complement, cur.data])  # Store the pair in the result list
        # Step 6: Add the current node's value to the hashmap
        hashmap[cur.data] = True
        cur = cur.next  # Move to the next node

    # Step 7: Return the list of pairs
    return ans
