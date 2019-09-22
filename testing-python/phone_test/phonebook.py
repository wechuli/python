class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, name, phone):
        self.numbers[name] = phone

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name in self.numbers:
            for name2 in self.numbers:
                if name == name2:
                    continue
                if self.numbers[name].startswith(self.numbers[name2]):
                    return False
        return True

    def get_names(self):
        pass

    def get_numbers(self):
        pass
