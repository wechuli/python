#Exercise 1: Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on
#a separate line, except backwards.

mystring="Oh dear girl"

a=len(mystring)-1

while a > -1:
    print(mystring[a])
    a=a-1
