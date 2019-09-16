import sqlite3

conn = sqlite3.connect(r".\data\myfriends.sqlite")
cur = conn.cursor()


# UNSAFE WAY TO ADD DATA
# form_first = "Dana"
# insert_query = f"insert into friends(first_name) values ('{form_first}')"


# ANOTHER WAY TO DO INSERT
form_first = "Mary-Todd"
form_second = "Smith"
insert_query = f"insert into friends(first_name,last_name) values(?,?)"
cur.execute(insert_query, (form_first, form_second))

# INSERTING_ REALISTIC
form_data = ("Steve", "Irwin", 9)
real_query = f"insert into friends values(?,?,?)"
cur.execute(real_query, form_data)


conn.commit()
conn.close()
