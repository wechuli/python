class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f'There are currently {cls.active_users} active users'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1

    def __repr__(self):
        return f'{self._first} {self._last}'

    def logout(self):
        User.active_users -= 1
        return f'{self._first} has logged out'

    def full_name(self):
        return f'{self._first} {self._last}'

    def initials(self):
        return f'{self._first[0]}.{self._last[0]}'

    def likes(self, thing):
        return f"Blah blah, useless method, {self._first} likes {thing}"

    def is_senior(self):
        return self._age > 65

    def birthday(self):
        self._age += 1
        return f'Happy {self._age}th birthday, {self._first}'


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self._community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f'{self.full_name()} removed a post from the {self._community} community'

    def community(self):
        return self._community


jasmine = Moderator("Jasmine", "Oconnor", 29, "Piano")
jasmine2 = Moderator("Jasmine", "Oconnor", 29, "Piano")
jasmine3 = Moderator("Jasmine", "Oconnor", 29, "Piano")
print(jasmine)
print("Active users: ", User.active_users)
print("Active Moderators: ", Moderator.total_mods)
print(jasmine.community())

tom = User("Tom", "Doe", 20)
print(tom)
print("Active users: ", User.active_users)
