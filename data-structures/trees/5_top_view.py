"""
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
Top view means when you look the tree from the top the nodes, what you will see will be called the top view of the tree. See the example below.
You only have to complete the function.
For example:
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top view: 1->2->5->6
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    queue = []
    nodes = {0: root.info}
    queue.append([root, 0])

    while queue:
        node, position = queue.pop(0)
        if node.left:
            queue.append([node.left, position - 1])
            if not (position - 1) in nodes:
                nodes[position - 1] = node.left.info

        if node.right:
            queue.append([node.right, position + 1])
            if not (position + 1) in nodes:
                nodes[position + 1] = node.right.info

    keys = sorted(nodes.keys())
    top_view = [nodes[i] for i in keys]
    print(*top_view)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
