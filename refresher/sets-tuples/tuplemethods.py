months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
    print(month)

for i in range(len(months)):
    print(months[i])


# Tuple methods - Couunt how many times a value appears in a tuple

count = months.count('January')
print(count)


# index - return the index of the passed value

index = months.index('August')
print(index)

# We can nest tuples and we can have tuple slices