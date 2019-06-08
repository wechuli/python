from random import shuffle
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


unique_comb = [[suit, value] for suit in suits for value in values]

print(unique_comb)
shuffle(unique_comb)
print(unique_comb)
print(unique_comb.__len__())
