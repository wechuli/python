nested_list = [[1, 2, 3, 4, 5], [4, 5, 6], [2, 3, 4, 5]]


for alist in nested_list:
    for anotherlist in alist:
        print(anotherlist)
    print(alist)

print(nested_list)

print(nested_list[0][2])
print(nested_list[2][0])

