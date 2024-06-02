# --- Directions
# Implement a Queue datastructure using two stacks.
# *Do not* create an array inside of the 'Queue' class.
# Queue should implement the methods 'add', 'remove', and 'peek'.
# For a reminder on what each method does, look back
# at the Queue exercise.
# --- Examples
#     const q = new Queue();
#     q.add(1);
#     q.add(2);
#     q.peek();  // returns 1
#     q.remove(); // returns 1
#     q.remove(); // returns 2

import stack 

class Queue:
    def __init__(self) -> None:
        self.s1 = stack.Stack()
        self.s2 = stack.Stack()
    
    def add(self, record):
        self.s1.push(record)
    
    def remove(self):
        while self.s1.peek():
            self.s2.push(self.s1.pop())
        record = self.s2.pop()
        while self.s2.peek():
            self.s1.push(self.s2.pop())
        return record
    def peek(self):
        while self.s1.peek():
            self.s2.push(self.s1.pop())
        record = self.s2.peek()
        while self.s2.peek():
            self.s1.push(self.s2.pop())
        return record

class Queue1:
    def __init__(self) -> None:
        self.s1 = stack()
        self.s2 = stack()

    def add(self, record):
        self.s1.append(record)
        while self.s1.peek():
            self.s2.append(self.s1.pop())
        

    def peek(self):
        # if not self.s1:
        #     return;
        return self.s1.peek()
    
    def remove(self):
        return self.s1.pop()
    

q = Queue()
print('start',q.s1.data)
q.add(1)
print(q.s1.data)
q.add(2)
print(q.s1.data)
q.peek()
print(q.s1.data)
q.remove()
print(q.s1.data)
q.remove()
print(q.s1.data)
    