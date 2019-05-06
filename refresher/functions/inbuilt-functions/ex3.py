

def max_magnitude(array):
    return max(abs(number) for number in array)


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))


def sum_even_values(*args):
    return sum(number for number in args if number % 2 == 0)


print(sum_even_values(1, 2, 3, 4, 5, 6, 7))
print(sum_even_values(4, 2, 1, 10))
print(sum_even_values(1))


def sum_floats(*args):
    return sum(number for number in args if type(number) == float)


print(sum_floats(1.5, 2.4, 'awesome', [], 1))  # 3.9
print(sum_floats(1, 2, 3, 4, 5))  # 0
