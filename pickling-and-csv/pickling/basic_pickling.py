import pickle
from class_to_pickle import Cat


blue = Cat("blue", "scottish fold", "string")


with open("pets.pickle","wb") as file:
    pickle.dump(blue,file)

