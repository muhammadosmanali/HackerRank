# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(str(input()))
    
    n_arr = []
    for x in arr:
        n_char = ''
        for y in range(len(x)):
            if y % 2 == 0:
                n_char += x[y]
        n_char += ' '
        for z in range(len(x)):
            if z % 2 != 0:
                n_char += x[z]
        n_arr.append(n_char)

    for x in n_arr:
        print(x)