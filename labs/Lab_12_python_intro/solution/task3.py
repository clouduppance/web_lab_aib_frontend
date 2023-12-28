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
    i = maxValue

    while i > 0:
        str = ""
        for item in charValue:
            if myList[item] >= i:
                str += '#'
            else:
                str += ' '
        print(str)
        i -= 1
        
    for c in charValue:
        print(c, end='')


if __name__=='__main__':
    line = input()
    print_histogram(line)