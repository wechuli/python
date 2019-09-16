import sqlite3

conn = sqlite3.connect(r".\data\myfriends.sqlite")

cur = conn.cursor()

insert_query = ''' insert into friends
values ('Mary','Lewis',71)'''

insert_mul_query = """
insert into friends(first_name, last_name, closeness)
values ('Valary','Achieng',8),
       ('Jess','Mbugua',5),
       ('Norman','Barras',10);
"""


cur.execute(insert_query)
cur.execute(insert_mul_query)

# commit changes
conn.commit()
conn.close()
