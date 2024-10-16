class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = DoublyLinkedListNode(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False

class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * size
        self.load_factor = 0.75
        self.shrink_factor = 0.25

    # Hash function using multiplication method
    def hash_function(self, key):
        A = (5 ** 0.5 - 1) / 2  # Constant A for multiplication method
        return int(self.size * ((key * A) % 1))

    # Generic function to insert a key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = DoublyLinkedList()

        existing_node = self.table[index].find(key)
        if existing_node:
            existing_node.value = value
        else:
            self.table[index].append(key, value)
            self.count += 1

        if self.count / self.size > self.load_factor:
            self.resize(self.size * 2)

    # Generic function to get a value by key
    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        node = self.table[index].find(key)
        return node.value if node else None

    # Generic function to delete a key
    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return False
        removed = self.table[index].remove(key)
        if removed:
            self.count -= 1
            if self.count / self.size < self.shrink_factor and self.size > 8:
                self.resize(self.size // 2)
        return removed

    # Resize the hash table (double or half the size)
    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0

        for chain in old_table:
            if chain:
                current = chain.head
                while current:
                    self.insert(current.key, current.value)
                    current = current.next

# Test the Hash Table implementation
hash_table = HashTable()

# Insert some key-value pairs
hash_table.insert(10, 100)
hash_table.insert(20, 200)
hash_table.insert(30, 300)

# Retrieve values
print(hash_table.get(10))  # Output: 100
print(hash_table.get(20))  # Output: 200
print(hash_table.get(30))  # Output: 300

# Delete a key
hash_table.delete(20)
print(hash_table.get(20))  # Output: None

# Insert more to trigger resizing
for i in range(40, 100):
    hash_table.insert(i, i * 10)

# Check resizing and retrieval
print(hash_table.get(40))  # Output: 400
