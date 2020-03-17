#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    n = len(a) - 2
    result = []
    for i in range(0, n):
        for j in range(0, n):
            total = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]+ a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            result.append(total)
    return max(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
