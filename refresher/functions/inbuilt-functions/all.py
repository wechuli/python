# Return True if all elements of the iterable are truthy(or if the iterable is empty)

print(all([0, 1, 2, 3]))
print(all([char for char in 'eio' if char in 'aeiou']))

people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']


print(all([name[0] == 'C' for name in people])) #this will be True


people.append('Paul')

print(all([name[0] == 'C' for name in people])) # this will be False
