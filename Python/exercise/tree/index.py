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
        node = Node(data)
        self.children.append(node)
    
    def remove(self):
        self.children.pop()

class Tree:
    pass