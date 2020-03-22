# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    see = set(arr)
    
    a1 = sum(see) * n
    a2 = a1 - sum(arr)
    a3 = a2 // (n-1)
    print(a3)
