#the keyword break gives us the ability to exit out of a loop whenever we want

while True:
    command = input('What\' your command: ')
    if command == 'exit':
        break
    else:
        print(f'Got it I am now {command}ing')