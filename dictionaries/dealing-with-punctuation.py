import string
fname=input("Please enter the name of the file you want me to open: ")
try:
    fhand=open(fname)
except:
    print("The file you entered does not exist")
    exit()
words=list()
for t in fhand:
    t=t.rstrip()
    t = t.translate(t.maketrans('', '', string.punctuation))
    t=t.lower()
    words.extend(t.split())
count=dict()
for word in words:
    if word not in count:
        count[word]=1
    else:
        count[word]+=1

print(count)




