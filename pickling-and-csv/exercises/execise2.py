from csv import reader


with open('users3.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f'First Name: {row[0]}, Last Name: {row[1]}')
