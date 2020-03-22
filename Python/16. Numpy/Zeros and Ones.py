import numpy

if __name__ == '__main__':
    n = tuple(map(int, input().split()))
    
    print(numpy.zeros(n, dtype = numpy.int))
    print(numpy.ones(n, dtype = numpy.int))