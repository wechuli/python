# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259

import re
fname=input(r"Please enter the name of the file you want opened: ")
try:
    fhandle=open(fname)
except:
    print("Invalid file name. The program is exiting...")
    exit()
mylist=list()
for line in fhandle:
    line=line.rstrip()
    x=re.findall("New Revision: ([0-9]+)",line)
    if len(x)>0:
        mylist.extend(x)
mylist2=list()
for items in mylist:
    items=float(items)
    mylist2.append(items)
    
print(sum(mylist2)/len(mylist2))


