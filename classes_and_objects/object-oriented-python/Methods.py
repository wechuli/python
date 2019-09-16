

class User:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    def full_name(self):
        return f'{self._first} {self._last}'

    def initals(self):
        return f'{self._first[0]}.{self._last[0]}'

    def likes(self, thing):
        return f"Blah blah, useless method, {self._first} likes {thing}"

    def is_senior(self):
        return self._age > 65

    def birthday(self):
        self._age += 1
        return f'Happy {self._age}th birthday, {self._first}'


basic_user = User('Joe', 'Black', 85)
basic_user2 = User('Jane', 'Doe', 29)

print(basic_user.full_name())
print(basic_user2.full_name())

print(basic_user.initals())
print(basic_user2.likes('Music'))
print(basic_user.is_senior())
print(basic_user2.is_senior())
print(basic_user.birthday())
print(basic_user2.birthday())
