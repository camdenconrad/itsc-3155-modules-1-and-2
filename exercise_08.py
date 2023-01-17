def main():
    nums = []
    for i in range(10):
        nums.append(int(input(f'Enter number {i + 1}: ')))

    justOnce = []

    for elem in nums:
        if nums.count(elem) == 1:
            justOnce.append(elem)

    print(f'Original list: {nums}')
    print(f'Numbers that appear once: {justOnce}')


main()
