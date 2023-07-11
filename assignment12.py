#Q1.Given a singly linked list, delete **middle** of the linked list. For example, if given linked list is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, then there would be **two middle** nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list is NULL or has 1 node, then it should return NULL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    del slow

    return head
# Create a linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5

head = delete_middle(head)

print("\nModified linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 4 5


#Q2.Given a linked list of N nodes. The task is to check if the linked list has a loop.
# Linked list can contain self loop.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
# Create a linked list with a loop: 1->2->3->4->5->2 (loop)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

has_loop = detect_loop(head)

if has_loop:
    print("The linked list has a loop.")
else:
    print("The linked list does not have a loop.")
# Output: The linked list has a loop.


#Q3.Given a linked list consisting of L nodes and given a number N.
# The task is to find the N the  node from the end of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_nth_from_end(head, n):
    if head is None:
        return None

    main_ptr = head
    ref_ptr = head

    # Move the ref_ptr N nodes ahead
    count = 0
    while count < n:
        if ref_ptr is None:
            return None  # Less than N nodes in the linked list
        ref_ptr = ref_ptr.next
        count += 1

    # Move main_ptr and ref_ptr one node at a time
    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.data
# Create a linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

n = 2
nth_node = find_nth_from_end(head, n)

if nth_node is not None:
    print("The {}th node from the end is: {}".format(n, nth_node))
else:
    print("The linked list has fewer than {} nodes.".format(n))
# Output: The 2nd node from the end is: 4


#Q4.Given a singly linked list of characters,
# write a function that returns true if the given list is a palindrome, else false.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    stack = []
    slow = head
    fast = head

    # Traverse the linked list and push characters onto the stack
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # Handle the case of odd number of elements
    if fast is not None:
        slow = slow.next

    # Compare characters with the stack
    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True
# Create a linked list: r -> a -> d -> a -> r
head = Node('r')
head.next = Node('a')
head.next.next = Node('d')
head.next.next.next = Node('a')
head.next.next.next.next = Node('r')

if is_palindrome(head):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
# Output: The linked list is a palindrome.


#Q5.Given a linked list of N nodes such that it may contain a loop.
#A loop here means that the last node of the link list is connected to the node at position X(1-based index).
# If the link list does not have any loop, X=0.
#Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_and_remove_loop(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    # Detect the loop using Floyd's Cycle Detection algorithm
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If there is no loop, return the linked list as it is
    if slow != fast:
        return

    # Find the node where the loop starts
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop
    fast.next = None

# Create a linked list with a loop: 1->2->3->4->5->2 (loop)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

print("Original linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5 2

detect_and_remove_loop(head)

print("\nModified linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5

#Q6.Given a linked list and two integers M and N. Traverse the linked list such that
# you retain M nodes then delete next N nodes, continue the same till end of the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def retain_and_delete(head, M, N):
    if head is None:
        return None

    current = head

    while current is not None:
        # Retain M nodes
        for _ in range(M - 1):
            if current.next is not None:
                current = current.next
            else:
                return head  # Less than M nodes remaining

        # Delete N nodes
        for _ in range(N):
            if current.next is not None:
                current.next = current.next.next
            else:
                return head  # End of linked list reached

        # Move to the next node
        current = current.next

    return head
# Create a linked list: 1->2->3->4->5->6->7->8->9->10
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)

M = 3
N = 2

print("Original linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5 6 7 8 9 10

head = retain_and_delete(head, M, N)

print("\nModified linked list:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 6 7 8

#Q7.Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_alternate_positions(first, second):
    if first is None:
        return second
    if second is None:
        return first

    current1 = first
    current2 = second

    while current1 is not None and current2 is not None:
        next1 = current1.next
        next2 = current2.next

        current2.next = next1
        current1.next = current2

        current1 = next1
        current2 = next2

    if current2 is not None:
        current1.next = current2

    return first
# Create the first linked list: 1->3->5
first = Node(1)
first.next = Node(3)
first.next.next = Node(5)

# Create the second linked list: 2->4->6->8
second = Node(2)
second.next = Node(4)
second.next.next = Node(6)
second.next.next.next = Node(8)

print("First linked list:")
current = first
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 3 5

print("\nSecond linked list:")
current = second
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 2 4 6 8

first = insert_at_alternate_positions(first, second)

print("\nModified linked list:")
current = first
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5 6 8

#Q8.Given a singly linked list, find if the linked list is circular or not.
