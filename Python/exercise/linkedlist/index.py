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
    
    def getFirst(self):
        return self.head 

    def getLast(self):
        if not self.head:
            return None 
        
        node = self.head 
        while node.next:
            node = node.next 
        return node 
    
    def clear(self):
        self.head = None 

    def removeFirst(self):
        self.head = self.head.next 