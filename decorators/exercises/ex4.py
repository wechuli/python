# Write a function called only_ints which accepts a fucntion and returns another function. The fucntion passed to it should only be invoked if all of the arguments passed to it are integers. Otherwise the inner fucntion should retyurn "Please only invoke with integers"

from functools import wraps


def only_ints(fn):
    wraps(fn)

    def wrapper(*args):
        for value in args:
            if not isinstance(value, int):
                raise TypeError("Please only invoke with integers")
        return fn(*args)
    return wrapper

# Alternative implementation
# def only_ints(fn):
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         if any([arg for arg in args if type(arg) != int]):
#             return "Please only invoke with integers."
#         return fn(*args, **kwargs)
#     return inner

print(all([1, 2, 3, 4," "]))


@only_ints
def sum_ints(*args):
    return sum(args)


print(sum_ints(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(sum_ints(1, 2, 3, 4, 5, 6, 7, 8, 9))
