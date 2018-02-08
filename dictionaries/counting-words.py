# One of the common uses of a dictionary is to count the occurrence of words in a
# file with some written text. Let’s start with a very simple file of words taken from
# the text of Romeo and Juliet.

fhand=open(r'D:\Study\Python\python-codes\lists\romeo.txt')
words=[]
for line in fhand:
    line.strip()
    words.extend(line.split())
# print(words)

my_dict=dict()
for n in words:
    my_dict[n]=my_dict.get(n,0)+1

print(my_dict)
    