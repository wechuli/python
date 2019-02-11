#While loops continue to execute while a certain condition is truthy and will end when they belcome falsy

msg = input('Whats the secret password? ')

while msg != 'bananas':
    print("Wrong")
    msg = input('Whats the secret password? ')
print('Correct')

