# Write a function called copy, which takes in a file name and a new file name and copies the contents of the contaent of the first file to the second file

# open the existing file in read mode, read all contents, create the new file using write mode, copy all contents


def copy(file, newfile):
    # open the old file and read its contents
    with open(file, "r") as oldfile:
        oldfile_contents = oldfile.read()
        # create the new file and copy the contents into it
        with open(newfile, "w") as newfile:
            newfile.write(oldfile_contents)
    return True


copy("poem.txt", "after_the_funeral.txt")
