import sqlite3 as sql

conn = sql.Connection("data.db")
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS users (ism TEXT, username TEXT, rasm BLOB) """)
# c.execute("""INSERT INTO users VALUES ("Odilbek", "Xudaybergenov", "img.jpg") """)

c.execute("""CREATE TABLE IF NOT EXISTS users (ism TEXT, job TEXT) """)

# c.execute("""INSERT INTO users VALUES ("Ali", "O'qituvchi")""")
# c.execute("""INSERT INTO users VALUES ("Vali", "O'qituvchi")""")
# c.execute("""INSERT INTO users VALUES ("Anvar", "O'qituvchi")""")
# c.execute("""INSERT INTO users VALUES ("Aziz", "Direktor")""")
# c.execute("""INSERT INTO users VALUES ("Asadbek", "O'qituvchi")""") 
# c.execute("""INSERT INTO users VALUES ("Olim", "Direktor")""")

# data = c.execute("""SELECT * FROM users """).fetchall()
# print(data)

# c.execute("""SELECT * FROM users """)
# print(c.fetchall()[0][0])

# c.execute("""SELECT * FROM users WHERE job="O'qituvchi" """)

# c.execute("""SELECT * FROM users WHERE ism="Vali" """)
# print(c.fetchone())
# print(c.fetchall())

# c.execute("""SELECT * FROM users """)
# print(c.fetchmany(5))


conn.commit()
conn.close()