# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.
import string
fname=input("Please enter the name of the file you want to open: ")
try:
    fhand=open(fname)
except:
    print("The file you entered does not exist, the program is exiting now.....")
    exit()
my_list=list()
for line in fhand:
    line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line=line.lower()
    words=line.split()
    my_list.extend(words)
my_list2=list()
for no in my_list:
    no=list(no)
    my_list2.extend(no)
my_dict=dict()
for num in my_list2:
    if num not in my_dict:
        my_dict[num]=1
    else:
        my_dict[num]+=1
mylist3=list(my_dict.items())
mylist4=list()
for keys,vals in mylist3:
    mylist4.append((vals,keys))
mylist4.sort(reverse=True)
# print(mylist4)
for valu,ke in mylist4:
    print(ke,valu)

