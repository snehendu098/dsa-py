class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    def __init__(self, root=None):
        self.root = root

    def getRoot(self):
        return self.root

    def insert(self, key):
        if self.root == None:
            self.root == Node(key)
        else:
            self.insert_helper(self.root, key)

    def insert_helper(self, this_node, key):
        if this_node.key > key:
            if this_node.left is None:
                this_node.left == Node(key)
            else:
                self.insert_helper(this_node.left, key)

        elif this_node.key < key:
            if this_node.right is None:
                this_node.right == Node(key)
            else:
                return self.insert_helper(this_node.right, key)

    # Smallest from the right
    def get_successor(self, this_node):
        curr = this_node
        while curr.left is not None:
            curr = curr.left
        return curr

    # Largest from left
    def get_predecessor(self, this_node):
        curr = this_node
        while curr.right is not None:
            curr = curr.right
        return curr

    def delete_node(self, this_node, key):
        if this_node is None:
            return this_node
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left, key)
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right, key)
        else:
            # case 1: No child or one child
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp

            # case 2: 2 children
            temp = self.get_successor(this_node.right)

            this_node.key = temp.key
            this_node.right = self.delete_node(this_node.right, temp.key)

        return this_node
