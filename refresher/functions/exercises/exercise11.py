import string


def is_palindrome(word):
    original = list()
    # trsanslating a string
    translator = str.maketrans('', '', string.punctuation)

    word = word.lower()
    word = word.translate(translator)
    for letter in word:
        if letter == ' ':
            continue
        original.append(letter)

    reversed_word = original.copy()
    reversed_word.reverse()

    return reversed_word == original


print(is_palindrome('testing'))
print(is_palindrome('taco cat?'))
print(is_palindrome('hannah!'))
print(is_palindrome('robert'))
print(is_palindrome('amanaplanacanalpanama'))
