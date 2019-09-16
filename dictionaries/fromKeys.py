# creates a key-values pairs from comma separated values

empty = dict()

newUser = empty.fromkeys(["email", "email2"], "wechuliPaul") #the original user remains unchanged, the first value of the function is the iterable
print(newUser)

