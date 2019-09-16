# A Key feature of OOP is the ability to define a class which inherits from another class(a 'base' or 'parent' class)
# In Python, inheritence works by passing the parent class as an argument to the definition of a child class


class Animal:
    cool = True

    def make_sound(self, sound):
        print f'this animal says {sound}'


class Cat(Animal):
    pass
