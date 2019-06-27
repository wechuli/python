a_string = "This is a long string"

iterator = iter(a_string)
print(iterator.__next__())
print(iterator.__next__())
print(iterator)


# for letter in a_string:
#     print(letter)
# raise StopIteration()