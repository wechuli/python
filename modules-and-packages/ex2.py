import keyword


def contains_keyword(*args):
    for key in args:
        if keyword.iskeyword(key):
            return True
    return False


print(contains_keyword('hello', 'goodbye'))
print(contains_keyword('def', 'haha', 'lol', 'chicken', 'alaska'))
print(contains_keyword('four', 'for', 'if'))
print(contains_keyword('blah', 'doggo', 'crab', 'anchor'))
print(contains_keyword('grizzly', 'ignore', 'return', 'False', 'JustRandom'))
