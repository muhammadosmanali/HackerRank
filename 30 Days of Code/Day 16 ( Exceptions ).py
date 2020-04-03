#!/bin/python3

import sys


S = input().strip()
try:
    output = int(S)
    print(output)
except:
    print("Bad String")