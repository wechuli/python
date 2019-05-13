import custom  # we can import our module into the new file
from anothercustom import Customer, Girl


june = Customer('June Baby', 200000)
mercy = Customer('Mercy Cher', 2500)


print(june.get_customer())
print(mercy.get_customer())


mary = Girl('August', 56000)
print(mary.private_method())
print(mary.get_customer())

custom.fn()
custom.anotherOne()
