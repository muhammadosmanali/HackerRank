# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    d = deque()
    n = int(input())
    for _ in range(n):
        q = list(input().split())

        if len(q) == 1:
            getattr(d, q[0])()
        elif len(q) > 1:
            getattr(d, q[0])(*[int(q[1])])
    
    print(*[i for i in d])
    
