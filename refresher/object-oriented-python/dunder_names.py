

class Person:
    def __init__(self, name, age):  # special methods that python uses
        self._name = name  # _ is used to indicate private data members, there is nothing preventing you from skipping that convention
        self._age = age
        # __(double underscore), this is called name mangling, if we put two underscores before  a data member, Python will mange the name
        self.__message = "I like tutles" # this will be mangles to _Person__message


p = Person('Paul', 26)


print(dir(Person))
print(dir(p))
print(p._Person__message)
