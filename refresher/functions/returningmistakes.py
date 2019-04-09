def sum_odd_numbers_wrong(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total # the return is at the wrong indentation level


def sum_odd_numbers_correct(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers_wrong([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sum_odd_numbers_correct([1, 2, 3, 4, 5, 6, 7, 8, 9]))
