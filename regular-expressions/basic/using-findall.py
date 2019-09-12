import re
fname=input(r"Please enter a filename you want opened: ")
fhandle=open(fname)
all_file=fhandle.read()
# lst=re.findall('\S+@\S+',all_file)
# the square brackets are used to indicate the particular characters we want
# in this case, i only want numbers or letters at the end of the substring thus
lst=re.findall('[a-zA-Z1-9]\S+@\S+[a-zA-Z]',all_file)
print(lst)