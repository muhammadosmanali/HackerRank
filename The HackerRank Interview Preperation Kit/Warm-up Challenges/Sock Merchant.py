#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    n_arr = []
    for x in ar:
        if x not in n_arr:
            n_arr.append(x)
            
    result = []
    for x in n_arr:
        n_result = []
        for y in ar:
            if y == x:
                n_result.append(y)
        result.append(n_result)
        
    count = 0
    for x in result:
        count += int(len(x)/2)
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
