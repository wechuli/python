import pdb
import random

# The module pdb defines an interactive source code debugger for Python programs. It supports setting(conditional) breakpoints and single stepping at the source level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame

first = "First"
second = "Second"
result = first + second

pdb.set_trace() 

third = "Third"
result += third
print(result)


def add_numbers(a,c)

# Common PDB Commands
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
# if you have conflicting names with the pydb commands use p {variable name} to show the value
