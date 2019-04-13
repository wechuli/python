def list_manipulation(mylist, command, location, value=None):
    if command == 'remove':
        if location == 'end':
            return mylist[0:-1]
        elif location == 'beginning':
            return mylist[1:]
        else:
            return 'Invalid location'
    elif command == 'add':
        if value:
            if location == 'end':
                mylist.append(value)  # remember that lists are mutable
                return mylist
            elif location == 'beginning':
                mylist.insert(0, value)
                return mylist
            else:
                return 'Invalid location'

        else:
            return 'You need to provide a value'
    else:
        return 'Invalid command'


print(list_manipulation([1, 2, 3], 'add', 'end', 45))
print(list_manipulation([1, 2, 3], 'add', 'beginning', 45))
print(list_manipulation([1, 2, 3], 'remove', 'end'))
print(list_manipulation([1, 2, 3], 'remove', 'beginning'))
