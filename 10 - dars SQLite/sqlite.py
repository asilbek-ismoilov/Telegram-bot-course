# import sqlite3

# class Database:
#     def __init__(self, path_to_db="users.db"):
#         # Bazaga ulanish
#         self.connection = sqlite3.connect(path_to_db)
#         self.cursor = self.connection.cursor()

#     def execute(self, sql, parameters=None, commit=False):
#         if parameters is None:
#             parameters = ()
        # self.cursor.execute(sql, parameters)
        # if commit:
        #     self.connection.commit()

#     def create_table_users(self):
#         # Users jadvalini yaratamiz
#         sql = """
#         CREATE TABLE IF NOT EXISTS Users(
#             name TEXT,
#             surname TEXT,
#             age INTEGER,
#             tel TEXT,
#             kurs TEXT
#         );
#         """
#         self.execute(sql, commit=True)

#     def add_user(self, name: str, surname: str, age: int, tel: str, kurs: str):
#         # Foydalanuvchini jadvalga qo'shamiz
#         sql = """
#         INSERT INTO Users(name, surname, age, tel, kurs) VALUES(?, ?, ?, ?, ?);
#         """
#         self.execute(sql, parameters=(name, surname, age, tel, kurs), commit=True)

#     def close(self):
#         # Bazani yopamiz
#         self.connection.close()


import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

    def execute(self, sql, parameters=None, commit=False):
        if parameters is None:
            parameters = ()
        self.cursor.execute(sql, parameters)
        if commit:
            self.connection.commit()

    def create_table_users(self):
        # Users jadvalini yaratish
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            full_name TEXT,
            name TEXT,
            surname TEXT,
            age INTEGER,
            phone TEXT,
            course TEXT
        )
        """
        self.execute(sql, commit=True)

    def add_user(self, telegram_id, full_name, name, surname, age, phone, course):
        # Foydalanuvchini jadvalga qo'shish
        sql = """
        INSERT OR IGNORE INTO users (telegram_id, full_name, name, surname, age, phone, course)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(telegram_id, full_name, name, surname, age, phone, course), commit=True)

    def get_user_count(self):
        # Barcha foydalanuvchilarni sanaydi
        self.cursor.execute("SELECT COUNT(*) FROM users")
        count = self.cursor.fetchone()[0]
        return count
    
    def get_all_users(self):
        # Barcha foydalanuvchilarni olish (telegram_id va full_name)
        sql = "SELECT telegram_id, full_name FROM users"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def close(self):
        # Bazani yopamiz
        self.connection.close()
