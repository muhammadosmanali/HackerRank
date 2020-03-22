import numpy

if __name__ == '__main__':
    numpy.set_printoptions(sign=' ')
    arr = list(map(float, input().split()))

    print(numpy.floor(arr))
    print(numpy.ceil(arr))
    print(numpy.rint(arr))