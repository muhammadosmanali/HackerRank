import numpy

if __name__ == '__main__':
    arr = numpy.array(list(map(int, input().split())))
    print(numpy.reshape(arr, (3,3)))

