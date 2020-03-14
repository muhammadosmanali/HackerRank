def swap_case(s):
    s_arr = list(s)
    for x in range(0, len(s_arr)):
        if s_arr[x].islower():
            s_arr[x] = s_arr[x].upper()
        elif s_arr[x].isupper():
            s_arr[x] = s_arr[x].lower()
    
    result = ''.join(s_arr)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)