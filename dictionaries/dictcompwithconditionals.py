num_list = [1, 2, 3, 4]

geteven = {
    num: ('even' if num % 2 == 0 else "odd") for num in num_list
}

print(geteven)


class Person:
    def funcname(self, parameter_list):
        pass
    def funcname(self, parameter_list):
        raise NotImplementedError