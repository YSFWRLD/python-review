def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


assert find_max([3, 1, 9]) == 9