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
        if not self.head:
            return None
        self.head = self.head.next 

    def removeLast(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None 
        
        previous = self.head 
        node = self.head.next 
        while node.next:
            previous = node 
            node = node.next 
        previous.next = None 
        return self.head

    def insertLast(self, data):
        last = self.getLast()
        if last:
            last.next = Node(data)
        else:
            self.head = Node(data)

    def getAt(self, integer):
        node = self.head 
        if self.size() < integer:
            return None 
        
        for i in range(integer):
            node = node.next 
        return node 
        # if not self.head:
        #     return 
        
        # counter = 0
        # node = self.head 
        # while node:
        #     if counter == integer:
        #         return node 
        #     counter += 1
        #     node = node.next 
        # return
        
    
    def removeAt(self, idx):
        # doesnt crash on an empty list 
        if not self.head:
            return

        # deletes the first node 
        if idx == 0:
            self.head = self.head.next
            return

        pre = self.getAt(idx - 1)
        # doesnt crash on an index out of bounds
        if not pre.next:
            return
    
        # deletes the node at the given index
        # works on the last node
        pre.next = pre.next.next 

    def insertAt(self, data, integer):
        if not self.head:
            self.head = Node(data)
            return
        if integer == 0:
            self.head = Node(data, self.head)
            return 
        
        if self.getAt(integer-1):
            pre = self.getAt(integer-1)  
        else :
            pre = self.getLast()
        node = Node(data, pre.next)
        pre.next = node  

    def forEach(self, fn):
        node = self.head
        while node:
            fn(node)
            node = node.next 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 