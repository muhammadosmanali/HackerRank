if __name__ == '__main__':
    N = int(input())
    input_list = []
    for _ in range(N):
        input_list.append(input().split())

    l = []

    for x in input_list:
        if x[0] == 'insert':
            l.insert(int(x[1]), int(x[2]))
        if x[0] == 'append':
            l.append(int(x[1]))
        if x[0] == 'remove':
            l.remove(int(x[1]))
        if x[0] == 'sort':
            l.sort()
        if x[0] == 'reverse':
            l.reverse()
        if x[0] == 'pop':
            l.pop()
        if x[0] == 'print':
            print(l)