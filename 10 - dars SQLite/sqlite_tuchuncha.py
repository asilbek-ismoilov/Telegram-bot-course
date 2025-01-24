import sqlite3

# import sqlite3 — bu qator SQLite bilan ishlash uchun kerak bo'lgan sqlite3 modulini dasturimizga kiritadi. 
# SQLite bu kichik hajmli, engil vaznli ma'lumotlar bazasi bo'lib, uni alohida server o'rnatmasdan 
# to'g'ridan-to'g'ri fayllar ichida saqlash imkonini beradi.

class Database:
# class Database: — bu qator yangi Database nomli klassni yaratadi. Klasslar obyektga yo'naltirilgan 
# dasturlash (OOP) usulida ma'lumotlar va metodlarni bir joyda saqlash va boshqarish uchun ishlatiladi.
    def __init__(self, path_to_db="users.db"):
        # __init__ metodi — bu klassdan yangi obyekt yaratilganda avtomatik ishlaydigan maxsus metod. Uning asosiy 
        # vazifasi — obyektni boshlang'ich holatga keltirish (ya'ni, unga dastlabki qiymatlar berish).
        # path_to_db="users.db" — bu parametr orqali bazaga ulanish uchun fayl nomi (yo'li) beriladi. 
        #   Agar bu parametr berilmasa, u avtomatik ravishda users.db faylini tanlaydi. Demak, ma'lumotlar shu faylda saqlanadi.
        self.connection = sqlite3.connect(path_to_db)
        # self.connection = sqlite3.connect(path_to_db) — bu qator orqali SQLite bazasi fayliga (path_to_db) ulanish o'rnatiladi. 
        # Agar fayl mavjud bo'lmasa, u avtomatik ravishda yangi fayl yaratadi.
        self.cursor = self.connection.cursor()
        # self.cursor = self.connection.cursor() — bu yerda cursor obyektini yaratamiz. 
        # cursor orqali SQL buyruqlarini bajarish va natijalarni olish mumkin.

    def execute(self, sql, parameters=None, commit=False):
        # execute metodi — bu umumiy maqsadli metod bo'lib, u SQL buyruqlarini bajarish uchun ishlatiladi.
        # sql — bu parametrga SQL buyrug'i (masalan, CREATE TABLE, INSERT INTO kabi) kiritiladi
        # parameters=None — bu parametr SQL buyrug'idagi bo'sh joylarga (ya'ni ? belgilariga) kiritiladigan 
        #   qiymatlarni belgilaydi. Agar parametrlar berilmasa, u avtomatik ravishda None bo'ladi.
        if parameters is None:
            parameters = ()
            # Bu qator shuni tekshiradi: agar parameters bo'sh (None) bo'lsa, u holda parametersni bo'sh 
            # tuple (()) deb o'rnatadi. Bu degani, agar SQL buyrug'iga hech qanday parametrlar kerak bo'lmasa, 
            # parameters oddiy tuple bo'lib qoladi va xato chiqmaydi.

            # Agar SQL buyrug'i parametrlar talab qilsa, masalan:
                # INSERT INTO Users(name, surname, age) VALUES(?, ?, ?);
            # Bu yerda uchta ? belgi bor, va ularni parameters ichidagi qiymatlar bilan almashtiramiz (masalan, ('John', 'Doe', 25)).

            # Agar SQL buyrug'i parametrlar talab qilmasa, masalan:
                # CREATE TABLE Users(name TEXT, surname TEXT);
            # Bu yerda hech qanday parametr kerak emas, shuning uchun parameters=None va bu holda parameters bo'sh tuple bo'lib qoladi.

        self.cursor.execute(sql, parameters)
        # self.cursor.execute(sql, parameters) — bu qator SQL buyrug'ini bajaradi. Agar SQL buyruq parametrlarni talab 
        # qilsa, ularni parameters yordamida buyruqqa joylashtiradi.

        # commit=False — bu parametr SQL buyruqni bajarishdan keyin o'zgarishlarni bazaga saqlash kerakligini 
        # ko'rsatadi. Agar commit=True bo'lsa, bazaga kiritilgan o'zgarishlar doimiy saqlanadi.
        if commit:
            self.connection.commit()
            # elf.connection.commit() — bu qator SQL buyrug'i orqali amalga oshirilgan o'zgarishlarni (masalan, yangi foydalanuvchi 
            # qo'shilishi yoki jadval yaratilishi) bazaga yozadi. Bu qator faqat commit=True bo'lganda bajariladi.

    # Jadval yaratish metodi (create_table_users)
    def create_table_users(self):
        # create_table_users metodi — bu metod Users nomli jadval yaratadi. CREATE TABLE IF NOT EXISTS SQL 
        # buyrug'i orqali jadval yaratiladi, agar oldin mavjud bo'lmasa.
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
            name TEXT,
            surname TEXT,
            age INTEGER,
            tel TEXT,
            kurs TEXT
        );
        """
        # Jadval ustunlari:
        # - name — ism (matn turidagi ma'lumot),
        # - surname — familiya (matn),
        # - age — yosh (butun son),
        # - tel — telefon raqami (matn),
        # - kurs — kurs nomi (matn).
        self.execute(sql, commit=True)
        # self.execute(sql, commit=True) — bu SQL buyrug'ini bajaradi va o'zgarishlarni bazaga saqlaydi (commit=True).

    # Foydalanuvchini qo'shish metodi (add_user)
    def add_user(self, name: str, surname: str, age: int, tel: str, kurs: str):
        # add_user metodi — bu metod yangi foydalanuvchini Users jadvaliga qo'sh
        sql = """
        INSERT INTO Users(name, surname, age, tel, kurs) VALUES(?, ?, ?, ?, ?);
        """
        # SQL buyruq ichida VALUES(?, ?, ?, ?, ?) qismi qiymatlarning joyini belgilaydi. 
        # Keyin bu qiymatlar (name, surname, age, tel, kurs) tuple ko'rinishida metodga uzatiladi.
        
        # Misol: Agar foydalanuvchining ismi "John", familiyasi "Doe", yoshi 25, telefon raqami "+998900000000", kursi "Python" bo'lsa, 
        # SQL buyrug'i quyidagicha ko'rinishga keladi:
            # INSERT INTO Users(name, surname, age, tel, kurs) VALUES('John', 'Doe', 25, '+998900000000', 'Python');
        self.execute(sql, parameters=(name, surname, age, tel, kurs), commit=True)
        # bu qator orqali SQL buyrug'i bajariladi va o'zgarishlar saqlanadi.

    # Bazani yopish metodi (close)
    def close(self):
        self.connection.close()
        # close metodi — bu metod bazaga ulanishni yopadi. self.connection.close() qatori orqali SQLite bilan bog'lanish to'xtatiladi. 
        # Bu juda muhim, chunki bazani yopmaslik uning xotirada qolishiga yoki boshqa dasturlarda ishlashiga to'sqinlik qilishi mumkin.


# Qo'shimcha
def get_user_count(self):
# get_user_count — bu funksiya, u self argumentini oladi. self argumenti, odatda, klasslar ichida o'z ob'ektlariga 
# murojaat qilish uchun ishlatiladi. Bu funksiya Database klassiga tegishli bo'lishi mumkin.
    self.cursor.execute("SELECT COUNT(*) FROM users")
    # self.cursor — bu SQL so'rovlarini bajarish uchun ishlatiladigan ob'ekt. execute metodi SQL so'rovini bajaradi.
    # "SELECT COUNT(*) FROM users" — bu SQL so'rovi.
        # SELECT COUNT(*) — bu SQL buyruq, u users jadvalidagi barcha qatorlarni hisoblaydi.
        # FROM users — bu so'rov qaysi jadvaldan ma'lumot olishini ko'rsatadi (bu holda, users jadvalidan).
    count = self.cursor.fetchone()[0]
    # fetchone() metodi so'rov natijasining birinchi qatorini qaytaradi.
    # [0] — bu natijada qaytarilgan qatorning birinchi elementi (bu holda, COUNT(*) 
    # natijasi, ya'ni foydalanuvchilar soni) olinadi va count o'zgaruvchisiga saqlanadi.

    return count
    # count o'zgaruvchisi (foydalanuvchilar soni) funksiyadan qaytariladi, 
    # shuning uchun bu qiymat boshqa joylarda ishlatilishi mumkin.