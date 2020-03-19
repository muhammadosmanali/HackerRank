#!/bin/python3

import math
import os
import random
import re
import sys

def fun(number):
    if number % 2 != 0:
        print("Weird")
    elif number % 2 == 0 and 2 <= number <= 5:
        print("Not Weird")
    elif number % 2 == 0 and 6 <= number <= 20:
        print("Weird")
    elif number % 2 == 0 and number > 20:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    fun(n)
