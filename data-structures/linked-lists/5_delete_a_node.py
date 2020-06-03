#!/bin/python3
"""
You’re given the pointer to the head node of a linked list and the position of a node to delete.
Delete the node at the given position and return the head node.
A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
The list may become empty after you delete the node.

Input:
You have to complete the deleteNode(SinglyLinkedListNode* llist, int position) method which takes two arguments - the head of the linked list and the position of the node to delete.
You should NOT read any input from stdin/console.
Position will always be at least 0 and less than the number of the elements in the list.
The first line of input contains an integer n, denoting the number of elements in the linked list.
The next n lines contain an integer each in a new line, denoting the elements of the linked list in the order.
The last line contains an integer position denoting the position of the node that has to be deleted form the linked list.
8
20
6
2
19
7
4
15
9
3

Output:
Delete the node at the given position and return the head of the updated linked list.
Do NOT print anything to stdout/console.
The code in the editor will print the updated linked list in a single line separated by spaces.
20 6 2 7 4 15 9
"""

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def deleteNode(head, position):
    if position == 0:
        head = head.next
    else:
        previous = head
        current = head.next
        current_i = 1
        while current_i != position:
            previous = current
            current = current.next
            current_i += 1
        previous.next = current.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
