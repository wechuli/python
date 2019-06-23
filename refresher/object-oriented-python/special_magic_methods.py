# In Python, special methods are a set of predefined methods you can use to encrich your classes. They are easy to recognize because they start and end with double underscores.
from copy import copy


class Human:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    def __repr__(self):
        return f'Human names {self._first} {self._last}'

    def __len__(self):
        return self._age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self._last, age=0)
        raise TypeError("Invalid Type")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError('Invalid Type')


jenny = Human("Jenny", "Simpson", 31)
kevin = Human("Kevin", "Larson", 32)
print(jenny)
print(len(jenny))
print(jenny+kevin)
# note that these objects are not copied, a reference is created for each object
print(jenny*2)

# if we want to copy different objects, we need the copy method from the copy built in module

mutliplecopies = kevin * 4
# Lets change one of the copies
mutliplecopies[3]._first = "Changed Name"
print(mutliplecopies)

#
triplets = (jenny+kevin) * 3
print(triplets)
