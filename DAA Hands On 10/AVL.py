class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at leaf

class AVLTree:
    def __init__(self):
        self.root = None  # Initialize the root node as None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1

        # Return new root
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        # Return new root
        return y

    def _insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # Update height of this ancestor node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Get the balance factor to check whether this node became unbalanced
        balance = self._get_balance(root)

        # If node becomes unbalanced, perform the appropriate rotation

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        # Return the unchanged node pointer
        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)

    def _delete(self, root, key):
        # Perform standard BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self._delete(root.left, key)

        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:
            # Node with one or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self._delete(root.right, temp.key)

        if root is None:
            return root

        # Update height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Get the balance factor
        balance = self._get_balance(root)

        # Balance the node

        # Left Left Case
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)

        # Left Right Case
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Right Case
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)

        # Right Left Case
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        return self._inorder(root, [])

    def _inorder(self, node, res):
        if node is not None:
            self._inorder(node.left, res)
            res.append(node.key)
            self._inorder(node.right, res)
        return res

# Test AVL Tree
avl = AVLTree()

# Insert some nodes
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

# Print inorder traversal of the AVL tree (should be sorted)
print("Inorder traversal:", avl.inorder(avl.root))

# Search for a node
print("Search for 30:", "Found" if avl.search(avl.root, 30) else "Not found")
print("Search for 100:", "Found" if avl.search(avl.root, 100) else "Not found")

# Delete a node
avl.delete(50)
print("Inorder traversal after deleting 50:", avl.inorder(avl.root))

avl.delete(30)
print("Inorder traversal after deleting 30:", avl.inorder(avl.root))

