#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    n = len(arr)
    for x in range(n):
        print(arr[n-1-x], end=' ')
