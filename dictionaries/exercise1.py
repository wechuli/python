#
#  Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname=input("Please enter a file name: ")
try:
    fhand=open(fname)
except :
    print("The file you entered does not exist")
    exit()
word=list()
words=list()
for line in fhand:
    if line.startswith("From"):
        line=line.rstrip()
        word=line.split()
        if len(word)>3:
            words.append(word[2])
        else:
            continue    
    else:
        continue
# print(words)
mycount=dict()
for a in words:
    if a not in mycount:
        mycount[a]=1
    else:
        mycount[a]+=1
    
print(mycount)

     