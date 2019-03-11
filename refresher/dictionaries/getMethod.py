girls = {
    "caroline": 6,
    "june": 10,
    "Jess": 8,
    "Maria": 8.5
}

print(girls['june'])
# print(girls['fakename'])# will throw an error but
print(girls.get("Maria"))
print(girls.get("Marial")) # will return null

print(type(girls.get("dosenotexist")))