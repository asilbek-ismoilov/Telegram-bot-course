import sqlite3 as sql

# Bazaga ulanish yoki yangi baza yaratish
con = sql.connect("data.db")
c = con.cursor()

# # Jadval yaratish ❗️ :

# c.execute("""CREATE TABLE IF NOT EXISTS users (ism TEXT, username TEXT, rasm BLOB) """)


# c.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Avtomatik ID qo'shiladi
#     ism TEXT NOT NULL,                      -- Foydalanuvchi ismi
#     job TEXT NOT NULL,                      -- Kasbi
#     age INTEGER,                            -- Yoshi
#     salary REAL                               
# )
# """)

# print("Jadval yaratildi!")

# # Ma'lumot qo'shish ❗️ : 

# c.execute("""INSERT INTO users VALUES ("Ali", "Valiyev", "img.jpg") """)


# users = [
#     ("Ali", "O'qituvchi", 35, 5000.50),
#     ("Vali", "Muhandis", 29, 7000.00),
#     ("Anvar", "Dasturchi", 25, 10000.75),
#     ("Aziz", "Direktor", 40, 15000.00),
#     ("Asadbek", "Dasturchi", 30, 12000.20)
# ]

# c.executemany("INSERT INTO users (ism, job, age, salary) VALUES (?, ?, ?, ?)", users)
# print("Ma'lumotlar qo'shildi!")

# # Ma'lumotlarni ko'rish ❗️:

# c.execute("SELECT * FROM users")
# all_users = c.fetchall()
# print("\nHamma foydalanuvchilar:")
# for user in all_users:
#     print(user)

# # Filtrlangan ma'lumotlar ❗️:

# c.execute("SELECT * FROM users WHERE job = 'Dasturchi'")
# developers = c.fetchall()
# print("\nDasturchilar:")
# for dev in developers:
#     print(dev)

# # Ma'lumotlarni tartiblash ❗️:

# c.execute("SELECT * FROM users ORDER BY salary DESC")
# sorted_users = c.fetchall()
# print("\nMaoshi bo'yicha tartiblangan foydalanuvchilar:")
# for user in sorted_users:
#     print(user)

# # Ma'lumotlarni yangilash ❗️:

# c.execute("""UPDATE users SET WHERE job = "O'qituvchi" """)
# print("\nO'qituvchilarning maoshi oshirildi!")

# # Ma'lumotlarni o'chirish ❗️:

# c.execute("DELETE FROM users WHERE name = ?", (name,))
# print("\nYoshi 35 dan katta foydalanuvchilar o'chirildi!")

# # O'zgartirilgan ma'lumotlarni ko'rish ❗️:

# c.execute("SELECT * FROM users")
# updated_users = c.fetchall()
# print("\nYangilangan foydalanuvchilar:")
# for user in updated_users:
#     print(user)

# # Jadvaldagi qatorlarni sanash ❗️:

# c.execute("SELECT COUNT(*) FROM users")
# row_count = c.fetchone()[0]
# print(f"\nJadvaldagi qatorlar soni: {row_count}")

# # Maxsus funksiyalar: MAX, MIN, AVG, SUM ❗️:

# c.execute("SELECT MAX(salary), MIN(salary), AVG(salary), SUM(salary) FROM users")
# max_salary, min_salary, avg_salary, sum_salary = c.fetchone()
# print(f"\nMaksimal maosh: {max_salary}")
# print(f"Minimal maosh: {min_salary}")
# print(f"O'rtacha maosh: {avg_salary}")
# print(f"Jami maosh: {sum_salary}")

# # BLOB ma'lumotlarni qo'llash (masalan, rasmlar) ❗️:
# # Faylni BLOB sifatida saqlash ❗️:

# with open("example_image.jpg", "rb") as file:
#     blob_data = file.read()
# c.execute("CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, filename TEXT, data BLOB)")
# c.execute("INSERT INTO files (filename, data) VALUES (?, ?)", ("example_image.jpg", blob_data))
# print("\nRasm fayli bazaga yuklandi!")

# # BLOB ma'lumotni qayta olish va saqlash ❗️:

# c.execute("SELECT data FROM files WHERE filename = 'example_image.jpg'")
# file_data = c.fetchone()[0]
# with open("retrieved_image.jpg", "wb") as file:
#     file.write(file_data)
# print("Rasm bazadan qayta saqlandi!")

# O'zgarishlarni saqlash va ulanishni yopish
con.commit()
con.close()

print("\nIsh yakunlandi!")
