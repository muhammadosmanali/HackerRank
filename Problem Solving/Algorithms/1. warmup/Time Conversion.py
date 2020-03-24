#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    s = s.split(":")
    if s[2][2:] == 'PM':
        if s[0] == '12' and int(s[1]) > 0:
            pass
        else:
            s[0] = str(int(s[0]) + 12)
    elif s[2][2:] == 'AM' and s[0] == '12':
        s[0] = '0' + str(int(s[0]) - 12)
    s[2] = s[2][:2]
    print(s[0] + ':' + s[1] + ':' + s[2])

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)


