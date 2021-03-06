#!/bin/python3
"""
You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order.
Delete as few nodes as possible so that the list does not contain any value more than once.
The given head pointer may be null indicating that the list is empty.

Input:
You have to complete the SinglyLinkedListNode* removeDuplicates(SinglyLinkedListNode* head) method which takes one argument - the head of the sorted linked list.
You should NOT read any input from stdin/console.
The input is handled by the code in the editor and the format is as follows:
The first line contains an integer t, denoting the number of test cases.
The format for each test case is as follows:
The first line contains an integer n, denoting the number of elements in the linked list.
The next n lines contain an integer each, denoting the elements of the linked list.
1
5
1
2
2
3
4

Output:
Delete as few nodes as possible to ensure that no two nodes have the same data.
Adjust the next pointers to ensure that the remaining nodes form a single sorted linked list.
Then return the head of the sorted updated linked list.
Do NOT print anything to stdout/console.
The output is handled by the code in the editor and the format is as follows:
For each test case, print in a new line, the data of the linked list after removing the duplicates separated by space.
1 2 3 4 
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


def removeDuplicates(head):
    if head is None:
        return head

    unique_values = []
    unique_values.append(head.data)
    previous = head
    current = head.next

    while current is not None:
        if current.data in unique_values:
            previous.next = current.next
        else:
            unique_values.append(current.data)
            previous = current
        current = current.next

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
