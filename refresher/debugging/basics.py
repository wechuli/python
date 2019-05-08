# Types of Errors in Python

# 1. SyntaxError - Occurs when Python encounters incorrect syntax. Usually due to typos e.g
# def trr:


# 2. NameError - occurs when a variable is not defined
# print(test)


# 3. TypeError - occurs when an operation or function is applied to the wrong type - Python cannot interpret an operation on two data types e.g
# len(5)
# 'awesome' + 5


# 4. IndexError - Occurs when you try to access an element in alist using an invalid index
# e.g
# [1,2][5]

# 5. ValueError - This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value
# e.g
# int('foo')

# 6. KeyError - This occurs when a dictionary does not have a specific key
# e.g
person = {
    "name": "Paul",
    "age": 26
}
print(person['name'])
# print(person['gender'])  #keyError

# 7.AttributeError - This occurs when a variable does not have an attribute
# e.g
['yes','no'].hello()
