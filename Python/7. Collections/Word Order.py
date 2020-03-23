# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':

    # Takes less time to execute
    n = int(input())

    dic = OrderedDict()

    for _ in range(n):
        s = str(input())
        dic.setdefault(s, 0)
        dic[s] += 1
    
    print(len(dic))
    print(*dic.values(), end=' ')

    # Takes more time to execute
    arr = []
    for _ in range(n):
        arr.append(str(input()))

    arr_wo_dup = []
    for x in arr:
        if x not in arr_wo_dup:
            arr_wo_dup.append(x)

    print(len(arr_wo_dup))

    occurance = []
    for x in arr_wo_dup:
        count = 0
        for y in arr:
            if y == x:
                count += 1
        occurance.append(count)
    
    for x in occurance:
        print(x, end=' ')