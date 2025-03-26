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
        sql = """
        INSERT OR IGNORE INTO users (telegram_id, full_name, name, surname, age, phone, course)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(telegram_id, full_name, name, surname, age, phone, course), commit=True)

    def get_user_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM users")
        count = self.cursor.fetchone()[0]
        return count
    
    def get_all_users(self):

        sql = "SELECT telegram_id, full_name FROM users"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
