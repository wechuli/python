numbers = {
    "first": 1,
    "second": 2,
    "third": 3
}


squared_numbers = {key: value**2 for key, value in numbers.items()}
print(squared_numbers)

mydict = {num: num**2 for num in [1, 2, 3, 4, 5, 6, 7]}
print(mydict)
print(mydict[2])

instructor = {
    'name': 'colt',
    'city': 'San Fransico',
    'color': 'purple'
}


instructojoke = {key.upper(): value.upper()
                 for key, value in instructor.items()}

print(instructojoke)
