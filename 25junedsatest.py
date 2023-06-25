#Question.Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())


#Question.Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None  # Return None or raise an exception for empty queue

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.isEmpty())




