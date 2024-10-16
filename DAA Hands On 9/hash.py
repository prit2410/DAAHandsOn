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

    # Generic function to search for a value by key
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        node = self.table[index].find(key)
        return node.value if node else None

    # Generic function to delete a key
    def remove(self, key):
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

# Test the Hash Table implementation with provided example
ht = HashTable()

# Insert key-value pairs
ht.insert(11, 110)
ht.insert(22, 220)
ht.insert(33, 330)
ht.insert(44, 440)
ht.insert(55, 550)
ht.insert(66, 660)
ht.insert(77, 770)

# Search for a value by key
print("Value for key 33:", ht.search(33))  # Output: 330

# Remove a key-value pair
ht.remove(33)

# Search again after removal
print("Value for key 33 after removal:", ht.search(33))  # Output: None
