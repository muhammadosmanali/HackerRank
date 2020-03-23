# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        m = int(input())
        arr.append(list(map(int, input().split())))

    for x in arr:
        i = 0
        m = len(x)
        while i < m-1 and x[i] >= x[i+1]:
            i += 1
        while i < m-1 and x[i] <= x[i+1]:
            i += 1
        
        if i == m-1:
            print("Yes")
        else:
            print("No")
