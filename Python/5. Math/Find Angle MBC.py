# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    result = math.atan2(AB, BC)
    result = math.degrees(result)
    print(str(round(result)) + '°')