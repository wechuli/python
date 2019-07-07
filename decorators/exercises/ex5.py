#  Write a function called ensure_authorized which accepts a function and returns another function. The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value of "admin". Otherwise , the inner function should return "Unauthorized"

from functools import wraps
from datetime import datetime


def ensure_authorized(fn):
    wraps(fn)

    def wrapper(*args, **kwargs):
        if kwargs.get("role") != "admin":
            raise Exception("Unauthorized")

        return fn(*args, **kwargs)
    return wrapper


@ensure_authorized
def sum_nums(*args, **kwargs):
    return sum(args)

try:
    print(sum_nums(1, 2, 3, 34, 3544, 223, role="admi", name="Pauddl"))
except Exception as e:
    print("Unauthorized")

