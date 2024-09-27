#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'nextGreaterElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num_1
#  2. INTEGER_ARRAY num_2
#

def nextGreaterElement(num_1, num_2):
    mapping = {}  
    stack = []
    for num in num_2:
        while stack and num > stack[-1]:
            mapping[stack.pop()] = num
        stack.append(num)
    while stack:
        mapping[stack.pop()] = -1
    result = []
    for num in num_1:
        result.append(mapping.get(num, -1))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(raw_input().strip())

    n1 = map(int, raw_input().rstrip().split())

    k1 = int(raw_input().strip())

    n2 = map(int, raw_input().rstrip().split())

    result = nextGreaterElement(n1, n2)

    fptr.write(str(result) + '\n')

    fptr.close()
