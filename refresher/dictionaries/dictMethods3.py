# update - update keys and values in a dictionary with another set of key value pairs, it will overwrite keys and value pairs that are already present but will preserve values unique to the first dictionary

first = dict(a=1, b=2, c=3, d=4)
second = dict()

second.update(first)
print(second)


instructor = {
    "name": "Paul",
    "age": 26,
    "hobbies": ["reading", "sleeping", "coding"],
    "phone": 701782846
}

person = {
    "city": "Nairobi"
}

person.update(instructor)
print(person)
