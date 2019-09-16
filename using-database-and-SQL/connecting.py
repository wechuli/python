import sqlite3

# connect to the db
conn = sqlite3.connect(r".\data\myfriends.sqlite")

# create cursor object
cur = conn.cursor()

# execute some sql
cur.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT,closeness INTEGER);")


conn.close()
