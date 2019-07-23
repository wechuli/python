# Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replace all instances of the word in the file with the replacement word.


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
