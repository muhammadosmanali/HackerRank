# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__=='__main__':
    month, day, year = map(int, input().split())
    arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    d = calendar.weekday(year, month, day)
    print(arr[d].upper())
