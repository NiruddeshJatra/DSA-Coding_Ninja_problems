
class Queue :
    def __init__(self):
        self.queue = []

    '''----------------- Public Functions of Queue -----------------'''
  
    def isEmpty(self) :
        if self.queue:
            return 0
        return 1

    def enqueue(self, data) :
        self.queue.append(data)

    def dequeue(self) :
        if self.queue:
            num = self.queue[0]
            self.queue = self.queue[1:]
            return num
        return -1



    def front(self) :
        if self.queue:
            num = self.queue[0]
            return num
        return -1
