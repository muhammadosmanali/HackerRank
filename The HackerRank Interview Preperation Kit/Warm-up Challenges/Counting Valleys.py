#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    lvl = 0
    for x in s:
        if x == 'U':
            lvl += 1
        if x == 'D':
            lvl -= 1
        if lvl == 0 and x == 'U':
            count += 1
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
