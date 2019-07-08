# We can use a decorator function to ensure restrictions in the function e.g. encuring no keyword arguments or certain data types
from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No key word arguments allowed")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f'hi there {name}')


greet(name = "Paul")
