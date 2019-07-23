# Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replace all instances of the word in the file with the replacement word.


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, encoding="utf8") as file:
        whole_file = file.read()
    with open(file_name, "w", encoding="utf8") as file_to_write:
        whole_file = whole_file.replace(old_word, new_word)
        print(whole_file)
        file_to_write.write(whole_file)


find_and_replace("test.txt", "work", "work-changed")
