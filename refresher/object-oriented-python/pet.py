class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self._name = name
        self._species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
tiger = Pet("Wyo", "dd")
