# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(str, input().split())))

    for x in arr:
        if x[1] == '0':
            print("Error Code: integer division or modulo by zero")
        
        elif re.match('[~!@#$%^&*]', x[0]):
            print("Error Code: invalid literal for int() with base 10: '{}'".format(x[0]))
        elif re.match('[~!@#$%^&*]', x[1]):
            print("Error Code: invalid literal for int() with base 10: '{}'".format(x[1]))
        else:
            print(int(int(x[0])/int(x[1])))