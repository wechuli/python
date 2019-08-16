from csv import reader, writer


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):

    with open('users.csv', 'r') as file:
        csv_file = reader(file)
        new_contents = []
        # get ahead of the headers
        new_contents.append(next(csv_file))

        change_count = 0

        for row in csv_file:
            if(row[0] == old_first_name and row[1] == old_last_name):
                change_count += 1
                new_contents.append([new_first_name, new_last_name])
            else:
                new_contents.append(row)

    with open('users.csv', 'w') as file:
        csv_writer = writer(file)
        for row in new_contents:
            csv_writer.writerow(row)

    print(f'User updated: {change_count}')


update_users("Paul", "Wechuli", "Paul-updated", "Wechuli-updated")
