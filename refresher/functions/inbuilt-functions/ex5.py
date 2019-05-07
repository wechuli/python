# Write a function called triple_and_filer. This function should accept alist of numbers, filter out every number that is not divisible by 4 and return a new list where every remaining number is tripled


# Using a list comprehension
def triple_and_filter(array):
    return [number*3 for number in array if number % 4 == 0]


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))


# Using filter

def triple_and_filter2(array):
    return list(map(lambda x: x*3, filter(lambda x: x % 4 == 0, array)))


print(triple_and_filter2([1, 2, 3, 4]))
print(triple_and_filter2([6, 8, 10, 12]))
