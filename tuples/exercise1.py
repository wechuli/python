# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname=input("Please provide the file name: ")
try:
    fhandle=open(fname)
except :
    print("The file you entered does not exist in this folder, the program is exiting now.....")
    exit()
my_dict=dict()
my_list=list()
for line in fhandle:
    line=line.strip()
    if line.startswith("From: "):
        words=line.split()
        my_list.append(words[1])
    else:
        continue

for word in my_list:
    if word not in my_dict:
        my_dict[word]=1
    else:
        my_dict[word]=my_dict[word]+1
    

my_list2=my_dict.items()
#print(my_list2)
my_list3=list()
for key,val in my_list2:
    my_list3.append((val,key))
my_list3.sort(reverse=True)
print(max(my_list3))

# that was an ordeal, am sure there is a shorter code to do this, but this is the best I can come up with at the
# moment, maybe I'll check it later and try something else.
