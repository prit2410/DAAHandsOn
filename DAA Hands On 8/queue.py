class Queue:
    def __init__(self, size):
        self.queue = [0] * size  # Fixed-size array for the queue
        self.front = 0
        self.rear = 0
        self.size = size
        self.count = 0  # Keep track of the number of elements

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        dequeued_value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return dequeued_value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            elements = []
            i = self.front
            for _ in range(self.count):
                elements.append(self.queue[i])
                i = (i + 1) % self.size
            print("Queue:", elements)

# Example Usage
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  # Queue Overflow
queue.display()
print("Dequeued:", queue.dequeue())
print("Front element:", queue.peek())
queue.display()
