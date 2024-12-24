class MinHeap:
    def __init__(self, test):
        self.heap = []

    def extractMinElement(self):
        if not self.heap:
            return -1
        # Swap the root (minimum element) with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_element = self.heap.pop()
        # Heapify down to maintain the heap property
        self.heapifyDown(0)
        return min_element

    def deleteElement(self, ind):
        if ind < 0 or ind >= len(self.heap):
            return
        # Swap the element to be deleted with the last element
        self.heap[ind], self.heap[-1] = self.heap[-1], self.heap[ind]
        deleted_element = self.heap.pop()
        # Heapify up and down to maintain the heap property
        self.heapifyUp(ind)
        self.heapifyDown(ind)
        return deleted_element

    def insert(self, val):
        # Add the new element to the end of the heap
        self.heap.append(val)
        # Heapify up to maintain the heap property
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, ind):
        while ind > 0:
            parent_ind = (ind - 1) // 2
            if self.heap[ind] < self.heap[parent_ind]:
                # Swap if the current element is smaller than its parent
                self.heap[ind], self.heap[parent_ind] = self.heap[parent_ind], self.heap[ind]
                ind = parent_ind
            else:
                break

    def heapifyDown(self, ind):
        n = len(self.heap)
        while True:
            left_child_ind = 2 * ind + 1
            right_child_ind = 2 * ind + 2
            smallest = ind
            if left_child_ind < n and self.heap[left_child_ind] < self.heap[smallest]:
                smallest = left_child_ind
            if right_child_ind < n and self.heap[right_child_ind] < self.heap[smallest]:
                smallest = right_child_ind
            if smallest != ind:
                # Swap if the current element is larger than the smallest child
                self.heap[ind], self.heap[smallest] = self.heap[smallest], self.heap[ind]
                ind = smallest
            else:
                break
