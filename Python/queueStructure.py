# --- Description
# Create a queue data structure.  The queue
# should be a class with methods 'add' and 'remove'.
# Adding to the queue should store an element until
# it is removed
# --- Examples
#     const q = new Queue();
#     q.add(1);
#     q.remove(); // returns 1;

class Queue:
    def __init__(self) -> None:
        self.queue = []
    def add(self, n):
        self.queue.insert(0, n)
    def remove(self):
        return self.queue.pop()
    
q2 = Queue()
q2.add(1)
q2.add(2)
q2.add(3)
q2.remove()
q2.add(4)
q2.add(5)
print(q2.queue)


class Queue2:
    def __init__(self, queue = []):
        self.queue = []

    def add(self, queue, n):
        queue = self.queue 

        if len(queue)<1:
            return queue.append(n)
            
        queue[1:], queue[0] = queue, n
        return queue 
    
    def remove(self, queue):
        return self.queue.pop()

q = Queue2()
q.add(q, 1)
q.add(q, 2)
q.add(q, 3)
q.remove(q)
q.add(q, 4)
q.add(q, 5)
print(q.queue)