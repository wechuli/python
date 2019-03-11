d = dict(a=1, b=2, c=3)
print(d)
d.clear()  # removes all the values and keys
print(d)

original = dict(name="Wechuli", age=25, istall=True)
copy = original.copy()
print(copy)
print(original is copy) #copies the contents but is not the same object
