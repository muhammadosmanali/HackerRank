import numpy

if __name__ == '__main__':
    n = int(input())

    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    A = numpy.array(A)

    B = []
    for _ in range(n):
        B.append(list(map(int, input().split())))
    B = numpy.array(B)

    print(numpy.dot(A, B))




