class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, data=None):
        self.head = Node()
        self.count = 0

    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
        self.count += 1

    def append(self, data):
        node = Node(data)
        if self.head.next == None:
            self.count += 1
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self.count += 1

    def search(self, data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def insert(self, data, new_data):
        current_node = self.search(data)
        if current_node:
            node = Node(new_data,current_node.next)
            self.current_node.next = node
        self.count += 1

    def remove(self, data=None):
        previous_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                break
            previous_node = current_node
            current_node = current_node.next
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next
        self.count -= 1

class Stack:
    def __init__(self):
        self.stack = LinkedList()
        
    def getSize(self):
        return self.stack.count

    def isEmpty(self):
        if self.stack.count:
            return False
        return True

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.remove()

    def getTop(self):
        if self.stack.head.next == None:
            return self.stack.head
        current_node = self.stack.head.next
        while current_node.next:
            current_node = current_node.next
        return current_node
