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
    def __init__(self, size=8, hash_function=None):
        self.size = size
        self.count = 0
        self.table = [None] * size  # C-style array
        self.load_factor = 0.75
        self.shrink_factor = 0.25

        # Allow for a custom hash function, default to multiplication + division method
        if hash_function:
            self.hash_function = hash_function
        else:
            self.hash_function = self.multiplication_division_hash_function

    # Hash function using both multiplication and division method
    def multiplication_division_hash_function(self, key):
        A = (5 ** 0.5 - 1) / 2  # Multiplication constant A
        return int(self.size * ((key * A) % 1))

    # Insert key-value pair
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

    # Search for a value by key
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        node = self.table[index].find(key)
        return node.value if node else None

    # Remove a key-value pair
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
        self.table = [None] * new_size  # Create a new table with the new size
        self.count = 0

        for chain in old_table:
            if chain:
                current = chain.head
                while current:
                    self.insert(current.key, current.value)  # Rehash all elements
                    current = current.next

# Custom hash function example (optional, if you want to use a custom one)
def custom_hash_function(key):
    return key % 10

# Example usage of the hash table
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
print(ht.search(11))
print(ht.search(22))
print(ht.search(33))
print(ht.search(44))
print(ht.search(55))
print(ht.search(66))
print(ht.search(77))


# Remove a key-value pair
ht.remove(33)

# Search again after removal
print("After removing 33")
print(ht.search(11))
print(ht.search(22))
print(ht.search(33))
print(ht.search(44))
print(ht.search(55))
print(ht.search(66))
print(ht.search(77))