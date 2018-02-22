# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def __init__(self,nam,colo,valu):
        self.name=nam
        self.color=colo
        self.value=valu
        print("I have been created")
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle("Fer","Red",60000)
car2=Vehicle("Jump","Blue",10000)

# test code
print(car1.description())
print(car2.description())

#please also note that you can create attributes for the class as below
# car1 = Vehicle()
# car1.name = "Fer"
# car1.color = "red"
# car1.kind = "convertible"
# car1.value = 60000.00

# car2 = Vehicle()
# car2.name = "Jump"
# car2.color = "blue"
# car2.kind = "van"
# car2.value = 10000.00

# print(car1.description())
# print(car2.description())