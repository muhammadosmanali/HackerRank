# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    input_arr = input().split()
    x = int(input_arr[0])
    print(eval(input()) == int(input_arr[1]))