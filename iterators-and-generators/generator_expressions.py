# You can create generators from generator expressions
# Generator expressions look a lot like list comprehensions
# Generator expressions use () instead of []


def nums():
    for num in range(1, 10):
        yield num


print(nums)

g = (num for num in range(1, 10))

print(g)
