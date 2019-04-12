def number_compare(a, b):
    try:
        a = float(a)
        b = float(b)
    except:
        print('Please enter numeric values')
        exit()

    if a == b:
        return 'Numbers are equal'
    elif a > b:
        return f'The first number {a} is greater than the second {b}'

    return f'The second number {b} is greater than the first {a}'


a = input('Please enter your first number: ')
b = input('Please enter your second number: ')

print(number_compare(a, b))
