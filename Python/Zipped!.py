# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    integer_list = map(int, input().split())
    integer_list_arr = []
    for x in integer_list:
        integer_list_arr.append(x)
        
    input_arr = []
    for x in range(integer_list_arr[1]):
        in_list = map(float, input().split())
        input_arr.append(list(in_list))

    n_arr = zip(*input_arr)
    res_arr = []
    for y in n_arr:
        n = 0
        for z in y:
            n += float(z)
        res_arr.append(n)
        
    for x in res_arr:
        print(float(x / integer_list_arr[1]))