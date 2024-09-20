#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decrypt' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY code_array
#  2. INTEGER key
#

def next_index(current_index, length):
    return (current_index + 1) % length

def prev_index(current_index, length):
    return (current_index - 1 + length) % length

def decrypt(code_array, key):
    
    n = len(code_array)
    decrypted = [0] * n    
    window_sum = 0

    if key == 0:
        return decrypted

    if key > 0:
        for i in range(1, key + 1):
            window_sum += code_array[i % n]

        for i in range(n):
            decrypted[i] = window_sum
            window_sum -= code_array[(i + 1) % n]
            window_sum += code_array[(i + key + 1) % n]

    elif key < 0:
        for i in range(1, abs(key) + 1):
            window_sum += code_array[(-i) % n]

        for i in range(n):
            decrypted[i] = window_sum
            window_sum -= code_array[(i - abs(key)) % n]
            window_sum += code_array[i % n]

    return decrypted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    code = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    result = decrypt(code, k)

    fptr.write(str(result) + '\n')

    fptr.close()