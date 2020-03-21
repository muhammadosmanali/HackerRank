# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    inputs = map(str, input().split())
    inputs = list(inputs)
    p_ab = permutations(inputs[0], int(inputs[1]))
    
    result = []
    for x in p_ab:
        temp = ''
        for y in range(int(inputs[1])):
            temp += x[y]
        result.append(temp)
    result = sorted(result)
    for x in result:
        print(x)