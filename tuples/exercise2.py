# Exercise 2: This program counts the distribution of the hour of the day for each
# of the messages. You can pull the hour from the “From” line by finding the time
# string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.
# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


fname=input("Please provide the file name: ")
try:
    fhandle=open(fname)
except :
    print("The file you entered does not exist in this folder, the program is exiting now.....")
    exit()
my_list=list()
for line in fhandle:
    line=line.strip()
    if line.startswith("From"):
        words=line.split()
        if len(words)>4:
            my_list.append(words[5])
    else:
        continue
my_dict=dict()
mylist3=list()
mylist4=list()
for a in my_list:
    mylist3=a.split(':')
    mylist4.append(mylist3[0])

for sent in mylist4:
    if sent not in my_dict:
        my_dict[sent]=1
    else:
        my_dict[sent]+=1
mylist5=list(my_dict.items())
mylist5.sort()
for keys,value in mylist5:
    print(keys,value)
# Oh my goodness, that was very ineficient, even if we did get the job done, 40 or so lines
# of code for such a simple functionality is too big.