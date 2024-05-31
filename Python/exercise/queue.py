# --- Directions
# Implement a 'peek' method in this Queue class.
# Peek should return the last element (the next
# one to be returned) from the queue *without*
# removing it.

class Queue:
    def __init__(self):
        self.data = []
    
    def add(self, record):
        self.data.insert(0, record)

    def remove(self):
        return self.data.pop() if self.data else None 
    
    def peek(self):
        return self.data[-1] if self.data else None 
    