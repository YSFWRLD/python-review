def find_max(numbers):
    biggest = numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i] > biggest:
            biggest = numbers[i]
    return biggest


assert find_max([3, 1, 9]) == 9