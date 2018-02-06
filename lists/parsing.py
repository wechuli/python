# What if we wanted to print
# out the day of the week from those lines that start with “From”?
# From stephen.marquard@uct.ac.zaSat Jan 5 09:14:16 2008

fhand=open(r"D:\Study\Python\python-codes\files\mbox-short.txt")
for line in fhand :
    line.rstrip
    if line.startswith("From ") is True:
        words=line.split()
        print(words[2])
        
