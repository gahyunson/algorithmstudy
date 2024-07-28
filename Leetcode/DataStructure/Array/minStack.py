# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

'''
How to approach?

Initialization:
    stack - to store all elements
    min - to store the minimum elements
Push:
    The append method adds to the end of the array.
    Compare the 'val' with the last element of the 'min' list to determine the minimum number.
    I always append it to the min array if the val is equal or less than min's last element.
Pop:
    pop is the method removing at the last element of the array. 
    If the number was in the min array, it have to remove.
    If you don't include equal number when pushing, there was only once the number and it will disappear when you try pop even there was the number twice in stack.
Top:
    index -1 in python means always the last element of the array
GetMin:
    I initialized 'min' array and it sorted descending. I managed the minimum number at Push and Pop method so I don't need to check again.

top의 경우 배열의 가장 마지막 요소를 출력하면 되므로 -1 인덱스를 이용하여 출력하였다.
O(1) 복잡도에서 해결해야하므로, 가장 작은수는 숫자를 추가하거나 삭제할 때 함께 검증하고 추가하거나 삭제하도록 하였다. input할 val가 stack에 들어가 있는 숫자보다 작거나 같은 경우만 작은 숫자들의 배열에 추가하고, 같은 숫자도 추가한 이유는 pop를 할 때 pop 횟수만큼 숫자가 삭제되도록 하였다.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [(2)**31-1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min[-1]:
            self.min.append(val)
            print(self.min)

    def pop(self) -> None:
        rm = self.stack.pop()
        if rm == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()