#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n
    i = 0
    for x in s:
        if x == 'a':
            i+=1
    if i == 0:
        return i
    count = ((n // len(s)) * s.count('a')) + s[:n % len(s)].count('a') 
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
