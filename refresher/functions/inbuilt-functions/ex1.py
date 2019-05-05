
def is_all_strings(array):

    return all([False for item in array if type(item) != str])


print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2, 'a', 'b', 'c']))
print(is_all_strings(['hello', 'goodbye']))
