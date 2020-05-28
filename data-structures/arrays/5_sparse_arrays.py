#!/bin/python3
"""
There is a collection of input strings and a collection of query strings.
For each query string, determine how many times it occurs in the list of input strings.
Complete the function matchingStrings, it must return an array of integers representing the frequency of occurrence of each query string in strings.
matchingStrings has the following parameters:
strings - an array of strings to search
queries - an array of query strings
"""

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.


def matchingStrings(strings, queries):
    result = []
    for i in range(len(queries)):
        result.append(strings.count(queries[i]))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
