from csv import reader


def find_user(first_name, last_name):
    with open('users3.csv') as file:
        csv_reader = reader(file)
        next(csv_reader)
        index = 1
        for row in csv_reader:
            if(row[0] == first_name and row[1] == last_name):
                return index
            index += 1
    return f"{first_name} {last_name} not found"


print(find_user("Paul", "Wechuli"))
print(find_user("June", "Nekesa"))
