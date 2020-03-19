
def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = ['A','E','I','O','U']
    for i in range(0, len(string)):
        if string[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif stuart < kevin:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)