

def frequency(array, search_term):
    fr = 0
    for term in array:
        if term == search_term:
            fr += 1
    return fr


print(frequency([1, 2, 3, 4, 4, 4], 4))
print(frequency([True, False, True, True], False))
