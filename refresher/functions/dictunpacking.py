def display_names(first, second):
    print(f'{first} says hello to {second}')


names = dict(first='Paul', second='Wechuli')
display_names(second='Wechuli', first='Paul')
display_names(**names)  # dictionary unpacking with **


def add_and_multiply(a, b, c, **kwargs):
    print(a+b*c)
    print('Other stuff...')
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name='Tony')
add_and_multiply(**data, cat='blue')
