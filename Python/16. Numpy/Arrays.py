import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.flip(arr)
    return numpy.array(arr, dtype=numpy.float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)