# Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words and charcters in the file


def statistics(file_name):
    stats = {
        "lines": 0,
        "words": 0,
        "characters": 0
    }
    with open(file_name, "r", encoding="utf8") as file:
        for i, l in enumerate(file):
            stats["lines"] += 1
            # count the number of words
            no_of_words = len(l.rsplit(" "))
            stats["words"] += no_of_words
            # count the characters
            no_of_chars = len(l)
            stats["characters"] += no_of_chars

    return stats


print(statistics("poem.txt"))
print(statistics('test.txt'))
print(statistics('story.txt'))
