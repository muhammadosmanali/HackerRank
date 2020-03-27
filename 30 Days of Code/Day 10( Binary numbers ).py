#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = []
    while n > 0:
        rem = n % 2
        n = n // 2
        arr.append(rem)
    
    a = ''
    for x in arr:
        a += str(x)

    aa = []
    temp = []
    for x in range(0, len(a)-1):
        if a[x] == a[x+1]:
            temp.append(a[x])
        else:
            temp.append(a[x])
            aa.append(temp)
            temp = []
    temp1=[]
    for x in range(0, len(a)):
        if a[len(a)-1] == a[len(a)-1-x]:
            temp1.append(a[len(a)-1])
        else:
            break
    
    aa.append(temp1)
    
    n_arr = []
    for x in aa:
        if x[0] == '1':
            n_arr.append(len(x))
    print(max(n_arr))
        