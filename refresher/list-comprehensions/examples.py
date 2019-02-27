# Generating a sequence of numbers without doing anything to the argument
munumbers = [numbers for numbers in range(1, 67)]
print(munumbers)


# Manipulating the returned value
anotherone = [num + 7 for num in range(1, 10)]
print(anotherone)

# working with strings and list comprehensions
names = ['Paul', 'WeCHULI', 'JECINTa', 'NOrman', 'maninga', 'naTion']
print(names)
names_lower = [name.lower() for name in names]
print(names_lower)

# working with bools
values = [bool(val) for val in [0, [], '', True, 'some_value']]
print(values)


# converting numbers to strings
numbers = [1, 2, 3, 4, 3, 3, 3, 4, 2, 3, 2, 3, 2, 3, 3, 3, 3]

newnumbers = [str(number) for number in numbers]
print(newnumbers)
