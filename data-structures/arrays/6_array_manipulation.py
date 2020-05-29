#!/bin/python3
"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros n = 10. Your list of queries is as follows:
a b k
1 5 3
4 8 7
6 9 1

Add the values of k between the indices a and b inclusive:
index->  1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
	    [3,3,3, 3, 3,0,0,0,0, 0]
	    [3,3,3,10,10,7,7,7,0, 0]
	    [3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed

Complete the function arrayManipulation below. It must return an integer, the maximum value in the resulting array.
arrayManipulation has the following parameters:
n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

Input Format:
The first line contains two space-separated integers n and m, the size of the array and the number of operations.
Each of the next m lines contains three space-separated integers a, b and k, the left index, right index and summand.

Output format:
Return the integer maximum value in the finished array.

"""

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    arr = [0] * n
    max_value = 0
    for query in queries:
        left = query[0] - 1
        right = query[1]
        summand = query[2]

        arr[left] += summand
        if right != n:
            arr[right] -= summand

    max_row = 0
    for i in arr:
        max_row += i
        if max_row > max_value:
            max_value = max_row
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
