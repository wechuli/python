class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self._eye_color = eye_color
        self._hair_color = hair_color
        self._hair_type = hair_type

    def __repr__(self):
        return f'Eye color: {self._eye_color} Hair Color: {self._hair_color} Hair Type: {self._hair_type}'


class Father:
    def __init__(self, eye_color="blue", hair_color="blonde", hair_type="straight"):
        self._eye_color = eye_color
        self._hair_color = hair_color
        self._hair_type = hair_type

    def __repr__(self):
        return f'Eye color: {self._eye_color} Hair Color: {self._hair_color} Hair Type: {self._hair_type}'


class Child(Mother, Father):
    pass


child = Child()
print(child)
