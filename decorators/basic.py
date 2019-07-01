def sum(n, func):
    total = 0
    for num in range(n):
        total += func(n)


def square(x):
    return x * x


magic_num = sum(10, square)
print(magic_num)
