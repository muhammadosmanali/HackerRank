# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(str(input()))
    
    for x in arr:
        if re.match(r'^[+-]?\d*?\.{1}\d+$', x):
            print("True")
        else:
            print("False")