import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr = numpy.array(arr)

    minimum = numpy.min(arr, axis = 1)
    print(numpy.max(minimum, axis=None))

