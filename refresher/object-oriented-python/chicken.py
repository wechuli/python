class Chicken:
    total_eggs = 0

    def __init__(self, name, species, eggs=0):
        self._name = name
        self._species = species
        self._eggs = eggs

    def lay_egg(self):
        self._eggs += 1
        Chicken.total_eggs += 1
        return self._eggs

    def stats(self):
        return {"total": Chicken.total_eggs, "this_chicken": self._eggs}


c1 = Chicken("Alice", "Hen")
c1.lay_egg()
c1.lay_egg()
c1.lay_egg()
print(c1.stats())

c2 = Chicken("Alice2", "Hen")
c2.lay_egg()
print(c2.stats())
