def main(s: str):
    lowCase = []
    upCase = []

    for i in range(len(s)):
        if s[i].islower():
            lowCase.append(s[i])
        else:
            upCase.append(s[i])

    newS: str = ''
    for i in range(len(lowCase)):
        newS = newS + lowCase[i]

    for i in range(len(upCase)):
        newS = newS + upCase[i]

    print(newS.replace(' ', ''))


main(input("Enter a string: "))
