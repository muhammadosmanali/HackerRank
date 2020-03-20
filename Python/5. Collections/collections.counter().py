# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    x = int(input())
    
    shoes = map(int, input().split())
    shoes = list(shoes)
    
    n = int(input())
    
    cus = []
    for _ in range(n):
        in_cus = map(int, input().split())
        cus.append(list(in_cus))
    
    earning = 0
    for x in cus:
        if x[0] in shoes:
            i = shoes.index(x[0])
            del shoes[i]
            earning += x[1]
    print(earning)
            