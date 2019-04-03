# from random import random\
import random


def flip_coin():
    choice = random.choice([0, 1])
    if choice == 0:
        return 'head'
    else:
        return 'tail'


coin_toss_results = dict(head=0, tail=0)

for i in range(100000):
    value = flip_coin()
    coin_toss_results[value] = coin_toss_results[value] + 1
   

print(coin_toss_results)
