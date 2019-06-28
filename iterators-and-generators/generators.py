def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


mygenerator = count_up_to(10)
print(type(mygenerator))
print(dir(mygenerator))

for i in mygenerator:
    print(i)


