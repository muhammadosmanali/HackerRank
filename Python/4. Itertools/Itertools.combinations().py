# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    inputs = map(str, input().split())
    inputs = list(inputs)
    
    c_ab = []
    for x in range(1, int(inputs[1])+1):
        c_ab.append(list(combinations(inputs[0], x)))
    
    tn_cab = []
    for x in c_ab:
        n_cab = []
        for y in range(0, len(x)):
            x[y] = sorted(x[y])
            temp = ''
            for z in range(0, len(x[y])):
                temp += x[y][z]
            n_cab.append(temp)
        tn_cab.append(n_cab)
     
    ntn_cab = []
    for x in tn_cab:
        x = sorted(x)
        ntn_cab.append(x)
    
    for x in ntn_cab:
        for y in range(0, len(x)):
            print(x[y])
