# Write a function called get_multiples which accepts a number and a count, and returns a generator that yields the first count of multiples of the number


def get_multiples(number=1, count=10):
    current_number = number
    iterations = 0
    while count > iterations:
        yield current_number
        current_number += number
        iterations += 1

default = get_multiples()
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())
print(default.__next__())

evens = get_multiples(2,3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))

