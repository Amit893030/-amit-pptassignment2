#Q1.Given two linked list of the same size, the task is to create a new linked list using those
# linked lists. The condition is that the greater node among both linked list will be added to the new linked list.\

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLinkedLists(head1, head2):
    ptr1 = head1
    ptr2 = head2
    result = None
    tail = None

    while ptr1 and ptr2:
        if ptr1.data >= ptr2.data:
            new_node = Node(ptr1.data)
            ptr1 = ptr1.next
        else:
            new_node = Node(ptr2.data)
            ptr2 = ptr2.next

        if not result:
            result = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    while ptr1:
        new_node = Node(ptr1.data)
        tail.next = new_node
        tail = new_node
        ptr1 = ptr1.next

    while ptr2:
        new_node = Node(ptr2.data)
        tail.next = new_node
        tail = new_node
        ptr2 = ptr2.next

    return result

#Q2.Write a function that takes a list sorted in non-decreasing order and
# deletes any duplicate nodes from the list. The list should only be traversed once.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

#Q3.Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function)
# in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be
# considered as a group and must be reversed

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKNodes(head, k):
    current = head
    prev = None
    next = None
    count = 0

    # Reverse the first k nodes in the group
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # If there are remaining nodes, recursively reverse them
    if next:
        head.next = reverseKNodes(next, k)

    # Return the modified head of the linked list

#Q4.Given a linked list, write a function to reverse every alternate k nodes
# (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseAlternateKNodes(head, k):
    current = head
    prev = None
    next = None
    count = 0

    # Reverse every alternate k nodes
    while current:
        # Reverse k nodes
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # Connect the previous group with the next group
        if count == k:
            if head:
                head.next = prev
            else:
                head = prev

            # Skip k nodes
            while count > 0:
                prev = prev.next
                count -= 1

            # Find the next group
            while prev and prev.next and count < k:
                prev = prev.next
                count += 1

    # Return the modified head of the linked list
    return head

#Q5.Given a linked list and a key to be deleted.
# Delete last occurrence of key from linked. The list may have duplicates.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if head is None:
        return head

    # Find the last occurrence of the key
    prev = None
    toDelete = None
    current = head
    while current:
        if current.data == key:
            toDelete = current
        current = current.next

    # If key is not found, return the original list
    if toDelete is None:
        return head

    # If toDelete is the head node
    if toDelete == head:
        head = head.next
    else:
        prev = head
        while prev.next != toDelete:
            prev = prev.next
        prev.next = toDelete.next

    # Delete the last occurrence of the key
    toDelete = None

    return head

#Q6.Given two sorted linked lists consisting of N and  M  nodes respectively.
# The task is to merge both of the lists (in place) and return the head of the merged list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(head1, head2):
    dummyHead = Node(0)  # Create a dummy node
    current = dummyHead  # Pointer to the dummy node

    # Traverse both lists and compare values
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Append remaining nodes of list 1, if any
    if head1:
        current.next = head1

    # Append remaining nodes of list 2, if any
    if head2:
        current.next = head2

    return dummyHead.next  # Return the head of the merged list

#Q7.Given a Doubly Linked List, the task is to reverse the given Doubly Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDoublyLinkedList(head):
    current = head
    prev = None

    # Traverse the doubly linked list
    while current:
        # Swap prev and next pointers
        next = current.next
        current.next = prev
        current.prev = next

        # Move prev and current pointers
        prev = current
        current = next

    # Update the head of the reversed doubly linked list
    head = prev

    return head

#Q8.Given a doubly linked list and a position.
# The task is to delete a node from given position in a doubly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNodeAtPosition(head, position):
    # Handle deletion of head node
    if position == 1:
        if head is not None:
            head = head.next
            if head:
                head.prev = None
        return head

    current = head
    count = 1

    # Traverse to the desired position
    while current and count < position:
        current = current.next
        count += 1

    # If position is beyond the length of the list, return the original head
    if current is None:
        return head

    # Perform the deletion
    current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev

    return head
