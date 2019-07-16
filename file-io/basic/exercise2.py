# Exercise 2: Write a program to prompt for a file name, and then read through the
# file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519


# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program Modify the program that prompts
# the user for the file name so that it prints a funny message when the user types in
# the exact file name “na na boo boo”. The program should behave normally for all
# other files which exist and don’t exist

prompt=input("Please enter the file name: ")
try:
    fhand=open(prompt)
except:
    if prompt == 'na na boo boo':
        print(" NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("No such a file exists")
    exit()
count=0
sums=0
for line in fhand:
    if line.find('X-DSPAM-Confidence:') is not -1:
        #print(line)
        pos1=line.find(":")
        newstr=line[pos1+2:]
        newn=float(newstr)
        print(newn)
        count=count+1
        sums=sums+newn

mean=sums/count
print("The average span confidence is",mean)


    
