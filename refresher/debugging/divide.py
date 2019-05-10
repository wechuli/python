def divide(a, b):
    try:
        result = a/b
        return result
    # we could if we want catch several errors at a go with a tuple e.g (ZeroDivisionError,TypeError)
    except ZeroDivisionError as error:
        print(error)
    except TypeError as error:
        print(error)
    else:
        print(f'{a} divided by {b} is {result}')


divide(5, 6)
print(divide(1, 2))
print(divide(1, 0))
print(divide('as', 1))
