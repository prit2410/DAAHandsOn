class Node:
    def __init__(self, value, next_index=-1):
        self.value = value
        self.next = next_index  # Simulating pointer to the next node

class SinglyLinkedList:
    def __init__(self, size):
        self.list = [None] * size  # Fixed-size array for the nodes
        self.head = -1  # Head of the list (initially -1, indicating empty)
        self.size = size
        self.next_free = 0  # Points to the next free index in the array

    def insert_at_end(self, value):
        if self.next_free == self.size:
            raise Exception("List Overflow")
        new_node = Node(value, -1)
        if self.head == -1:
            self.head = self.next_free
        else:
            index = self.head
            while self.list[index].next != -1:
                index = self.list[index].next
            self.list[index].next = self.next_free
        self.list[self.next_free] = new_node
        self.next_free += 1

    def delete_at_beginning(self):
        if self.head == -1:
            raise Exception("List Underflow")
        value = self.list[self.head].value
        self.head = self.list[self.head].next
        return value

    def delete_at_end(self):
        if self.head == -1:
            raise Exception("List Underflow")
        if self.list[self.head].next == -1:
            value = self.list[self.head].value
            self.head = -1
            return value
        index = self.head
        while self.list[self.list[index].next].next != -1:
            index = self.list[index].next
        value = self.list[self.list[index].next].value
        self.list[index].next = -1
        return value

    def display(self):
        if self.head == -1:
            print("List is empty")
        else:
            index = self.head
            elements = []
            while index != -1:
                elements.append(self.list[index].value)
                index = self.list[index].next
            print("Linked List:", elements)

# Example Usage
linked_list = SinglyLinkedList(5)
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
linked_list.display()
print("Deleted from beginning:", linked_list.delete_at_beginning())
print("Deleted from end:", linked_list.delete_at_end())
linked_list.display()
