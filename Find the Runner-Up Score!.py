if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = []
    for x in arr:
        array.append(x)

    n_array = []
    for y in array:
        if y not in n_array:
            n_array.append(y)
        
    index = n_array.index(max(n_array))
    del n_array[index]
    print(max(n_array))
