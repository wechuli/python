# Write a function called show_args which accepts a function and returns another function. Before invoking the function passed to it, show_args should be responsible for pritnign two things: a tuple of the positional arguments, and a dictionary of the keword arguments

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Function that displays the args and kwargs of another function"""
        print(f'Here are the args: {args}')
        print(f'Here are the kwargs: {kwargs}')
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing("paul", 1, 2, 3, 3, 4, a="good byte", b=23, c=[
           "d", 1, 2], d={"key": "value", "this": "that"})
