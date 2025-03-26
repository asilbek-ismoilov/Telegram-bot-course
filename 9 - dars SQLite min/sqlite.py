# import sqlite3 as sql

# con = sql.connect("data.db")
# c = con.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS computers_info (name TEXT, photo TEXT, price TEXT, color TEXT) """)

# computers = [
#     ("Mackbook", "https://cdn.mos.cms.futurecdn.net/oN65txxVKUr76CF478iPmT.jpg", "2000", "Silver"),
#     ("Lenovo", "https://www.superplanshet.ru/images/Lenovo_Legion_Pro_7-1.jpg", "1200", "Black"),
#     ("HP", "https://i.ytimg.com/vi/_zs8bvPlpx0/maxresdefault.jpg", "1400", "Green")
# ]

# c.executemany("INSERT INTO computers_info (name, photo, price, color) VALUES (?, ?, ?, ?)", computers)

# def get_computers(name):
#     c.execute("SELECT * FROM computers_info WHERE name = ?", (name,))
#     all_users = c.fetchall()
#     return all_users


# con.commit()
# con.close()


import sqlite3 as sql

def create_db():
    con = sql.connect("data.db")
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS computers_info 
                (name TEXT, photo TEXT, price TEXT, color TEXT)""")

    # Dublikatni oldini olish
    c.execute("SELECT COUNT(*) FROM computers_info")
    if c.fetchone()[0] == 0:
        computers = [
            ("MacBook", "https://cdn.mos.cms.futurecdn.net/oN65txxVKUr76CF478iPmT.jpg", "2000", "Silver"),
            ("Lenovo", "https://www.superplanshet.ru/images/Lenovo_Legion_Pro_7-1.jpg", "1200", "Black"),
            ("HP", "https://i.ytimg.com/vi/_zs8bvPlpx0/maxresdefault.jpg", "1400", "Green"),
            ("ASUS","https://mobile-review.com/articles/2021/image/asus-zenbook-duo14-ux482e/pic/16.jpg", 1300, "Blue")
        ]
        c.executemany("INSERT INTO computers_info (name, photo, price, color) VALUES (?, ?, ?, ?)", computers)

    con.commit()
    con.close()

def get_computers(name):
    con = sql.connect("data.db")
    c = con.cursor()
    c.execute("SELECT * FROM computers_info WHERE name = ?", (name,))
    computers = c.fetchall()
    con.close()
    return computers

def get_all_computers_names():
    con = sql.connect("data.db")
    c = con.cursor()
    c.execute("SELECT name FROM computers_info")
    result = [row[0] for row in c.fetchall()]  
    con.close()
    return result
    
def update_computer(name, photo, price, color): 
    con = sql.connect("data.db")
    c = con.cursor()
    c.execute("UPDATE computers_info SET photo = ?, price = ?, color = ? WHERE name = ?", (photo, price, color, name))
    con.commit()
    con.close()

create_db()
