# using a list
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums


# using a generator

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1
