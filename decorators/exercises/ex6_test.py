# Write a function called delay which accepts a time and returns an inner function that accepts a function.When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. Defore starting the timer, delay will also print a message informaing the user that there will be a delay before the decorated function gets run

from time import sleep
from functools import wraps


def delay_execution(fn):
    wraps(fn)

    def wrapper(*args, **kwargs):
        print("Wait for it ...")
        sleep(3)        
        return fn(*args, **kwargs)
    return wrapper


@delay_execution
def sum_nums(a, b):
    return a + b


print(sum_nums(12, 58))
