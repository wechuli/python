from csv import reader


with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) # getting ahead of the headers
    for row in csv_reader:
        # each row is a list
        print(row)
