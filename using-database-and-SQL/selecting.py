import sqlite3
conn = sqlite3.connect(r".\data\myfriends.sqlite")

# create cursor object

cur = conn.cursor()

cur.execute("SELECT * from friends")

cur.execute("SELECT first_name from friends")
print(cur.fetchall())



conn.commit()
conn.close()
