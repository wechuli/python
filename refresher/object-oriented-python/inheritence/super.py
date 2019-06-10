class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def __repr__(self):
        return f'{self._name} is a {self._species}'

    def make_sound(self, sound):
        print(f'This animal says {sound}')


class Cat(Animal):

    def __init__(self, name, breed, toy, species="Cat"):
        super().__init__(name, species)
        self._breed = breed
        self._toy = toy


cat1 = Cat('Rex', 'German', "Bathtub", 'Cat')


print(cat1)
