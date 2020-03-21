# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))
    n = int(input())
    set_n = set(map(int, input().split()))

    result = sorted(list(set_m.symmetric_difference(set_n)))
    print(*result, sep='\n')