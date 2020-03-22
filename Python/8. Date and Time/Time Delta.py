from datetime import datetime as dt


if __name__ == '__main__':
    n = int(input())
    f = '%a %d %b %Y %H:%M:%S %z'

    for _ in range(n):
        t1 = dt.strptime(input(), f)
        t2 = dt.strptime(input(), f)
        result = abs((t1 - t2).total_seconds())
        print (int(result))