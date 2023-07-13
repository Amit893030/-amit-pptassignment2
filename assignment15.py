#Q1.Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next
# greater element for current element is -1. For example, next greater of the last element is always -1.
def next_greater_elements(arr):
    n = len(arr)
    answer = [-1] * n  # Initialize the answer array with -1s
    stack = []

    # Step 2: Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Pop indices from the stack while the current element is greater
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()

        if stack:
            # Set the answer for the current index
            answer[i] = arr[stack[-1]]

        # Push the current index onto the stack
        stack.append(i)

    return answer

#Q2.Given an array a of integers of length n, find the nearest smaller number for every element
# such that the smaller element is on left side.If no small element present on the left print -1.
def nearest_smaller_elements(arr):
    n = len(arr)
    answer = [-1] * n  # Initialize the answer array with -1s
    stack = []

    # Step 2: Traverse the array from left to right
    for i in range(n):
        # Pop elements from the stack while the current element is smaller or equal
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            # Set the answer for the current index
            answer[i] = stack[-1]

        # Push the current element onto the stack
        stack.append(arr[i])

    return answer

#Q3.Implement a Stack using two queues q1 and q2.
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        if self.is_empty():
            return None

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        value = self.q1.get()

        self.q1, self.q2 = self.q2, self.q1

        return value

    def top(self):
        if self.is_empty():
            return None

        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        value = self.q1.get()
        self.q2.put(value)

        self.q1, self.q2 = self.q2, self.q1

        return value

    def is_empty(self):
        return self.q1.empty() and self.q2.empty()

#Q4.You are given a stack St. You have to reverse the stack using recursion.

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


def reverse_stack(St):
    if St.is_empty() or St.size() == 1:
        return

    top_element = St.pop()

    reverse_stack(St)

    insert_at_bottom(St, top_element)


def insert_at_bottom(St, item):
    if St.is_empty():
        St.push(item)
        return

    top_element = St.pop()

    insert_at_bottom(St, item)

    St.push(top_element)

#Q5.You are given a string S, the task is to reverse the string using stack.

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


def reverse_string(S):
    stack = Stack()

    # Push each character onto the stack
    for char in S:
        stack.push(char)

    reversed_string = ""

    # Pop characters from the stack and append them to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

#Q6.Given string S representing a postfix expression, the task is to evaluate the expression and find the final
# value. Operators will only include the basic arithmetic operators like *, /, + and -.
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


def evaluate_postfix_expression(S):
    stack = Stack()

    # Iterate through each character of the postfix expression
    for char in S:
        if char.isdigit():
            # If character is an operand, convert it to an integer and push onto stack
            stack.push(int(char))
        else:
            # If character is an operator, perform the corresponding operation
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            # Push the result back onto the stack
            stack.push(result)

    # The final value is the only element remaining in the stack
    return stack.pop()

#Q7.Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the `MinStack` class:
#`MinStack()` initializes the stack object.
#void push(int val)` pushes the element `val` onto the stack.
#void pop()` removes the element on the top of the stack.
#int top()` gets the top element of the stack.
#int getMin()` retrieves the minimum element in the stack.
#You must implement a solution with `O(1)` time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()

            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

#Q8.Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it can trap after raining.
def trap(height):
    if not height:
        return 0

    n = len(height)
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water
