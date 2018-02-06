mylist=[]
while True:
    values=input("Please enter a value for me to add to the list, type done to finish:")
    if values=='done':
        break
    try:
        values=float(values)
        mylist.append(values)
    except:
        print("There value you entered is not a number, to exit, enter done")
               
  

print(mylist)
print("The sum of your list is",sum(mylist))
print("The maximum number on your list is",max(mylist))
print("The minimum number on your list is",min(mylist))
print("The avergae value of your list is",sum(mylist)/len(mylist))


