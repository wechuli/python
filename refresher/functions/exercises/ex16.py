

def intersection(first, second):
    first = set(first)
    second = set(second)
    return list(first.intersection(second))


print(intersection(['a', 'b', 'z'], ['x', 'y', 'z', 'a']))
