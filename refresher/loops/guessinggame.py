import random

while True:
    random_number = random.randint(1, 10)
    # print(random_number)

    try:
        user_guess = input('Guess a number between 1 and 10: ')
        user_guess = float(user_guess)
    except:
        print("Please guess a number, I told you I wanted a number, dumbass")
        continue
    while random_number != user_guess:
        if user_guess > random_number:
            print(f'{user_guess} is too high')
        elif user_guess < random_number:
            print(f'{user_guess} is too low')
        user_guess = input('Please try again: ')
        user_guess = float(user_guess)
    option = input(
        'Congrats, you guessed the correct number. Type y to continue and any other letter to quit: ')
   
    if option in ['y', 'yeah', 'yes', 'ya']:
        continue
    else:
        print('Thank you for taking part in this useless game, goodbye')
        break
