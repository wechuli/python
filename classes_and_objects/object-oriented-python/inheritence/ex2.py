class Character:
    def __init__(self, name, hp, level):
        self._name = name
        self._hp = hp
        self._level = level

    def __repr__(self):
        return f'name: {self._name}, health: {self._hp}, level:{self._level}'


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print(f'This is just an NPC character, moving on')


my_character = NPC("Bob", 100, 12)
print(my_character)
my_character.speak()
