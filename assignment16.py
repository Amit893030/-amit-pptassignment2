#Q1.Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than
# that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.
def nearest_greater_frequency(nums):
    frequency = {}
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        frequency[nums[i]] = frequency.get(nums[i], 0) + 1

        while stack and frequency[nums[stack[-1]]] <= frequency[nums[i]]:
            stack.pop()

        if stack:
            result[i] = nums[stack[-1]]

        stack.append(i)

    return result

#Q2.Given a stack of integers, sort it in ascending order using another temporary stack.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def sort_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not temp_stack.is_empty() and temp_stack.top() > temp:
            stack.push(temp_stack.pop())

        temp_stack.push(temp)

    # Transfer elements from temporary stack to the original stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

#Q3.Given a stack with push(),pop(), and empty() operations,
# The task is to delete the middle element of it without using any additional data structure.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def delete_middle(stack):
    if stack.is_empty() or stack.size() == 1:
        return

    mid = stack.size() // 2
    delete_middle_util(stack, mid)


def delete_middle_util(stack, mid, count=0):
    if stack.is_empty() or count == mid:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle_util(stack, mid, count + 1)
    stack.push(temp)

#Q4.Given a Queue consisting of first n natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:
#1. Push and pop elements from the stack
#2. Pop (Or Dequeue) from the given Queue.
#3. Push (Or Enqueue) in the another Queue.

from queue import Queue

def check_queue(arr):
    n = len(arr)
    given_queue = Queue()
    result_queue = Queue()
    stack = []

    for num in arr:
        given_queue.put(num)

    expected = 1

    while not given_queue.empty():
        front = given_queue.queue[0]

        if front == expected:
            result_queue.put(front)
            given_queue.get()
            expected += 1
        else:
            if stack and stack[-1] == expected:
                result_queue.put(stack.pop())
                expected += 1
            else:
                stack.append(given_queue.get())

    while stack:
        if stack.pop() == expected:
            result_queue.put(expected)
            expected += 1
        else:
            return False

    return True


#Q5.Given a number , write a program to reverse this number using stack.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_number(number):
    stack = Stack()
    number_str = str(number)

    for digit in number_str:
        stack.push(digit)

    reversed_str = ""

    while not stack.is_empty():
        reversed_str += stack.pop()

    reversed_number = int(reversed_str)

    return reversed_number

#Q6.Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.
#Only following standard operations are allowed on queue.
#enqueue(x) :** Add an item x to rear of queue
#dequeue() :** Remove an item from front of queue
#size() :** Returns number of elements in queue.
#front() :** Finds front item.

from queue import Queue

def reverse_k_elements(queue, k):
    if k > queue.qsize() or k <= 0:
        return queue

    stack = []
    for _ in range(k):
        stack.append(queue.get())

    reversed_queue = Queue()

    while stack:
        reversed_queue.put(stack.pop())

    while not queue.empty():
        reversed_queue.put(queue.get())

    return reversed_queue

#Q7.Given a sequence of n strings, the task is to check if any two similar words come together and then destroy
# each other then print the number of words left in the sequence after this pairwise destruction.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def count_remaining_words(sequence):
    stack = Stack()

    for word in sequence:
        if stack.is_empty() or word != stack.top():
            stack.push(word)
        else:
            stack.pop()

    return len(stack.items)

#Q8.Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.
#Note:If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is
#considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def max_absolute_difference(arr):
    n = len(arr)
    stack = Stack()
    left_smaller = [0] * n
    right_smaller = [0] * n

    # Find the nearest right smaller element for each element
    for i in range(n):
        while not stack.is_empty() and arr[stack.items[-1]] >= arr[i]:
            index = stack.pop()
            right_smaller[index] = arr[i]
        stack.push(i)

    stack = Stack()

    # Find the nearest left smaller element for each element
    for i in range(n - 1, -1, -1):
        while not stack.is_empty() and arr[stack.items[-1]] >= arr[i]:
            index = stack.pop()
            left_smaller[index] = arr[i]
        stack.push(i)

    max_diff = 0

    # Calculate the maximum absolute difference
    for i in range(n):
        diff = abs(right_smaller[i] - left_smaller[i])
        max_diff = max(max_diff, diff)

    return max_diff
