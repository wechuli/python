
# when the varible is not defined in the global scope but still defined in another scope, we need to use nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner



print(outer()())