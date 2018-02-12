# Write a program that when presented with any text file, determines the top 10 most used words
import string
fname=input("Please enter the file name you wish to get the most frequent words: ")
try:
    fhand=open(fname)
except:
    print("The file name you entered does not exist. The program is exiting now...")
    exit()
my_dict=dict()
for line in fhand:
    line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in my_dict:
            my_dict[word]=1
        else:
            my_dict[word]=my_dict[word]+1
#print(my_dict)
my_list1=list(my_dict.items())
my_list2=list()
for key,vals in my_list1:
    my_list2.append((vals,key))

my_list2.sort(reverse=True)
print(my_list2[:10])

#I cannot believe this actually worked, awesome stuff, I cannot even begin to imagine how to implement
#such a program in C or C++