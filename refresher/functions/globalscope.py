total = 0

# def increment():  #this will result in an error since we are referencing the global variable
#     total += 1
#     return total


def increment():  
    global total #referencing a global variable inside a function to enable modifying it
    total += 1
    return total

name = 'wechuli'

def printname():
    print(name) #interestingly, if we are just referencing the variable without changing it, there is no error


increment()
print(total)
printname()