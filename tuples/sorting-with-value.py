my_nary={'The':'Heart','is':"exceedingly",'deceitful':'and','wicked':'above','all':'things'}
my_nary2={'The':5,'is':85,'deceitful':2,'wicked':-8,'all':22,'things':85}
my_list=list(my_nary2.items())
my_lis2=list()
for key,vals in my_list:
    my_lis2.append((vals,key))

my_lis2.sort(reverse=True)
print(my_lis2)
