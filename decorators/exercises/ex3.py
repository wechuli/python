# Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than 3 positional arguments passed to it. Otherwise, the inner function should return 'Too many arguments'
from functools import wraps


def ensure_fewer_than_three_args(fn):
    wraps(fn)

    def wrapper(*args):
        if len(list(args)) >= 3:
            raise ValueError("Too many arguments")
        return fn(*args)
    return wrapper


@ensure_fewer_than_three_args
def add_nums(*args):
    return sum(args)


print(add_nums(1,2334,23))
