# variables created in functions are scoped in that function

instructor = 'Paul'


def say_hello():
    return f'Hello {instructor}'


print(say_hello())


def say_hello2():
    instructor2 = 'Paul'  # instructor variable is scoped to the say_hello2() function
    return f'Hello {instructor2}'


print(say_hello2())
