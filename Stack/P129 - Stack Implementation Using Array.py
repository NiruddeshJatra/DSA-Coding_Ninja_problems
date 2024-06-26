
class Stack:
    def __init__(self, n: int):
        self.stack = []
        self.n = n

    def push(self, num: int):
        if len(self.stack) < self.n:
            self.stack.append(num)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
        
    def isEmpty(self) -> int:
        if self.stack:
            return 0
        return 1

    def isFull(self) -> int:
        if len(self.stack) == self.n:
            return 1
        return 0

