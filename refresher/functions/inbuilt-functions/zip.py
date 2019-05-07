# Zip
# Make an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples , where the i-th tuple contains the i-th element from each of the argument sequences or iterables
# The iterator stops when the shortest input iterable is exhausted

first_zip = zip([1, 2, 3], [4, 5, 9])

print(list(first_zip))
print(dict(first_zip))  # we can turn it into a dictionary


mynumbers = [(1, 2), (2, 3), (3, 4), (4, 5)]


print(list(zip(*mynumbers)))