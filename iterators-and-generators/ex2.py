def get_unlimited_multiples(number=1):
    currentmultiple = number
    while True:
        yield currentmultiple
        currentmultiple += number

sevens = get_unlimited_multiples(7)
sevens_array = [next(sevens) for i in range(20)]

ones = get_unlimited_multiples()
ones_array = [next(ones) for i in range(20)]

print(sevens_array)
print(ones_array)
