

try:
    num = int(input("Please enter a number: "))
except Exception as error:
    print(error)
else:  # else code block will run if there is no exception
    print("Hurray, I passed without an exception")
finally:  # finally will run no matter what
    print("I am going to run no matter what happens")
