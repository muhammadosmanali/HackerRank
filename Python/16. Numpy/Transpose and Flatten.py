import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        matrix = map(int, input().split())
        arr.append(list(matrix))
    n_arr = numpy.array(arr)
    print(numpy.transpose(n_arr))
    print(n_arr.flatten())