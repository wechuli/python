import sqlite3

conn = sqlite3.connect(r".\data\myfriends.sqlite")
cur = conn.cursor()

people = [
    ("Ronale", "Amundes", 4),
    ("June", "Nafula", 9),
    ("Brian", "Otieno", 7),
    ("George", "Orion", 6),
    ("Seme", "Amos", 7),
    ("Diana", "Keiten", 5),
    ("Jecinta", "Nekesa", 10),
    ("Mercy", "Cherono", 8)

]

# bulk inserts
cur.executemany("insert into friends values(?,?,?)", people)

# using a for loop
for person in people:
    cur.execute("insert into friends values(?,?,?)", person)
    print("Inserting now!")


conn.commit()
conn.close()
