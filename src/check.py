class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root is not None:
            return self.preorder_search(self.root, find_val)
        return False

    def print_tree(self):
        sm = []
        self.preorder_print(self.root, sm)
        return '-'.join(sm)

    def preorder_search(self, start, find_val):
        if start is not None:
            if start.value == find_val:
                return True
            l = self.preorder_search(start.left, find_val)
            r = self.preorder_search(start.right, find_val)
            return l or r
        return False

    def preorder_print(self, start, vax):
        if start is None:
            return
        vax.append(str(start.value))
        self.preorder_print(start.left, vax)
        self.preorder_print(start.right, vax)

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree())
