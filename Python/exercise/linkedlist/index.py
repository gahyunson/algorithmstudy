class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        cnt = 0
        node = self.head 
        while node:
            cnt+=1
            node = node.next 
        return cnt 