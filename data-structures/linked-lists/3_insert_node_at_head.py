
#!/bin/python3
"""
You’re given the pointer to the head node of a linked list and an integer to add to the list.
Create a new node with the given integer, insert this node at the head of the linked list and return the new head node.
The head pointer given may be null meaning that the initial list is empty.

Input:
You have to complete the SinglyLinkedListNode Insert(SinglyLinkedListNode head, int data) method which takes two arguments - the head of the linked list and the integer to insert.
You should NOT read any input from stdin/console.
The input is handled by code in the editor and is as follows:
The first line contains an integer n, denoting the number of elements to be inserted at the head of the list.
The next n lines contain an integer each, denoting the element to be inserted.
5
383
484
392
975
321

Output:
Insert the new node at the head and return the head of the updated linked list.
Do NOT print anything to stdout/console.
The output is handled by the code in the editor and it is as follows:
Print the elements of linked list from head to tail, each in a new line.
321
975
392
484
383
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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtHead(llist_head, data):
    new_head = SinglyLinkedListNode(data)
    if llist_head is not None:
        new_head.next = llist_head
    llist_head = new_head
    return llist_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
