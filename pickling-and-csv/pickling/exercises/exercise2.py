from csv import reader, writer


def delete_users(first_name, last_name):
    with open('users.csv', 'r') as file:
        csv_reader = reader(file)
        file_contents_list = list(csv_reader)

    with open('users.csv', 'w', newline="") as file:
        csv_writer = writer(file)
        deleted_count = 0
        for row in file_contents_list:
            if(row):
                if(row[0] == first_name and row[1] == last_name):
                    deleted_count += 1
                else:
                    csv_writer.writerow(row)

    print(f'Users deleted: {deleted_count}')


delete_users("Paul", "Wechuli")
