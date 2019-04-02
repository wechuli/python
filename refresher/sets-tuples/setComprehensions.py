
mysetcomp = {x**2 for x in range(10)}
print(mysetcomp)

myupper = {char.upper() for char in 'hello world'}
print(myupper)


def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5


myvalue = are_all_vowels_in_string('This will obviously return a True')
myvalue2 = are_all_vowels_in_string('Must be false')
print(myvalue)
print(myvalue2)
