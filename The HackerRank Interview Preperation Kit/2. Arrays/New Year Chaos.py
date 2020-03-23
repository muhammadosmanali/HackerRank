#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    q = [x-1 for x in q]
    for i,x in enumerate(q):
        if x - i > 2:
            print("Too chaotic")
            return

        for y in range(max(x-1,0), i):
            if x < q[y]:
                count += 1
    if count != 0:
        print(count)

        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
