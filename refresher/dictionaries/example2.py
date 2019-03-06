cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True,
    "nestedP": {
        "propone": [12, 34, 2],
        "proptwo": "This is a fake property"
    }
}

print(cat)
print(cat['nestedP']["propone"][1])
dog = dict()

dog["name"] = "Sandack"
print(dog)
