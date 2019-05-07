# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionaries conactenated

names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]


def extract_full_name(names):
    return list(map(lambda x: ' '.join((x['first'], x['last'])), names))


print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
