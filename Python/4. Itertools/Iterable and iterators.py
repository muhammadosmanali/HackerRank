# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    string = map(str, input().split())
    k = int(input())
    
    c_sk = combinations(string, k)
    c_sk = list(c_sk)
    
    count = 0
    for x in c_sk:
        for y in x:
            if y == 'a':
                count += 1
                break
    result = count / len(list(c_sk))
    print(result)