class MinHeap:
    def __init__(self):
        self.heap = []

    # Bit manipulation to find parent, left child, and right child
    def parent(self, i):
        return (i - 1) >> 1  # i // 2

    def left_child(self, i):
        return (i << 1) + 1  # 2 * i + 1

    def right_child(self, i):
        return (i << 1) + 2  # 2 * i + 2

    # Insert an element into the heap
    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    # Heapify up for maintaining the min-heap property after insertion
    def _heapify_up(self, index):
        parent_index = self.parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    # Heapify down to maintain the min-heap property after removing the root
    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    # Pop the root node (smallest element)
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    # Build the heap from an arbitrary list of elements
    def build_min_heap(self, elements):
        self.heap = elements[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self._heapify_down(i)

    # Display the heap
    def display(self):
        print(self.heap)


# Example usage of the MinHeap class
if __name__ == "__main__":
    heap = MinHeap()

    # Build the heap from an initial list of elements
    elements = [9, 4, 7, 1, 10, 5]
    print("Building heap from:", elements)
    heap.build_min_heap(elements)
    heap.display()

    # Insert new elements
    print("\nInserting elements 2 and 0:")
    heap.insert(2)
    heap.insert(0)
    heap.display()

    # Pop the root element
    print("\nPopping the minimum element:", heap.pop_min())
    heap.display()

    # Pop the root element again
    print("\nPopping the minimum element again:", heap.pop_min())
    heap.display()
