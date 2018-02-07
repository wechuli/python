# Exercise 1:
# Write a function called chop that takes a list and modifies it, removing the first
# and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

mylist=['Data','SQL','Machine Learning','Python','AI','web','c#','hardware']
def chop(t):
    t.pop()
    del t[0]
    return None

chop(mylist)
print(mylist)

def middle(t):
    l=len(t)
    return t[1:l-1]

new=middle(mylist)
print(new)
print(mylist)