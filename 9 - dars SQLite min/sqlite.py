import sqlite3 as sql

con = sql.connect("data.db")
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS computers_info (name TEXT, photo TEXT, price TEXT, color TEXT) """)

c.execute("""INSERT INTO computers_info VALUES ("Mackbook", "https://cdn.mos.cms.futurecdn.net/oN65txxVKUr76CF478iPmT.jpg", "2000", "Silver") """)

# computers = [
#     ("Mackbook", "https://cdn.mos.cms.futurecdn.net/oN65txxVKUr76CF478iPmT.jpg", "2000", "Silver"),
# ]

# c.executemany("INSERT INTO computers_info (name, photo, price, color) VALUES (?, ?, ?, ?)", computers)

con.commit()
con.close()

print("\nIsh yakunlandi!")
