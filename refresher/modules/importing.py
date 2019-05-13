# The from keyword lets you import parts of a module
# Haandy rule of thumb:only import what you need

# imports only the classes you need from the module
# Different ways to import
from random import choice, shuffle
from random import *  # imports everything
from random import choice as gimme_one, shuffle as mix_up_fruits
import random as omg_so_random
import random
from random import randint as ri


while True:
    print(ri(1, 456))


