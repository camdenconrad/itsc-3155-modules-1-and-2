def main(s: str):
    newS: str = ''
    r = len(s)

    for i in range(r):
        newS = newS + (s[r - i - 1])

    print(newS)


main(input("Enter a string: "))
