import random
girls = ['June', 'Maureen', 'Cynthia', 'Jess', 'Molly', 'Beatrice']
numbers = dict()

for i in range(60000):
    choice = random.choice(girls)
    if choice in numbers.keys():
        numbers[choice] += 1
    else:
        numbers[choice] = 0

print(numbers)