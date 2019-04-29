
def multiply_even_numbers(numbers):
    result = 1
    for number in numbers:
        if number % 2 == 0:
            result *= number
    return result


print(multiply_even_numbers([2, 3, 4, 5, 6]))
