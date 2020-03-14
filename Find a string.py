def count_substring(string, sub_string):
    count = 0
    len_sub = len(sub_string)
    for x in range(0, len(string)):
        if len(string)-1-x >= len_sub-1:
            check_str = ''
            i = 0
            for y in range(0, len_sub):
                check_str += string[x+i]
                i += 1
            
            if check_str == sub_string:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count