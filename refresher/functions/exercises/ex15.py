

def compact(array):
    truthy = [item for item in array if item]
    return truthy


print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
