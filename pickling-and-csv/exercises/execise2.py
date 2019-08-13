from csv import reader


with open('users.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(row)
