#Q1.Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given
# Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binaryTreeToDLL(root):
    if root is None:
        return None

    # Initialize previous node as None (for the first call)
    global prev
    prev = None

    # Convert the binary tree to DLL
    head = convertToDLL(root)

    # Update the left pointer of the head (leftmost node)
    while head.left:
        head = head.left

    return head


#Q2.A Given a binary tree, the task is to flip the binary tree towards the right direction that is clockwise. See the below examples to see the transformation.
#In the flip operation, the leftmost node becomes the root of the flipped tree and its parent becomes its
# right child and the right sibling becomes its left child and the same should be done for all left most
# nodes recursively.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def flipBinaryTree(root):
    # Base case: If the root is None or a leaf node, return it
    if root is None or (root.left is None and root.right is None):
        return root

    # Recursively flip the left and right subtrees
    flipped_left = flipBinaryTree(root.left)
    flipped_right = flipBinaryTree(root.right)

    # Modify the pointers to flip the tree
    root.left = flipped_right
    root.right = None
    if flipped_left:
        temp = flipped_left
        while temp.right:
            temp = temp.right
        temp.right = flipped_right

    return flipped_left if flipped_left else root
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Flip the binary tree
flipped_root = flipBinaryTree(root)

# Traverse the flipped tree
def traverseFlippedTree(root):
    if root is None:
        return
    print(root.data, end=" ")
    traverseFlippedTree(root.right)
    traverseFlippedTree(root.left)

traverseFlippedTree(flipped_root)


#Q3.Given a binary tree,
# print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printRootToLeafPaths(root):
    if root is None:
        return

    # Create an empty stack and push the root node along with its path
    stack = [(root, str(root.data))]

    # Perform iterative depth-first traversal
    while stack:
        node, path = stack.pop()

        # If the current node is a leaf node, print the path
        if node.left is None and node.right is None:
            print(path)

        # Push the right child along with the updated path to the stack
        if node.right is not None:
            stack.append((node.right, path + "->" + str(node.right.data)))

        # Push the left child along with the updated path to the stack
        if node.left is not None:
            stack.append((node.left, path + "->" + str(node.left.data)))
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print all root-to-leaf paths
printRootToLeafPaths(root)
1->2->4
1->2->5
1->3



#Q4.Given  Preorder,
# Inorder and Postorder traversals of some tree. Write a program to check if they all are of the same tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def constructTree(preorder, inorder):
    if not preorder:
        return None

    # Create the root node using the first element of the preorder traversal
    root = Node(preorder[0])

    # Find the index of the root in the inorder traversal
    root_index = inorder.index(root.data)

    # Split the inorder traversal into left and right subtrees
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    # Split the preorder traversal into left and right subtrees
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    # Recursively construct the left and right subtrees
    root.left = constructTree(left_preorder, left_inorder)
    root.right = constructTree(right_preorder, right_inorder)

    return root
def comparePostorder(root, postorder):
    stack = []
    stack.append(root)
    index = len(postorder) - 1

    while stack:
        curr = stack[-1]
        stack.pop()

        if curr.data != postorder[index]:
            return False

        index -= 1

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return True
# Create the preorder, inorder, and postorder traversals of the tree
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]
postorder = [4, 5, 2, 3, 1]

# Construct the tree using the preorder and inorder traversals
root = constructTree(preorder, inorder)

# Check if the postorder traversal matches the tree's postorder traversal
is_same_tree = comparePostorder(root, postorder)

# Print the result
if is_same_tree:
    print("The traversals represent the same tree.")
else:
    print("The traversals do not represent the same tree.")
