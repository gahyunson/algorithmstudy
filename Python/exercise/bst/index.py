# --- Directions
# 1) Implement the Node class to create
# a binary search tree.  The constructor
# should initialize values 'data', 'left',
# and 'right'.
# 2) Implement the 'insert' method for the
# Node class.  Insert should accept an argument
# 'data', then create an insert a new node
# at the appropriate location in the tree.
# 3) Implement the 'contains' method for the Node
# class.  Contains should accept a 'data' argument
# and return the Node in the tree with the same value.

# Binary Search Tree 

class Node: 
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data > data and self.left:
            self.left.insert(data)
        elif self.data > data:
            self.left = Node(data)
        elif self.data < data and self.right:
            self.right.insert(data)
        elif self.data < data:
            self.right = Node(data)
    
    def contains(self, data):
        # all the data are unique values
        if self.data == data:
            return self 
        elif self.data > data and self.left :
            return self.left.contains(data)
        elif self.data < data and self.right :
            return self.right.contains(data)
        
        return None 