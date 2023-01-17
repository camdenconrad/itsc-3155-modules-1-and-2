import math


def main(n: int):
    i = 1
    while i < n + 1:
        print(math.pow(i, 3))
        i += 1


main(int(input("Enter a number: ")))
