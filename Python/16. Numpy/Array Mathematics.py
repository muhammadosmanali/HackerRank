import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    A, B = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))

    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)
    print(A**B)





