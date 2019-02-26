mygirls = ['Caro','June','Maria','Abigail','Jecinta','Mercy','Siggy']

#first parmaeter for slice:start

print(mygirls[1:])
print(mygirls[3:])
#we can slice from the end
print(mygirls[-3:])

#we can make a copy of the list -its not the same list though
print(mygirls is mygirls[:])


#the 2nd parameter is where to end the slice, doesnt include the last value

print(mygirls[:2])
print(mygirls[2:-1])

#the step count, the last parmater specifies how many values to skip
print(mygirls[1::2])

#we can have negative steps
print(mygirls[4:2:-1])


#modify specific portions
mygirls[0:2] = ['ChangeGirl','Girl']
print(mygirls)