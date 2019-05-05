# sorted sorts an iterable without changing the value, instead it returns the sorted iterable object

more_numbers = [6, 1, 8, 2]
print(sorted(more_numbers))

# we can change the direction of sorting
print(sorted(more_numbers, reverse=True))

# we can also sort a dictionary using the key parameter
girls = [
    {"name": "June", "rating": 12, "Age": 23},
    {"name": "Mercy", "rating": 6, "Age": 28},
    {"name": "Jess", "rating": 9, "Age": 24}
]

# we can use a lambda

print(sorted(girls, key=lambda user: user['Age'], reverse=True))
