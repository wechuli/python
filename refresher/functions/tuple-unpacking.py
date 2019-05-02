

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)


# passing  a list and unpacking
numlist = [1, 2, 3, 4, 5]
sum_all_values(*numlist)
# tuple
numtuple = (1, 2, 3, 4, 5)
sum_all_values(*numtuple)
