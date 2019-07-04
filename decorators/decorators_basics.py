

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day")
    return wrapper


def greet():
    print("My name is Gollum")


def hello():
    print("This is another")


greeting = be_polite(greet)
hello_greeting = be_polite(hello)

greeting()
hello_greeting()
