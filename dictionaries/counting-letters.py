my_string='It is rather a annoying to always be thinking of foolish things at the most serious times'
my_dict=dict()
for words in my_string:
    if words not in my_dict:
        my_dict[words]=1
    else:
        my_dict[words]=my_dict[words]+1

print(my_dict)