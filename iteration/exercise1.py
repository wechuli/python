
# Exercise 1: Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
count=0
sums=0.0
while True:
    
    a=input("Please enter a number or input'done' if you are through entering the numbers: ")
    if a == "done":
        break
   
    else:
        try:
            a=float(a)
            count=count+1
            sums=sums+a
        except:
            print("Invalid input, I thought we agreed you would enter a number not anything else")
try:
    aver=sums/count
except:
    print("Seems like you entered one number and it was a '0', thats bad, really bad")

aver=sums/count

if count >0 and count <=1:
    print("You entered",count,"number")
else:
    print("You entered",count,"numbers")
print("Their sum is",sums)
print("Their average is",aver)


    
        
    
