# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = map(int, input().split())
    set_n = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    happiness = 0
    for x in set_n:
        if x in set_a:
            happiness += 1
        if x in set_b:
            happiness -= 1
    
    print(happiness)

