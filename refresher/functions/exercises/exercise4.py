

def product(a, b):
    try:
        a = float(a)
        b = float(b)
    except:
        print('Please enter a numeric number')
        exit()
    return a * b


a = input('Please insert your first number: ')
b = input('Please insert your second number: ')

print(product(a, b))
