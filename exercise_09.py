def main():

    words = []

    for i in range(5):
        words.append(input("Enter a word: "))

    print(f'Words: {words}')

    oneString: str = words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4]
    print(f'One String: {oneString}')


main()
