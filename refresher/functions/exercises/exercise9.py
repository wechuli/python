

def multiple_letter_count(mystring):
    if type(mystring) == str:
        mystring = mystring.lower()
        return {letter: mystring.count(letter) for letter in mystring}

    else:
        return 'Incorrect Data types entered'


print(multiple_letter_count('This is another fake random string'))
print(multiple_letter_count('Python is super easy to use'))
