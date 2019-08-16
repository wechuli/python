import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sayHello(self):
        return f'{self.name} says hello'


my_cat = Cat("Charles", "Tabby")

frozen = jsonpickle.encode(my_cat)
print(frozen)

with open("cat.json", "w") as file:
    file.write(frozen)
