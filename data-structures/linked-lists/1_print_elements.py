"""
Given a pointer to the head node of a linked list, print its elements in order, one element per line.
If the head pointer is null (indicating the list is empty), don’t print anything

Input:
The first line of input contains n, the number of elements in the linked list.
The next n lines contain one element each, which are the elements of the linked list.
2
16
13

Output:
Print the integer data for each element of the linked list to stdout/console (e.g.: using printf, cout, etc.).
There should be one element per line.
16
12
"""


#!/bin/python3

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

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def printLinkedList(head):
    print(head.data)
    if head.next is not None:
        printLinkedList(head.next)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
