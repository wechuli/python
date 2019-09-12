import re
fname=input(r"Please enter the name of the file you want opened: ")
try:
    fhand=open(fname)
except:
    print("The file you entered does not exist")
    exit()
for line in fhand:
    line=line.rstrip()
    # If we want to extract only a part of the searched string we use a parantheses () 
    # to delimit what we want 
    # extracted
    # if re.findall("X-\S*: [0-9.]+",line):
    if re.findall("X-\S*: [0-9.]+",line):
        print(line)
