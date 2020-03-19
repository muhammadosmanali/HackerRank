# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = str(input())

    aa = []
    temp = []
    for x in range(0, len(a)-1):
        if a[x] == a[x+1]:
            temp.append(a[x])
        else:
            temp.append(a[x])
            aa.append(temp)
            temp = []
    temp1=[]
    for x in range(0, len(a)):
        if a[len(a)-1] == a[len(a)-1-x]:
            temp1.append(a[len(a)-1])
        else:
            break

    aa.append(temp1)

    result = []
    for x in aa:
        count = 0
        for y in x:
            count += 1
        n_s = '(' + str(count) + ', ' + x[0] + ')'
        result.append(n_s)

    for x in result:
        print(x, end=' ')
