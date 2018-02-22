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
# lets now create an object of the class employee

emp1=Employee("Philip",34000)
emp2=Employee("Jane",90000)

emp1.displaycount()

emp2.displayemployee()



    