import sqlite3
conn = sqlite3.connect(r".\data\myfriends.sqlite")

# create cursor object

cur = conn.cursor()

cur.execute("SELECT * from friends")
for result in cur:
    print(result)

cur.execute("SELECT first_name from friends")
print(cur.fetchall())

cur.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness DESC")
for result in cur:
    print(result)


conn.commit()
conn.close()
