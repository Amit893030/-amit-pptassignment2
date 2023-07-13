#Q1.Given a linked list of N nodes such that it may contain a loop.
#A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.
#Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
def remove_loop(head):
    # Step 1: Initialize pointers
    slow = fast = head

    # Step 2: Find the meeting point or detect the absence of a loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        # No loop found, return the linked list as it is
        return head

    # Step 3: Move slow to the head and keep fast at the meeting point
    slow = head

    # Step 4: Move both pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Step 5: Remove the loop by setting the next pointer of the node before the meeting point to null
    fast.next = None

    # Step 6: Return the modified linked list with the loop removed
    return head

#Q2.A number N is represented in Linked List such that
# each digit corresponds to a node in linked list. You need to add 1 to it.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_one(head):
    # Step 1: Reverse the linked list
    head = reverse_linked_list(head)

    # Step 2: Add 1 to the reversed linked list
    current = head
    carry = 1

    while current:
        current.val += carry
        carry = current.val // 10
        current.val %= 10
        prev = current
        current = current.next

    # Step 3: Handle the carry if it exists after the last node
    if carry:
        prev.next = ListNode(carry)

    # Step 4: Reverse the linked list again to restore the original order
    head = reverse_linked_list(head)

    return head


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

#Q3.Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a next pointer to the next node,(ii) a bottom pointer
# to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.Note
# :The flattened list will be printed using the bottom pointer instead of next pointer.
class Node:
    def __init__(self, data=None, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom


def merge_lists(list1, list2):
    # If either list is empty, return the other list
    if not list1:
        return list2
    if not list2:
        return list1

    # Compare the data of the two lists and merge them in sorted order
    if list1.data < list2.data:
        result = list1
        result.bottom = merge_lists(list1.bottom, list2)
    else:
        result = list2
        result.bottom = merge_lists(list1, list2.bottom)

    return result


def flatten_list(head):
    # Base case: if the list is empty or has only one node
    if not head or not head.next:
        return head

    # Recursively flatten the next linked list
    head.next = flatten_list(head.next)

    # Merge the current list with the flattened next list
    head = merge_lists(head, head.next)

    return head

#Q4.You are given a special linked list with N nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**
#Construct a copy of the given list. The copy should consist of exactly N  new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
#For example, if there are two nodes X and Y in the original list, where X.arb-->Y, then for the corresponding two nodes x and y in the copied list,x.arb --> y.**
#Return the head of the copied linked list.

class Node:
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if not head:
        return None

    # Create a hash map to store the mapping between original and copied nodes
    node_map = {}

    # Create a new head node
    new_head = Node(head.val)
    node_map[head] = new_head

    # Initialize pointers for the original and copied lists
    current_orig = head
    current_copy = new_head

    # Traverse the original list and create the copied list
    while current_orig.next:
        # Create a new node for the next original node
        new_node = Node(current_orig.next.val)
        node_map[current_orig.next] = new_node

        # Link the copied nodes
        current_copy.next = new_node

        # Move the pointers forward
        current_orig = current_orig.next
        current_copy = new_node

    # Reset the pointers for the original and copied lists
    current_orig = head
    current_copy = new_head

    # Traverse the original list and link the random pointers in the copied list
    while current_orig:
        if current_orig.random:
            current_copy.random = node_map[current_orig.random]
        current_orig = current_orig.next
        current_copy = current_copy.next

    return new_head

#Q5.Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.
#The **first** node is considered **odd**, and the **second** node is **even**, and so on.
#Note that the relative order inside both the even and odd groups should remain as it was in the input.
#You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    if not head or not head.next:
        return head

    odd_head = odd = head
    even_head = even = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head

    return odd_head

#Q6.Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes,
# where **k** is a given positive integer smaller than or equal to length of the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def left_shift_linked_list(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the kth node from the beginning
    current = head
    for _ in range(k - 1):
        current = current.next

    # Set the new head of the shifted list
    new_head = current.next
    current.next = None

    # Traverse to the end of the original linked list
    current = new_head
    while current.next:
        current = current.next

    # Connect the end of the original linked list with the original head
    current.next = head

    return new_head

#Q7.You are given the `head` of a linked list with `n` nodes.
#For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.
#Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**).
# If the `ith` node does not have a next greater node, set `answer[i] = 0`.
 print("doubt in question 7")


 #Q8.Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.
#After doing so, return the head of the final linked list.  You may return any such answer.
#(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head

    stack = []
    cumulative_sum = 0
    current = dummy

    while current:
        cumulative_sum += current.val

        if cumulative_sum in stack:
            # Remove nodes between the previous occurrence of the cumulative sum
            # and the current node
            prev = stack.pop()
            prev.next = current.next

            # Update the cumulative sum to the value after removing the sequence
            cumulative_sum -= current.val

            # Restart the traversal from the previous occurrence of the cumulative sum
            current = prev
        else:
            stack.append(current)

        current = current.next

    return dummy.next
