# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

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
    
print(mycount)
