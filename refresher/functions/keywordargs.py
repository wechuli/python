def full_name(first, last):
    return f'Your name is {first} {last}'


print(full_name('Paul', 'Wechuli'))
print(full_name(last='Wechuli', first='Paul'))


# When you define a function and use an = you are setting a default parameter
# When you invoke a function and use an  = you are making a keyword argument