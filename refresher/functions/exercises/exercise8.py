
def single_letter_count(mystring, letter):
    if type(mystring) == str and type(letter) == str:
        mystring = mystring.lower()
        letter = letter.lower()
        return mystring.count(letter)

    else:
        return 'Incorrect Data types entered'


print(single_letter_count('This is my super fake string', 'z'))
