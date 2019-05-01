# use * and ** as parameters to a function and outside a function
# leverage dictionary and tuple unpacking to create more flexible functions

#  * a special operator we can pass to a function, gathers all the remaining arguments as a tuple

# collects the parameters in a tuple


def sum_all_nums(*args):
    return sum(args)


print(sum_all_nums(1, 2, 3, 5))
print(sum_all_nums(1, 2, 3))


def with_other_params(num1, *args):
    print(args)
    print(num1)


with_other_params(1, 2, 3, 4)
