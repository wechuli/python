import math
pi=22/7
radius=input("Please enter the radius of your circle: ")
try:
    radius=float(radius)
    if radius<0:
        print(radius,"Is a negative value, We cannot have a negative radius, dah!")
    else:
        area=pi*radius**2
        print("The area of your circle is",area,"cm squared")
        print("The logarithmic value is", math.log10(area))
except:
    print("Since when did the radius of a circle be in strings")
