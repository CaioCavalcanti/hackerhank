"""
You are given a pointer to the root of a binary search tree and values to be inserted into the tree.
Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree.
You just have to complete the function

Input:
The value to be inserted is 6 on the tree below
        4
       / \
      2   7
     / \
    1   3

Output:
Return the root of the binary search tree after inserting the value into the tree
         4
       /   \
      2     7
     / \   /
    1   3 6
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if current.info > val:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
