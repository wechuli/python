# Implement the following function
# add_user: Takes a first name and a laast name and adds a new user to the users.csv file
from csv import DictReader, DictWriter, writer, reader


def add_user(first_name, last_name, age, company):
    with open('users.csv', 'a+') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name, age, company])




add_user("Mike", "Shitso", 32, "Equity Bank")
