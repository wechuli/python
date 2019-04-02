# An ordered collection or grouping of items
# A tuple is immutable

numbers = (1, 2, 3, 4, 5, 5)

print(type(numbers))
print(numbers[2])


alphabet = ('a', 'b', 'c', 'd')

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
print(months[11])

# Tuples can be used as keys in dictionaries

locations = {
    (35.685, 39.6917): 'Tokyo Office',
    (40.7128, 740060): 'New York Office',
    (37.7749, 122.4194): 'San Francisco Office'
}  # you cannot use a list in a dictionary

print(locations[(35.685, 39.6917)])

# some dictionary methods will return tuples
cat = {
    "name": "Black",
    "age": 25,
    "date": False
}

print(cat.items())
