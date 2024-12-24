from typing import List

def pop(heap: List[int]) -> int:
    def heapify_down(index):
        """
        Heapify down to restore the max-heap property.
        """
        largest = index
        left = 2 * index + 1  # Left child
        right = 2 * index + 2  # Right child
        size = len(heap)

        # Compare with left child
        if left < size and heap[left] > heap[largest]:
            largest = left

        # Compare with right child
        if right < size and heap[right] > heap[largest]:
            largest = right

        # If largest is not the current index, swap and recurse
        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            heapify_down(largest)

    if not heap:
        return -1

    max_value = heap[0]  # The root element
    # Replace root with the last element and reduce heap size
    heap[0] = heap[-1]
    heap.pop()  # Remove the last element
    
    # Restore heap property
    heapify_down(0)
    return max_value

'''
    def push(self, x):
        self.heap.app
        end(x)
        pos = len(self.heap) - 1
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[pos] > self.heap[parent]:
                self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
                pos = parent
            else:
                break
'''
