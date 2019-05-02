

def calculate(make_float, operation, first, second, message=None):

    if make_float:
        first = float(first)
        second = float(second)
    else:
        first = int(first)
        second = int(second)
    if operation == 'add':
        if message:
            return f'{message} {first + second}'
        else:
            return f'The result is {first + second}'
    elif operation == 'subtract':
        if message:
            return f'{message} {first - second}'
        else:
            return f'The result is {first - second}'
    elif operation == 'multiply':
        if message:
            return f'{message} {first * second}'
        else:
            return f'The result is {first * second}'
    elif operation == 'divide':
        if message:
            return f'{message} {first / second}'
        else:
            return f'The result is {first / second}'
    else:
        return 'Unsupported operation'


print(calculate(make_float=False, operation='add',
                message='You just added', first=2, second=4))  # "You just added 6"
print(calculate(make_float=True, operation='divide',
                first=3.5, second=5))  # "You just added 6"
