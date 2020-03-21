# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    s = set()
    for x in range(n):
        s.add(str(input()))
    print(len(s))