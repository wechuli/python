# documenting a function

def say_hello(name):
    # we can add a doc string
    """
    This is a simple function that greets a person depending on the name entered as a parameter.
    """
    return f'Hi,{name}'


fvalue = say_hello('Wechuli')
print(fvalue)
# we can access the doc string
print(say_hello.__doc__)
