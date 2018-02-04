prompt=input("Please choose the file you would like me to open: ")
try:
    fhand=open(prompt)
except:
    print("The file you entered does not reside in this folder")
    exit()

search=input("Please enter the pattern you want me to search: ")

for line in fhand:
    line.rstrip()
    if line.find(search) is not -1 :
        print(line)


