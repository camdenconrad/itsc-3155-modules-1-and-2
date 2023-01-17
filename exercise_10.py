def main(s):
    length: int = int((len(s) + 2) / 3)
    finalList = []
    counter: int = 0

    for i in range(length):
        quickList = []
        for j in range(3):
            try:
                quickList.append(s[counter])
                counter += 1
            except IndexError:
                pass

        finalList.append(quickList.copy())
        quickList.clear()

    print(finalList)


main(input("Enter a string: "))
