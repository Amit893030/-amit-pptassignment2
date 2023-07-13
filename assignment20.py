#Q1Given a binary tree, your task is to find subtree with maximum sum in tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSumSubtree(root):
    if root is None:
        return 0

    left_sum = maxSumSubtree(root.left)
    right_sum = maxSumSubtree(root.right)

    current_sum = root.val + left_sum + right_sum

    global maxSum
    maxSum = max(maxSum, current_sum)

    return current_sum

def maxSubtreeSum(root):
    global maxSum
    maxSum = float('-inf')
    maxSumSubtree(root)
    return maxSum

#Q2.Construct the BST (Binary Search Tree) from its given level order traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(level_order):
    if not level_order:
        return None

    queue = []
    root = None

    for val in level_order:
        node = TreeNode(val)

        if root is None:
            root = node
        else:
            curr = root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    return root

#Q3.Given an array of size n. The problem is to
# check whether the given array can represent the level order traversal of a Binary Search Tree or not.
def canRepresentBST(arr):
    n = len(arr)

    lowerBound = []
    upperBound = []

    lowerBound.append(float('-inf'))
    upperBound.append(float('inf'))

    for i in range(n):
        if arr[i] <= lowerBound[-1] or arr[i] >= upperBound[-1]:
            return False

        while lowerBound and arr[i] > lowerBound[-1]:
            lowerBound.pop()

        while upperBound and arr[i] < upperBound[-1]:
            upperBound.pop()

        lowerBound.append(arr[i])
        upperBound.append(arr[i])

    return True
