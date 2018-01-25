#the random function gives a float between 0.0 and 1.0
import random
for i in range(10):
    x = random.random()
    print(x)

#the randint function gives a integer random number btw two numbers
value=random.randint(5,89)
print(value)

#the choice function chooses a number from a list
t=[45,23,34,2,1,78]
seq= random.choice(t)
print(seq)