class GrumpyDict(dict):
    # we do not need to define an init,the init in dict will be used
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You wany, {key}, it ain't here")

    def __setitem__(self, key, value):
        print("You want to change the dictionary")
        print('ok, fine')
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No it aint here")
        return False


data = GrumpyDict(first="Tom", animal="cat")
print(data)
data['city'] = "Tokyo"
print(data)
