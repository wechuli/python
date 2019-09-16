# Class methods are methods(with the @classmethod decorator) that are not concerned with instances, but the class itself


class User:
    active_users = 0  # this is a class attribute

    @classmethod
    def display_active_users(cls):  # this is a class method
        return f'There are currently {cls.active_users} active users'

    @classmethod
    def from_string(cls, data_str):  # using a class method to create an instance
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1  # we can change the class attributes

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


tom = User.from_string("Paul,Wechuli,25")


print(User.active_users)
print(User.display_active_users())
# print(tom.first)

# print(tom.initials())
basic_user = User('Joe', 'Black', 85)

# basic_user2 = User('Jane', 'Doe', 29)
# # print(User.active_users)
# # # basic_user.logout()
# # print(User.active_users)

# print(User.display_active_users())
# basic_user2 = User('Jennifer', 'Dame', 29)
# print(User.display_active_users())
