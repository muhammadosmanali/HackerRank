# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    r1 = a ** b
    r2 = pow(a, b, m)
    print(r1)
    print(r2)