class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def remove(self, data):  # self na pewno istnieje
        # Są lepsze sposoby na usuwanie.
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data)
        else:                # self.data == data
            if self.left is None:   # przeskakuje self
                return self.right
            else:     # self.left na pewno niepuste
                # Szukamy największego w lewym poddrzewie.
                node = self.left
                while node.right:   # schodzimy w dół
                    node = node.right
                node.right = self.right   # przyczepiamy
                return self.left
        return self



def bst_min(top): 
    if top.left == None:
        return None
    while (top.left != None):
        top = top.left
    return top.data

def bst_max(top): 
    if top.right == None:
        return None
    while (top.right != None):
        top = top.right
    return top.data

tree = Node(16)
tree.insert(Node(42))
tree.insert(Node(14))
tree.insert(Node(19))
tree.insert(Node(25))
tree.insert(Node(62))
tree.insert(Node(45))
tree.insert(Node(35))
tree.insert(Node(2))
tree.insert(Node(4))
tree.insert(Node(3))
tree.insert(Node(5))
tree.insert(Node(12))

print(bst_min(tree))
print(bst_max(tree))
