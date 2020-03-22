import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    arr = numpy.array(arr)
    summ = numpy.sum(arr, axis=0)
    result = 1
    for x in range(n):
        result = result * summ[x]
    print(result)

