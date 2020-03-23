#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    lst = sorted(input())
    for x in OrderedCounter(lst).most_common(3):
        print(*x)
    
    