# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = defaultdict(list)
    b = []
    
    for x in range(n):
        a[str(input())].append(x+1)
    for y in range(m):
        b.append(str(input()))
    
    for z in b:
        if z in a:
            print(*a[z])
        else:
            print(-1)
