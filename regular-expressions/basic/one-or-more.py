import re
fname=input(r"Please enter the name of the file to be opened: ")
fhnadle=open(fname)
for line in fhnadle:
    line=line.rstrip()
    if re.search('F.+@',line):
        print(line)
