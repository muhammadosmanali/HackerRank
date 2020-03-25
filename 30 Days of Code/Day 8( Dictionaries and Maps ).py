# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    dic = {}

    for _ in range(n):
        x = input().split()
        dic[x[0]] = x[1]
    while True:
        try:
            name = str(input())
            if name in dic:
                print(name + "=" + dic[name])
            else: 
                print("Not found")   
        except: 
            break
