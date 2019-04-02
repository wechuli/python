myset = set([1,2,3])

#add value
myset.add(4)

print(myset)


#remove value - will throw an error if item is not present
myset.remove(1)
print(myset)

#discard will not throw an error
myset.discard('rt')
print(myset)

#copy
mysetCopy = myset.copy()
print(mysetCopy)


