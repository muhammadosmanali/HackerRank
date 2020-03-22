import numpy

if __name__ == '__main__':
    P = numpy.array(list(map(float, input().split())))
    x = int(input())

    print(numpy.polyval(P, x))



