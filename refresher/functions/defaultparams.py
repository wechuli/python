# Default parameters allow:
# allows you to become defensive
# avoids errors with incorrect parameters
# more readable examples


# Default params can be anything - Functions, lists,dictionaries,strings,booleans

def exponent(num, power=2):  # we have passed a default parameter
    return num ** power

print(exponent(2, 3))
print(exponent(3))
