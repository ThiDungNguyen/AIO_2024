class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        # Your Code Here
        if not self.is_full():
            self.stack.append(value)
        else:
            raise OverflowError("Stack is full, cannot push new element.")
        # End Code Here

    def top(self):
        # Your Code Here
        return max(self.stack)
        # End Code Here


'''#q9
stack1 = MyStack(capacity=5)
stack1 . push(1)

assert stack1.is_full() == False
stack1 . push(2)
print(stack1.is_full())
'''

# q10
stack1 = MyStack(capacity=5)
stack1 . push(1)
assert stack1 . is_full() == False
stack1 . push(2)
print(stack1 . top())
