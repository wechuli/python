# Write a function called double_return which accepts a function and returns another function. The double_return should decorate a function by returninf two copies of the inner function's return value inside a list
from functools import wraps


def double_return(fn):
    wraps(fn)

    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper


@double_return
def add(a, b):
    return a+b


@double_return
def greet(name):
    return f"Hi I'm {name}"


print(add(12, 20))
print(greet("Paul"))
