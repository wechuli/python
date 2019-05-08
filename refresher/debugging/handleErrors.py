# In Python, it is strongly encouraged to use try/except blocks to catch exceptions when we can do something about them


# Use try catch to limit the number of errors you can actually get

try:
    foobar
except:
    print('Problem')


d = {"name": "Tricky"}
# d['city'] keyError


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, 'city'))
