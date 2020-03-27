#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    a = []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

    n = len(a) - 2
    result = []
    for i in range(0, n):
        for j in range(0, n):
            total = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]+ a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
            result.append(total)
    print(max(result))
