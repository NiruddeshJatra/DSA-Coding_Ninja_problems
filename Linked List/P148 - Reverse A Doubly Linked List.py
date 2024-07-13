'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    prev = None
    cur = head
    while cur:
        front = cur.next
        cur.next = cur.prev
        cur.prev = front
        prev = cur
        cur = front

    return prev
