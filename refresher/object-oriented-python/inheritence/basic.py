class Human:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    def __repr__(self):
        return f'{self._first},{self._last},{self._age}'

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property  # getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f'{self._first} {self._last}'

    @full_name.setter
    def full_name(self, name):
        self._first, self._last = name.split(" ")


jane = Human("Jane", "Wanjiku", 25)
print(jane)
print(jane.age)
jane._age = 45
print(jane.age)
jane.age = 22
print(jane)
print(jane.full_name)
print(jane.__dict__)
