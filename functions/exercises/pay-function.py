#write a program that accepts the number of hours worked, the rate, and computes
#the wages, if hours is above forty, multiply 1.5 times the wages got
#use try and accept to print an error if string instead of a number is input

error="Please enter a numerical value for both the pay and the rate per hour"
hours=input("Please enter the number of hours you worked")
rate=input("Please enter the rate of pay per hour")


try:
    hours=float(hours)
    rate=float(rate)

except:
    print(error)
def wage(a,b):
    if a <= 40 and a >= 0 and b>=0:
        pay= a*b
        print("You should receive a pay of",pay,"Kshs")
    
    elif a > 40 and b>=0:
        pay=(40*b)+(a-40)*b*1.5
        print("You should receive a pay of",pay,"Kshs")
        
    elif a<0 or b<0:
        print("Please enter a positive number for both rate and pay")
    
try:
    wage(hours,rate)
except:
    pass



