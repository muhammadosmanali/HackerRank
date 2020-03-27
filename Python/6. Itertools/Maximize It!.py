# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    k, m = map(int, input().split())
    
    arr = []
    for x in range(k):
        s = list(map(int, input().split()))[1:]
        arr.append(s)

    products = product(*arr)
    arr = []
    for x in list(products):
        temp = 0
        for y in x:
            temp += y**2
        temp = temp % m
        arr.append(temp)
    print(max(arr))
            
            