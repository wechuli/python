# Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file


def copy_and_reverse(file, newfile):
    with open(file, "r") as oldfile:
        old_file_contents = oldfile.read()
        old_file_contents = "".join(reversed(old_file_contents))
        with open(newfile, "w") as thenewfile:
            thenewfile.write(old_file_contents)


copy_and_reverse("poem.txt", "reversed_poem.txt")


# print("".join(reversed("this is reversed")))


print("".join(['d', 'f']))
