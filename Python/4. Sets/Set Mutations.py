# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        n1 = input().split()[0]
        s = set(map(int, input().split()))
        getattr(a, n1)(s)
    result = 0
    for x in a:
        result += x
    print(result)