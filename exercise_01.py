def main(n: int):
    if n < 0:
        print("No grade applicable")
        return
    if n < 60:
        print("Your grade is an F")
        return
    if n < 70:
        print("Your grade is an D")
        return
    if n < 80:
        print("Your grade is an C")
        return
    if n < 90:
        print("Your grade is an B")
        return
    if n < 101:
        print("Your grade is an A")
        return

    print("No grade applicable")
    return


main(int(input("Enter a grade from 0 to 100: ")))
