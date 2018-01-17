#write a program that accepts the number of hours worked, the rate, and computes
#the wages, if hours is above forty, multiply 1.5 times the wages got
#use try and accept to print an error if string instead of a number is input

error="You should enter numeric values for both hours worked and rate, where did you go to school?"
hours_w=input("Please enter the number of hours you worked: ")
rate=input("Please enter the rate per hour: ")
try:
    hours_w=float(hours_w)
    rate=float(rate)
    if hours_w > 40:
        wages = (40*rate)+((hours_w-40)*rate*1.5)
        print("You should receive",wages,"Ksh as your wages")
    elif hours_w <= 40 and hours_w > 0 and rate > 0:
        wages = (rate*hours_w)
        print("You should receive",wages,"Ksh as your wages")
    else:
        print("Seems like you entered negative values for hours worked and/or rate per hour, acha jokes")
except:
    print(error)