#!/bin/python3
""""
You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted.
Create a new node with the given integer, insert this node at the desired position and return the head node.
A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.
The head pointer given may be null meaning that the initial list is empty.
As an example, if your list starts as 1->2->3 and you want to insert a node at position 2 with data=4, your new list should be 1->2->4->3

Complete the function insertNodeAtPosition below. It must return a reference to the head node of your finished list.
insertNodeAtPosition has the following parameters:
head: a SinglyLinkedListNode pointer to the head of the list
data: an integer value to insert as data in your new node
position: an integer position to insert the new node, zero based indexing

Input:
The first line contains an integer n, the number of elements in the linked list.
Each of the next n lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer data denoting the data of the node that is to be inserted.
The last line contains an integer position.
3
16
13
7
1
2

Output:
Return a reference to the list head. Locked code prints the list for you.
16 13 1 7
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


def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        head = new_node
    else:
        current_position = 1
        current_node = head.next
        previous_node = head
        while current_position != position:
            previous_node = current_node
            current_node = current_node.next
            current_position += 1
        previous_node.next = new_node
        new_node.next = current_node
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
