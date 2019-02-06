import random
girls = ['June', 'Maureen', 'Cynthia', 'Jess', 'Molly', 'Beatrice']
userInput = input('How many times do I have to tell you: ')
try:
    userInput = int(userInput)
except:
    print('Please enter a numeric number')
    exit()

for i in range(userInput):
    print(f'{i+1}.Clean up your room')
    print(random.choice(girls))
