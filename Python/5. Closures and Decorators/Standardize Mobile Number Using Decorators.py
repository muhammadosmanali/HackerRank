import math

def wrapper(f):
    def fun(l):
        k = 5
        n_l=[]
        for x in l:
            if x[0] == '0' and len(x) == 11:
                x = x[1:]
            if x[0] == '+':
                x = x[3:]
            if len(x) == 10:
                sub_list = [x[k*i:k*i+k] for i in range(0,math.ceil(len(x)/k))]
                result = '+91 ' + sub_list[0] + ' ' + sub_list[1] 
                n_l.append(result)
            if len(x) > 10:
                s = x[2:]
                sub_list = [s[k*i:k*i+k] for i in range(0,math.ceil(len(s)/k))]
                result = '+' + x[:2] + ' ' + sub_list[0] + ' ' + sub_list[1]
                n_l.append(result)
        f(n_l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


