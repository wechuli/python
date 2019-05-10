
def foobar():
    print('I run')


try:
    foobar()
except NameError as err:
    print(err)
