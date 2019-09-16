# Method Resolution Order(MRO)

# Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class which is the order in which Python will look for methods on instances of that class.

# You can programmatically reference the MRO in three ways:
# 1. the __mro__ attribute on the class
# 2. use the mro() method on the class
# 3. use the builtin help(cls) method