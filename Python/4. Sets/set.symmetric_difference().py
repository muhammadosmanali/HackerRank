# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    n_arr = set(map(int, input().split()))
    m = int(input())
    m_arr = set(map(int, input().split()))

    result = n_arr.symmetric_difference(m_arr)
    print(len(result))