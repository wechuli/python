import sqlite3

conn = sqlite3.connect(r".\data\users.sqlite")
cur = conn.cursor()

username = input("Please enter your username: ")
password = input("Please enter your password: ")

query = f"SELECT * FROM users WHERE username=? AND password=?;"
cur.execute(query, (username, password))

result = cur.fetchone()
if result:
    print(f"Welcome back {username}")
else:
    print("Malicious user, I have caught you")

conn.commit()
conn.close()
