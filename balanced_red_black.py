# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class MutableInt:
    def __init__(self, data):
        self.value = data

    def set(self, data):
        self.value = data

    def get(self):
        return self.value


# Recursive function to determine if the given binary tree
# satisfy the height-balanced property of red–black tree or not
def isHeightBalanced(root, rootMax):

    # Base case
    if root is None:
        return True

    # to hold maximum height of left and right subtree
    leftMax = MutableInt(0)
    rightMax = MutableInt(0)

    # proceed only if both left and right subtree are balanced
    if isHeightBalanced(root.left, leftMax) and isHeightBalanced(root.right, rightMax):

        # Calculate the minimum and maximum height of the left and right subtree
        rootMin = min(leftMax.get(), rightMax.get()) + 1
        rootMax.set(max(leftMax.get(), rightMax.get()) + 1)

        # return true if the root node is height balanced
        return rootMax.get() <= 2 * rootMin

    # return false if either left or right subtree is unbalanced
    return False


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left = Node(8)
    root.left.left.left = Node(9)
    root.left.right.left = Node(10)

    rootMax = MutableInt(0)

    if isHeightBalanced(root, rootMax):
        print("Given Binary tree is height-balanced")
    else:
        print("Given Binary tree is not height-balanced")
