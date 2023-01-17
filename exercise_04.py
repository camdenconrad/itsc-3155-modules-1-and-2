def main(n: int):
    floats = []
    total: float = 0.0

    for i in range(n):
        floats.append(float(getFloat()))
        total += floats[len(floats) - 1]

    print(f'List: {floats}')
    print(f'Average: {(total / len(floats))}')


def getFloat():
    return input("Enter float: ")


main(int(input("Enter number: ")))
