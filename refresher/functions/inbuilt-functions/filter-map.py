names = ['Lassie', 'Colt', 'Rusty']

comb = list(map(lambda name: f'Your instructor is {name}', filter(
    lambda value: len(value) < 5, names)))
print(comb)

