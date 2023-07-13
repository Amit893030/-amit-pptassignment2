#Q!.Given preorder of a binary tree, calculate its **[depth(or height)](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)** [starting from depth 0]. The preorder is given as a string with two possible characters.
#1. ‘l’ denotes the leaf
#2. ‘n’ denotes internal node
#The given tree can be seen as a full binary tree where every node has 0 or two children.
# The two children of a node can ‘n’ or ‘l’ or mix of both

def calculateDepth(preorder):
    stack = []
    depth = 0

    for char in preorder:
        if char == 'n':
            stack.append(char)
        elif char == 'l':
            while stack and stack[-1] == 'l':
                stack.pop()
            if stack:
                stack.pop()
                stack.append('l')
            else:
                depth += 1

    return depth
# Provide the preorder traversal string
preorder = "nlnll"

# Calculate the depth of the binary tree
depth = calculateDepth(preorder)

# Print the depth of the binary tree
print("Depth of the binary tree:", depth)


#Q2.Given a Binary tree, the task is to print the
# left view of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def leftView(root):
    if root is None:
        return

    # Create a queue for level order traversal
    queue = []

    # Enqueue the root node
    queue.append(root)

    # Iterate until the queue is empty
    while queue:
        # Get the number of nodes in the current level
        level_size = len(queue)

        # Traverse the current level
        for i in range(level_size):
            # Dequeue a node from the front of the queue
            node = queue.pop(0)

            # Print the leftmost node of the current level
            if i == 0:
                print(node.data, end=" ")

            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)

            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Print the left view of the binary tree
print("Left View of Binary Tree:")
leftView(root)
Left View of Binary Tree:
1 2 4

#Q3.Given a Binary Tree, print the Right view of it.
#The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def rightView(root):
    if root is None:
        return

    # Create a queue for level order traversal
    queue = []

    # Enqueue the root node
    queue.append(root)

    # Iterate until the queue is empty
    while queue:
        # Get the number of nodes in the current level
        level_size = len(queue)

        # Traverse the current level
        for i in range(level_size):
            # Dequeue a node from the front of the queue
            node = queue.pop(0)

            # Print the rightmost node of the current level
            if i == level_size - 1:
                print(node.data, end=" ")

            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)

            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Print the right view of the binary tree
print("Right View of Binary Tree:")
rightView(root)
Right View of Binary Tree:
1 3 6


#Q4.Given a Binary Tree, The task is to print the bottom view from left to right. A node x is there in output
# if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal
# to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def bottomView(root):
    if root is None:
        return

    # Initialize a dictionary to store the horizontal distance and node values
    horizontal_distance_map = {}

    # Create a queue for level order traversal
    queue = []

    # Enqueue the root node along with its horizontal distance
    queue.append((root, 0))

    # Perform level order traversal
    while queue:
        # Dequeue a node and its horizontal distance from the front of the queue
        node, horizontal_distance = queue.pop(0)

        # Update the horizontal distance and node value in the dictionary
        horizontal_distance_map[horizontal_distance] = node.data

        # Enqueue the left child with its horizontal distance if it exists
        if node.left:
            queue.append((node.left, horizontal_distance - 1))

        # Enqueue the right child with its horizontal distance if it exists
        if node.right:
            queue.append((node.right, horizontal_distance + 1))

    # Print the bottom view nodes in the sorted order of horizontal distance
    for distance in sorted(horizontal_distance_map):
        print(horizontal_distance_map[distance], end=" ")
# Create a sample binary tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Print the bottom view of the binary tree
print("Bottom View of Binary Tree:")
bottomView(root)
Bottom View of Binary Tree:
5 10 4 14 25
