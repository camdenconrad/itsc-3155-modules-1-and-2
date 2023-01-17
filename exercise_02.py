def main(s: []):

    print(s[0].endswith(s[1]) or s[1].endswith(s[0]))


def getStrings():
    return [input("Enter string one: "), input("Enter string two: ")]


main(getStrings())
