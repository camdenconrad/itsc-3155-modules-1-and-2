def main():
    while True:
        row = int(input("Enter row number (1 to 5): "))
        if 0 < row < 6:
            break

    while True:
        col = int(input("Enter col number (1 to 5): "))
        if 0 < col < 6:
            break

    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    board[row - 1][col - 1] = 1

    for i in range(5):
        print(board[i])


main()
