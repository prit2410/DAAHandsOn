class RBTNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = RBTNode(0)
        self.TNULL.color = 'black'
        self.root = self.TNULL

    # Insert operation
    def insert(self, key):
        node = RBTNode(key)
        node.left = self.TNULL
        node.right = self.TNULL
        current = self.root
        parent = None

        while current != self.TNULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 'red'
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)

        self.root.color = 'black'

    # Left rotation
    def _left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.TNULL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    # Right rotation
    def _right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.TNULL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    # Search operation
    def search(self, key):
        current = self.root
        while current != self.TNULL and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current if current != self.TNULL else None

    # Inorder traversal
    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, res):
        if node != self.TNULL:
            self._inorder(node.left, res)
            res.append((node.key, node.color))
            self._inorder(node.right, res)
        return res

# Test Red-Black Tree

# Create an instance of RedBlackTree
rbt = RedBlackTree()

# Insert elements
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(40)
rbt.insert(50)
rbt.insert(25)

# Inorder traversal (should return sorted keys with their colors)
print("Inorder traversal with colors:", rbt.inorder())

# Search tests
print("Search for 25:", rbt.search(25).key if rbt.search(25) else "Not found")  # Should return 25
print("Search for 100:", "Found" if rbt.search(100) else "Not found")  # Should return Not found
