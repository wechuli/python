import random

print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Make your move: ')
player2 = random.choice(['rock', 'paper', 'scissors'])

try:
    p1_choice = player1.lower()
    p2_choice = player2.lower()

    if p1_choice in ['rock', 'paper', 'scissors'] and p2_choice in ['rock', 'paper', 'scissors']:
        if p1_choice == p2_choice:
            print('The game ends in a draw! sweet')
        if p1_choice == 'rock' and p2_choice == 'scissors':
            print('Congratulations, you won!')
        elif p1_choice == 'rock' and p2_choice == 'paper':
            print('The computer wins, sorry')
        elif p1_choice == 'scissors' and p2_choice == 'paper':
            print('Congratulations, you won!')
        elif p1_choice == 'scissors' and p2_choice == 'rock':
            print('The computer wins, sorry')
        elif p1_choice == 'paper' and p2_choice == 'rock':
            print('Congratulations, you won!')
        elif p1_choice == 'paper' and p2_choice == 'scissors':
            print('The computer wins, sorry')
    else:
        print('Invalid choice by one of the players')
        exit()
except:
    print('You did not enter a valid choice')

# You could refactor the and statements with nested conditional statements
# Even better, you could only check for when player one wins and everything else will mean 2 won
