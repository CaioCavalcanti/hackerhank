#!/bin/python3
"""
Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1.
The elements within each of the N sequences also use 0-indexing.
Create an integer, lastAns, and initialize it to 0.
The types of queries that can be performed on your list of sequences (seqList) are described below:
1] Query: 1 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Append integer y to sequence seq
2] Query: 2 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Find the value of element y % size in seq (where size is the size of seq) and assign it to lastAns.
	3] Print the new value of lastAns on a new line
"""

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    print_result = []
    seq_list = [[] for _ in range(n)]
    lastAnswer = 0

    for query in queries:
        target_query = query[0]
        x = query[1]
        y = query[2]
        seq_i = (x ^ lastAnswer) % n
        seq = seq_list[seq_i]
        if target_query == 1:
            seq.append(y)
        elif target_query == 2:
            i = y % len(seq)
            lastAnswer = seq[i]
            print_result.append(lastAnswer)
    return print_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
