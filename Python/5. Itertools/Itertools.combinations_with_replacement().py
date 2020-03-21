# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    inputs = map(str, input().split())
    inputs = list(inputs)
    p_ab = combinations_with_replacement(inputs[0], int(inputs[1]))
    
    np_ab = []
    for x in p_ab:
        x = sorted(x)
        np_ab.append(x)
    
    result = []
    for x in np_ab:
        temp = ''
        for y in range(int(inputs[1])):
            temp += x[y]
        result.append(temp)
    result = sorted(result)
    for x in result:
        print(x)