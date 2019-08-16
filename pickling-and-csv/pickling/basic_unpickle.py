import pickle
from class_to_pickle import Cat


with open("pets.pickle", "rb") as file:
    unpickled = pickle.load(file)
    print(unpickled)
    unpickled.play()
