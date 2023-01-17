def main():
    allNums, evenNums = [], []

    while True:
        strIn = input("Enter a number or QUIT to quit: ")
        if strIn == 'QUIT':
            break
        else:
            allNums.append(int(strIn))
            if int(strIn) % 2 == 0:
                evenNums.append(int(strIn))

    print(f'All nums: {allNums}')
    print(f'Even nums: {evenNums}')


main()
