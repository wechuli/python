
with open('test.txt', 'r+') as file:
    file.write("Just been added")

with open('test.txt', 'r+') as file:
    file.write(":)")
    file.seek(10)
    file.write(":(")
