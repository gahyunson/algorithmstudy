# --- Directions
# Create a stack data structure.  The stack
# should be a class with methods 'push', 'pop', and
# 'peek'.  Adding an element to the stack should
# store it until it is removed.
# --- Examples
#   const s = new Stack();
#   s.push(1);
#   s.push(2);
#   s.pop(); // returns 2
#   s.pop(); // returns 1

class Stack:
    def __init__(self) -> None:
        self.data = []
    
    def push(self, something):
        self.data.append(something)
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        if not self.data:
            return;
        return self.data[-1]
    
s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.pop())
print(s.data)