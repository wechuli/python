my_chars='It is rather a annoying to always be thinking of foolish things at the most serious times'
mydoc=dict()
for c in my_chars:
    mydoc[c]= mydoc.get(c,0)+1

print(mydoc)
