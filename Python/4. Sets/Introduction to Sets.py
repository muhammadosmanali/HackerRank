def average(array):
    array = list(set(array))
    total = 0
    for x in array:
        total += x
    
    result = total / len(array)
    return round(result, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)