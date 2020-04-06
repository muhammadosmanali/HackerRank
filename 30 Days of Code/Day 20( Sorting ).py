#!/bin/python3

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numOfSwaps = 0
for x in range(n):
    for y in range(n-1):
        if a[y] > a[y+1]:
            temp = a[y]
            a[y] = a[y+1]
            a[y+1] = temp
            numOfSwaps += 1
    if numOfSwaps == 0:
        break

print("Array is sorted in {} swaps.".format(numOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))