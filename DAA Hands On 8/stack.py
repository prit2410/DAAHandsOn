class Stack:
    def __init__(self, size):
        self.stack = [0] * size  # Fixed-size array for the stack
        self.top = -1  # Initial position of the top
        self.size = size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        popped_value = self.stack[self.top]
        self.top -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack[:self.top + 1])

# Example Usage
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # Stack Overflow
stack.display()
print("Popped:", stack.pop())
print("Top element:", stack.peek())
stack.display()
