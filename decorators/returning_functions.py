from random import choice
#  we can return functions from other functions


def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAHA', 'lol', 'tehehe'))
        return l
    return get_laugh

# We can pass functins to the inner functinos. Inner functions can access outer function scope


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAHA', 'lol', 'tehehe'))
        return f'{laugh} {person}' # person was passed in by the outer function
    return get_laugh


laugh = make_laugh_func()
print(laugh())


laugh_at = make_laugh_at_func("Linda")
print(laugh_at())
print(laugh_at())
print(laugh_at())