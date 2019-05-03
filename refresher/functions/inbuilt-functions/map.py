# a standard function that accepts accepts at least two arguments, a function and an iterable
# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure


myvalues = [1, 2, 3, 4, 5, 6]
print(myvalues)

mynewvalues = map(lambda value: value * 2, myvalues) # we don't need a lambda function, but is shorter


print(list(mynewvalues))
print(mynewvalues)
