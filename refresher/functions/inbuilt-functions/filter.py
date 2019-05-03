# returns an oobject that contains obly values that return true to the lambda

l = [1, 2, 3, 4, 5, 6, 7]

evens = list(filter(lambda number: number % 2 == 0, l))
print(evens)
