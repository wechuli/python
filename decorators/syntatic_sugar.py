def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day")
    return wrapper


@be_polite
def greet():
    print("My name is Gollum")
# we don't need to set
#  greet = be_polite(greet)

# applying it to another
@be_polite
def rage():
    print("I am unhappy")


greet()
rage()
