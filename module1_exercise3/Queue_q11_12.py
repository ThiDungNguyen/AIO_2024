class MyQueue:
    def __init__(self, capacity):
        self . __capacity = capacity
        self . __queue = []

    def isEmpty(self):
        return len(self . __queue) == 0

    def is_full(self):
        return len(self . __queue) == self . __capacity

    def enqueue(self, value):
        # Your Code Here
        self.__queue.append(value)
        # End Code Here

    def front(self):
        # Your Code Here
        if not self.isEmpty():
            return self.__queue[0]
        else:
            raise IndexError(
                "Front operation cannot be performed on empty queue.")
        # End Code Here


'''
#q11
queue1 = MyQueue(capacity=5)
queue1 . enqueue(1)
assert queue1 . is_full() == False
queue1 . enqueue(2)
print(queue1 . is_full())
'''

# q12
queue1 = MyQueue(capacity=5)
queue1 . enqueue(1)
assert queue1 . is_full() == False
queue1 . enqueue(2)
print(queue1 . front())
