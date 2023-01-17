def main():
    common = []
    list2 = getList('one')
    list1 = getList('two')
    for elem in list1:
        if list2.count(elem) > 0 or common.count(elem) < 1:  # check if common, and if already in common list
            common.append(elem)

    print(list1)
    print(list2)
    print(common)


def getList(s: str):
    locList = []
    for i in range(5):
        locList.append(int(input(f'Enter a number for list {s}: ')))

    return locList


main()
