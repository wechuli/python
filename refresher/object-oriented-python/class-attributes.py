# We can also define attributes directyl on a class that are shared by all instances of a class and the class itself
class User:
    active_users = 0  # this is a class attribute

    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1 # we can change the class attributes
    
    def logout(self):
        User.active_users -= 1
        return f'{self._first} has logged out'


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

print(User.active_users)
basic_user = User('Joe', 'Black', 85)
basic_user2 = User('Jane', 'Doe', 29)
print(User.active_users)
basic_user.logout()
print(User.active_users)

