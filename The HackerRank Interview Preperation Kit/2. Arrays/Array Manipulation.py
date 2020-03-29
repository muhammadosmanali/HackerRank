#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n)
    
    for x in queries:
        arr[x[0]-1] += x[2]
        if x[1]<n:
            arr[x[1]] -= x[2]
    
    m = 0
    t = 0
    for x in range(0, n):
        t += arr[x]
        if t > m:
            m = t
    return m

    return max(arr)

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
