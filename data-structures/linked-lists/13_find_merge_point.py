#!/bin/python3
"""
Given pointers to the head nodes of 2 linked lists that merge together at some point, find the Node where the two lists merge.
It is guaranteed that the two head Nodes will be different, and neither will be NULL.
Complete the int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) method so that it finds and returns the data value of the Node where the two lists merge.

Input:
Do not read any input from stdin/console.
The findMergeNode(SinglyLinkedListNode,SinglyLinkedListNode) method has two parameters, head1 and head2, which are the non-null head Nodes of two separate linked lists that are guaranteed to converge.
1
 \
  2->3->Null
 /
1
1->2
    \
     3->Null
    /
   1

Contraints:
The lists will merge
head1, head2 != None
head1 != head2

Output:
Do not write any output to stdout/console.
Each Node has a data field containing an integer.
Return the integer data for the Node where the two lists merge.
2
3
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


def findMergeNode(head1, head2):
    """
    By linking the tail of a node to the head of the other, we'll be able to find
    the intersection, since the number of nodes traveled from head1->tail1->head2->intersection
    will be equal to head2->tail2->head1->intersection
    """
    current1 = head1
    current2 = head2

    while current1 != current2:
        if current1.next is None:
            current1 = head2
        else:
            current1 - current1.next

        if current2.next is None:
            current2 = head1
        else:
            current2 = current2.next

    return current2.data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
