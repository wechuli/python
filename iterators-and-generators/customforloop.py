# Custom for loop


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except Exception as execp:
            return
        else:
            func(thing)


sum([1, 2, 3], 0)

my_for('hello', print)
# my_for([1, 2, 3, 4, 4, 34], sum)
