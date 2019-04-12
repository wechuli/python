

def list_manipulation(mylist, command, location, value):
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
                return mylist.insert(-1, value)
            elif location == 'beginning':
                return mylist.insert(0, value)
            else:
                return 'Invalid location'

        else:
            return 'You need to provide a value'
    
