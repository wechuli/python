# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
# 8.16. EXERCISES 107
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

mylist=[]
while True:
    values=input("Please enter a value for me to add to the list, type done to finish:")
    if values=='done' or 'd':
        break
    try:
        values=float(values)
        mylist.append(values)
    except:
        print("There value you entered is not a number, to exit, enter done")
               
  

print(mylist)

    