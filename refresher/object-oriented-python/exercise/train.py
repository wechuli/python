class Train:
    def __init__(self, num_cars):
        self._num_cars = num_cars

    def __repr__(self):
        return f'{self._num_cars} car train'

    def __len__(self):
        return self._num_cars

    def fakeMethod(self):
        pass


a_train = Train(4)
print(a_train)
print(len(a_train))
print(dir(Train))
print(dir(a_train))
