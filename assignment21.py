#Q1You are given a binary tree. The binary tree is represented using the TreeNode class. Each TreeNode has an integer value and left and right
# children, represented using the TreeNode class itself. Convert this binary tree into a binary search tree.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convertToBST(root):
    # Step 1: Perform in-order traversal to extract values
    def inOrderTraversal(node):
        if node is None:
            return []

        return inOrderTraversal(node.left) + [node.value] + inOrderTraversal(node.right)

    values = inOrderTraversal(root)

    # Step 2: Sort the extracted values
    values.sort()

    # Step 3: Replace the values in the tree with the sorted values
    def inOrderReplacement(node):
        nonlocal values

        if node is None:
            return None

        node.left = inOrderReplacement(node.left)
        node.value = values.pop(0)
        node.right = inOrderReplacement(node.right)

        return node

    return inOrderReplacement(root)


#Q2.Given a Binary Search Tree with all
# unique values and two keys. Find the distance between two nodes in BST. The given keys always exist in BST.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findDistance(root, key1, key2):
    # Helper function to find the distance between a node and a key
    def findNodeDistance(node, key, distance):
        if node is None:
            return 0

        if node.value == key:
            return distance

        if key < node.value:
            return findNodeDistance(node.left, key, distance + 1)
        else:
            return findNodeDistance(node.right, key, distance + 1)

    # Helper function to find the lowest common ancestor (LCA)
    def findLCA(node, key1, key2):
        if node is None:
            return None

        if key1 < node.value and key2 < node.value:
            return findLCA(node.left, key1, key2)
        elif key1 > node.value and key2 > node.value:
            return findLCA(node.right, key1, key2)
        else:
            return node

    # Find the LCA of the two keys
    lca = findLCA(root, key1, key2)

    # Find the distances from the LCA to each key
    distance1 = findNodeDistance(lca, key1, 0)
    distance2 = findNodeDistance(lca, key2, 0)

    # Return the sum of the distances
    return distance1 + distance2

#Q3.Write a program to convert a binary tree to a doubly linked list.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convertToDoublyLinkedList(root):
    global prev
    prev = None

    def inorderTraversal(node):
        nonlocal prev

        if node is None:
            return None

        # Convert left subtree
        inorderTraversal(node.left)

        # Update pointers
        if prev:
            prev.right = node
            node.left = prev
        prev = node

        # Convert right subtree
        inorderTraversal(node.right)

    # Perform in-order traversal to convert the tree
    inorderTraversal(root)

    # Update the right pointer of the last node
    while prev and prev.right:
        prev = prev.right
    if prev:
        prev.right = None

    # Return the head of the doubly linked list
    return root


#Q4.Write a program to connect nodes at the same level.
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def connectNodes(root):
    if root is None:
        return root

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i < level_size - 1:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root
