def split_and_join(line):
    n_line = line.split(" ")
    n_line = "-".join(n_line)
    return n_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)