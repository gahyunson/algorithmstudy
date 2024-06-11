# --- Directions
# 1) Create a node class.  The constructor
# should accept an argument that gets assigned
# to the data property and initialize an
# empty array for storing children. The node
# class should have methods 'add' and 'remove'.
# 2) Create a tree class. The tree constructor
# should initialize a 'root' property to null.
# 3) Implement 'traverseBF' and 'traverseDF'
# on the tree class.  Each method should accept a
# function that gets called with each element in the tree

class Node:
    def __init__(self, data):
        self.data = data 
        self.children = []
    
    def add(self, data):
        # node = Node(data)
        self.children.append(Node(data))
    
    def remove(self, data):
        self.children = [child for child in self.children if child.data != data]

class Tree:
    def __init__(self) -> None:
        self.root = None 
    
    def traverseBF(self, fn):
        arr = [self.root]
        while len(arr):
            node = arr.pop(0)
            arr.extend(node.children)
            fn(node)
    def traverseDF(self, fn):
        arr = [self.root]
        while arr:
            node = arr.pop(0)
            arr = node.children + arr 
            fn(node)