#!/bin/python3
"""
Given a 2D Array, A, we define an hourglass in to be a subset of values
with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g
There are hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Complete the function hourglassSum below. It should return an integer, the maximum hourglass sum in the array.
hourglassSum has the following parameter(s):
arr: an array of integers
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    max_sum = None
    for i in range(4):
        for j in range(4):
            hourglass_sum = get_hourglass_sum(i, j)
            if max_sum is None or hourglass_sum > max_sum:
                max_sum = hourglass_sum
    return max_sum


def get_hourglass_sum(row, col):
    hourglass_sum = 0
    hourglass_sum += arr[row][col]
    hourglass_sum += arr[row][col + 1]
    hourglass_sum += arr[row][col + 2]
    hourglass_sum += arr[row + 1][col + 1]
    hourglass_sum += arr[row + 2][col]
    hourglass_sum += arr[row + 2][col + 1]
    hourglass_sum += arr[row + 2][col + 2]
    return hourglass_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
