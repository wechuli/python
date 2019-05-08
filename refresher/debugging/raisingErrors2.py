

def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError('text must be an instance of a string')
    if type(color) is not str:
        raise TypeError('color must be an instance of a string')
    if color not in colors:
        raise ValueError('color is invalid')

    print(f'Printed {text} in {color}')


colorize('hello', 'chicken')
colorize(1, 'red')
