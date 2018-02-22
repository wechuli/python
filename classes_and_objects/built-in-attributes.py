class Employee:
    empcount=0
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.empcount += 1
    def displaycount(self):
        print("Total Employee %d" % Employee.empcount)
    def displayemployee(self):
        print("Name",self.name,"Salary:",self.salary)
# lets now try to see the built in attributes

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)




    