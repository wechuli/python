

print('hello'.__len__())


class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50


l1 = SpecialList([1, 2, 3, 4, 3, 4, 334])
l2 = SpecialList([44, 3, '4'])

print(len(l1))
print(len(l2))
