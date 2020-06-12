#!/bin/python3
"""
Given a reference to the head of a doubly-linked list and an integer, data, create
a new DoublyLinkedListNode object having data value data and insert it into a sorted
linked list while maintaining the sort.
Complete the sortedInsert function in the editor below.
It must return a reference to the head of your modified DoublyLinkedList.
sortedInsert has two parameters:
    - head: A reference to the head of a doubly-linked list of DoublyLinkedListNode objects.
    - data: An integer denoting the value of the data field for the DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where head == null) and a list with one element are sorted lists.

Input:
The first line contains an integer t, the number of test cases.
Each of the test case is in the following format:
The first line contains an integer n, the number of elements in the linked list.
Each of the next n lines contains an integer, the data for each node of the linked list.
The last line contains an integer data which needs to be inserted into the sorted doubly-linked list.
1
4
1
3
4
10
5

Output:
Do not print anything to stdout. Your method must return a reference to the head of the same list that was passed to it as a parameter.
The ouput is handled by the code in the editor and is as follows:
For each test case, print the elements of the sorted doubly-linked list separated by spaces on a new line.
1 3 4 5 10
"""

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)

    if head is None:
        return node
    elif data <= head.data:
        node.next = head
        head.prev = node
        return node
    else:
        rest = sortedInsert(head.next, data)
        head.next = rest
        rest.prev = head
        return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
