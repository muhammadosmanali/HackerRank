import math
from collections import OrderedDict

def merge_the_tools(string, k):
    sub_list = [string[k*i:k*i+k] for i in range(0,math.ceil(len(string)/k))]

    for x in sub_list:
        temp = "".join(OrderedDict.fromkeys(x))
        print(temp)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)