# __name__


# When run, every Python file has a __name__ variable
# If the file is the main file being run, its value is "__main__"
def say_another():
    print(f'Hi! my name is {__name__} from say another')


def say_hi():
    print(f'Hi! my name is {__name__} from hi')


if __name__ == '__main__': # will only execute if it is the current file being executed by the intepreter and not being called by some other module
    say_hi()
