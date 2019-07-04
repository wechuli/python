def sum(n, func):
    total = 0
    for num in range(n):
        total += func(n)

    return total


def square(x):
    return x * x


def cude(x):
    return x*x*x


magic_num = sum(10, square)
magic_num2 = sum(10, cude)
print(magic_num)
print(magic_num2)
