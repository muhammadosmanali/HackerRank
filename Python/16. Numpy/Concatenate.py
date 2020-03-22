import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().split())

    matrix1 = []
    matrix2 = []
    for x in range(n):
        arr = map(int, input().split())
        matrix1.append(list(arr))
    for x in range(m):
        arr = map(int, input().split())
        matrix2.append(list(arr))
    
    n_arr = numpy.concatenate(
        (numpy.array(matrix1),
        numpy.array(matrix2))
    )
    print(n_arr)

