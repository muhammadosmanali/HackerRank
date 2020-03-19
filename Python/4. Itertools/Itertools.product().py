# Enter your code here. Read input from STDIN. Print output to STDOUT\
from itertools import product

if __name__ == '__main__':
    a = map(int, input().split())
    b = map(int, input().split())
    p_ab = product(a, b)
    for x in p_ab:
        print(x, end=' ')