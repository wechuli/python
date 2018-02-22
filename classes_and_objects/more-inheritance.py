#!/usr/bin/python

class nothing:
    x=45
    def __init__(self, name):
        print("My name is",self.name)
    

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


#determining if a class is a subclass of another
print(issubclass(Child,Parent))
#determining if an instance belongs to a particular class
print(isinstance(c,Child))
#what if it is false
print(isinstance(c,nothing))
