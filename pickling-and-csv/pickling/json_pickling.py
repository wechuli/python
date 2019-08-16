import json
from class_to_pickle import Cat

# dumps serislizes a python object to a json string object
json_data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

rex = Cat("Rex", "Kenyan Feline", "Lifundo")

rex_json = json.dumps(rex.__dict__)


print(json_data)
print(rex_json)
