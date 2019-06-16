class Aquatic:
    def __init__(self, name):
        print("Aquatic Init")
        self._name = name

    def swim(self):
        return f'{self._name} is swimming'

    def greet(self):
        return f'I am {self._name} of the sea'


class Ambulatory:
    def __init__(self, name):
        print("Ambulatory Init")
        self._name = name

    def walk(self):
        return f'{self._name} is walking'

    def greet(self):
        return f'I am {self._name} of the land'


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin Init")
        super().__init__(name=name)
        # Ambulatory.__init__(self, name=name)
        # Aquatic.__init__(self, name=name)


# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
print(help(captain_cook))

# object
# print(captain_cook.swim())
# print(captain_cook.walk())
# print(captain_cook.greet())

# print(
#     f'Captain cook is instance of base Object: {isinstance(captain_cook,object)}')
# print(
#     f'Captain cook is instance of Penguin: {isinstance(captain_cook,Penguin)}')
# print(
#     f'Captain cook is instance of Aquatic: {isinstance(captain_cook,Aquatic)}')
# print(
#     f'Captain cook is instance of Ambulatory: {isinstance(captain_cook,Ambulatory)}')
