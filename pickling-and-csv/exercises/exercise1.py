# Implement the following function
# add_user: Takes a first name and a laast name and adds a new user to the users.csv file
from csv import DictReader, DictWriter, writer, reader


def add_user(first_name, last_name, age, company):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name, age, company])


def add_user_dict(first_name, last_name, age, company):
    with open("users2.csv", "a+") as file:
        headers = ["firstname", "lastname", "age", "company"]
        csv_writer2 = DictWriter(file, fieldnames=headers)
        csv_writer2.writeheader()
        csv_writer2.writerow({
            "firstname": first_name,
            "lastname": last_name,
            "age": age,
            "company": company
        })


add_user("Mike", "Shitso", 32, "Equity Bank")
add_user_dict("Mike", "Shitso", 32, "Equity Bank")
