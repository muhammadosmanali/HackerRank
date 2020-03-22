import numpy

if __name__ == '__main__':
    numpy.set_printoptions(legacy='1.13')

    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr = numpy.array(arr)

    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(numpy.std(arr, axis=None))

