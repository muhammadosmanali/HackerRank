if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
            name = input()
            score = float(input())
            arr.append([name, score])

    marks = []
    marks_copy = []
    for x in arr:
        marks.append(x[1])

    for x in marks:
        if x not in marks_copy:
            index_arr.append(x)

    result = []
    for x in index_arr:
        result.append(arr[x][0])
    result.sort()
    for x in result:
        print(x)  marks_copy.append(x)

    index = marks_copy.index(min(marks_copy))
    del marks_copy[index]

    sec_lowest = min(marks_copy)
    index_arr = []

    for x in range(0, len(marks)):
        if marks[x] == sec_lowest:
          
