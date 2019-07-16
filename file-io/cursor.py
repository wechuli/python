try:
    file = open('poem.txt')
except FileNotFoundError as fnf:
    print("The file was not found")
print(file.read(1))
file.seek(0)

print(file.readline())
print(file.readline())
