
def is_even(num):
    return num % 2 == 0


# The brunt first thought way
def partition(array, callback):
    falsy = list()
    truthy = list()
    for item in array:
        verdict = callback(item)
        if verdict:
            truthy.append(item)
        else:
            falsy.append(item)
    return [truthy, falsy]



print(partition([1, 2, 3, 4], is_even))

# Using list comprehensions
def partition_comp(array, callback):
    return [[item for item in array if callback(item)], [item for item in array if not callback(item)]]


print(partition([1, 2, 3, 4], is_even))
