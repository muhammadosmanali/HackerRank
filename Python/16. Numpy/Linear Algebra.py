import numpy

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(float, input().split())))
    arr = numpy.array(arr)
    print(numpy.around(numpy.linalg.det(arr), 2))

