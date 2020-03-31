class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0

    def computeDifference(self):
        a = self.__elements
        n = len(self.__elements)
        arr = []
        for x in range(n):
            for y in range(x, n):
                r = abs(a[x] - a[y])
                arr.append(r)
        self.maximumDifference = max(arr)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)