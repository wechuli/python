# sets are like formal mathematical sets. sets do not have duplicate values, elements in sets aren;t ordered, you
# you cannot access items in aset by index
# sets can be useful if you need to keep track of a collection of elements , but don't care about ordering, keys or values and duplicates

s = {1,2,3,4,5,4,4,4,1}
print(s)

set2 = set({2,3,4,2,'ssd'})
print(set2)

## we can test if an element is in a set

print('ssd' in set2)
print(85 in set2)

#looping

for number in set2:
    print(number)


# turning a list of duplicates to unique values
cities = ["Los Angeles","Nairobi","Mombasa","Nairobi","Nakuru","Kakamega","Kisumu","Los Angeles","Gilgil","Soy","Voi","Kwale","Naivasha"]

setcities = set(cities)
print(setcities)
print(list(setcities))
print(len(setcities))
