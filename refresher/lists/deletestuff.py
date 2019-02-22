mylist = [1,2,3,4]
mylist2 = [5,4,5,6,3]
mylist3 = ['june','betty','caro','maria','mercy','molly']

#clear method removes averything

print(f'Before operation {mylist}')
mylist.clear()
print(f'after operation {mylist}')

#pop removes the index passed in or the last item

print(f'Before operation {mylist2}')
last_item = mylist2.pop(2) #pop return the item deleted 
print(last_item)
print(f'after operation {mylist2}')

#remove -we provide a value to remove, remove the first item

print(f'Before operation {mylist3}')
mylist3.remove('caro')
print(f'after operation {mylist3}')