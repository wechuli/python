# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section [maximumloop]) to find who
# has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

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
            words.append(word[1])
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
a=max(mycount)
print(a,mycount[a])