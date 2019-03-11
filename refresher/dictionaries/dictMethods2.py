instructor = {
    "name": "Paul",
    "age": 26,
    "hobbies": ["reading", "sleeping", "coding"],
    "phone": 701782846
}

# pop, must provide the key
print(instructor)
instructor.pop('phone')
print(instructor)
# if you pass a key that doesn't exist, it will throw an error
# instructor.pop("email")


# popitem will remove something at random

instructor.popitem()
print(instructor)
