import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'{self.name}'

    def sayHello(self):
        return f'{self.name} says hello'


with open('cat.json', 'r') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)
