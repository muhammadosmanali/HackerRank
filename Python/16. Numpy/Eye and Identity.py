import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(str(numpy.eye(n, m, k=0)).replace('1', ' 1').replace('0', ' 0'))



