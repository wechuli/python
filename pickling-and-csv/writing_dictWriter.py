from csv import DictReader, DictWriter

with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Blue",
        "Breed": "Orange Tuby",
        "Age": 10
    })
    csv_writer.writerow({
        "Name": "Brian",
        "Age": 220,
        "Breed": "No Idea"
    })
