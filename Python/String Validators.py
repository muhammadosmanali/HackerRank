if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for x in s:
        if x.isalnum():
            isalnum = True
            break

    for x in s:
        if x.isalpha():
            isalpha = True
            break

    for x in s:
        if x.isdigit():
            isdigit = True
            break

    for x in s:
        if x.islower():
            islower = True
            break

    for x in s:
        if x.isupper():
            isupper = True
            break

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)