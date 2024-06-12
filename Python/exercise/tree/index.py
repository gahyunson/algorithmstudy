# --- Directions
# 1) Create a node class.  The constructor
# should accept an argument that gets assigned
# to the data property and initialize an
# empty array for storing children. The node
# class should have methods 'add' and 'remove'.
'''
'data property' , 'empty array for storing children' 
a node carries references to all the child nodes underneath it 

Node
    data = 123,
    children = Node data = 456, 
                    children = None

Add Node(789) then,

Node
    data = 123,
    children = Node data = 456, 
                    children = None,
               Node data = 789, 
                    children = None
'''
# 2) Create a tree class. The tree constructor
# should initialize a 'root' property to null.
# 3) Implement 'traverseBF' and 'traverseDF'
# on the tree class.  Each method should accept a
# function that gets called with each element in the tree

class Node:
    def __init__(self, data): # argument = (data) , accept an argument
        self.data = data  # get assigned
        self.children = []  # initialize an empty array
    
    def add(self, data):
        # node = Node(data) # create new Node
        self.children.append(Node(data)) # add to children 
        # We can find out the child nodes of a given node by looking at the children array
        #   We can tell which nodes are a child of a given node 
        #   by just looking at the children array
    
    def remove(self, data): # given some data -> loot at each child -> if argument data == child of the current node -> remove that!
        # show me the elements excepts 'data'
        self.children = [child for child in self.children if child.data != data]

        # When remove mothod run, it will return true value
        # we want the result was excepted 'data'
        # if don't want to see 'data' element,
        # filtering. 'show me the elements excepts "data"'

        # return True 
        # for every element that is not equal to the data argument!
        

class Tree:
    # assign a root property
    def __init__(self) -> None:
        self.root = None 
    
    '''
    In the case of a Tree,
    whenever we start to want to add or remove elements
    we have to very precisely specify which node we want to adding or removing elements from.

    So, which node are we trying to add new Node to?
    add and remove method with an actual node

    Because, it doesn't quite. It's kind of hard to evision 
    how we might call add or remove on atree
    '''

    '''
    Iterating through a tree == traversal
    How to iterate through a tree
    1. Breadth-First Traversal
    root(top of the tree) -> next level nodes -> next level nodes
    '''
    def traverseBF(self, fn):
        arr = [self.root] 

        # as long as array is a truth value
        while arr:
            # <make a array list to store all tree - sorted in traverseBF>
            # take the first element out of the array
            node = arr.pop(0) # pull out the 1st element
            # take it out so that the array over time will be decreased in size

            '''
            <Take any of its children and stick it in to the end of the array>
            arr.extend(node.children) # node.children is in a array, can't call directly , use for loop.
            for child in node.children:
                arr.extend(child)
            # or
            '''
            
            # if 0 index have children , it can add in front of.
            # take every element out of 'node.children' array,
            # push them one by one into the array.
            arr.extend([child for child in node.children])

            # pass to fn the element
            # gets called with each element in the tree
            fn(node)


    '''
    2. Depth-First Traversal
    root(top of the tree) -> bottom of the tree -> up to level -> bottom of the tree -> ... 

    start off at the very top
    go down the left hand side to the bottom as qickly as possible,
    and then we would loop back up and down, up and down, ... down.
    '''
    def traverseDF(self, fn):
        # Start off by making an array
        arr = [self.root] # taking the root node

        # as long as this array has some element
        while arr:
            # take out the 1st node
            node = arr.pop(0)

            # stick childrens all into the array
            # take an element and add to the start of the array
            # if, don't have children, pass it to the iterator, throw it away
            arr = node.children + arr 

            # we pass it to our iterator function and then throw it away.
            fn(node)