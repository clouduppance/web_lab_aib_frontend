def print_histogram(line):
    maxValue = 0
    myList = {}

    for item in line:
        if item == ' ':
            continue
        if item in myList:
            myList[item] += 1
            maxValue = max(maxValue, myList[item])
        else:
            myList[item] = 1

    charValue = list(myList.keys())
    charValue.sort()
    level = maxValue

    while level > 0:
        str = ""
        for item in charValue:
            if myList[item] >= level:
                str += '#'
            else:
                str += ' '                
        print(str)

        level -= 1

    for char in charValue:
        print(char, end='')


if __name__=='__main__':
    line = input()
    print_histogram(line)