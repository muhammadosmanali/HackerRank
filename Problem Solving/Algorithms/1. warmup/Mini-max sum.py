#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    wo_max = sum(arr) - max(arr)
    wo_min = sum(arr) - min(arr)
    print(wo_max, wo_min)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
