print(max([1, 2, 3, 4, 55, 334]))
print(max(33, 4, 3, 244))
print(max('a', 'b', 'c'))

print(min([1, 2, 3, 4, 55, 334]))
print(min(33, 4, 3, 244))
print(min('a', 'b', 'c'))


names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# find the length of the shortest name
print(min(len(name) for name in names))


# we can use a lambda instead to return the actual item

print(max(names, key=lambda n: len(n)))
