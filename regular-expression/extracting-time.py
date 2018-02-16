import re
fname=input(r"Please enter the name of the file you want opened: ")
try:
    fhand=open(fname)
except:
    print("The file you entered does not exist")
    exit()
for line in fhand:
    line=line.rstrip()
    x=re.findall("^From.* ([0-9][0-9]):",line)
    if len(x)>0:
        print(x)
