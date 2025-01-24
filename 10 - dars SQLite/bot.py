import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Registor
from button import menu
from sqlite import Database  # SQLite'dan bazani import qilamiz

TOKEN = ""
ADMIN_ID = []

dp = Dispatcher()

db = Database()  # Baza obyektini yaratamiz
db.create_table_users()  # Users jadvalini yaratish

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id

    # Foydalanuvchini bazaga qo'shish
    db.add_user(telegram_id, full_name, None, None, None, None, None)

    text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz"
    await message.answer(text, reply_markup=menu)

@dp.message(F.text=="Ro'yxatdan o'tish 📝")
async def register(message: Message, state:FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun ma'limotlarni kiriting !  \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

# First_name
@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    name = message.text
    await state.update_data(name = name)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")
# end First_name

@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text 
    await state.update_data(surname = familiya)
    await state.set_state(Registor.yosh)
    await message.answer("Yoshingizni kiriting")

@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text
    await state.update_data(age = yosh)
    await state.set_state(Registor.tel)
    await message.answer("Telefon raqamni kiriting")

# Phone_number
@dp.message(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.tel)
async def register_tel(message: Message, state:FSMContext):
    tel = message.text
    await state.update_data(tel = tel)
    await state.set_state(Registor.kurs)
    await message.answer("Kursni nomini kiriting")

# end Phone_number

@dp.message(F.text, Registor.kurs)
async def register_kurs(message: Message, state: FSMContext):
    data = await state.get_data() 

    ism = data.get("name")
    familiya = data.get("surname")
    yosh = data.get("age")
    tel = data.get("tel")
    kurs = message.text

    telegram_id = message.from_user.id
    full_name = message.from_user.full_name

    # Foydalanuvchi ma'lumotlarini yangilab bazaga qo'shish
    
    db.add_user(telegram_id, full_name, ism, familiya, yosh, tel, kurs)

    text = f"Ism : {ism} \nFamiliya : {familiya} \nYosh : {yosh} \nTel : {tel} \nKurs : {kurs}"
    await message.answer("Siz ro'yxatdan o'tdingiz")

    for admin in ADMIN_ID:
        await bot.send_message(chat_id=admin, text=text)
    await state.clear()
    
@dp.message(F.text=="Foydalanuvchi soni 📊")
async def register(message: Message):
    user_count = db.get_user_count()
    await message.answer(f"Bazada ro'yxatdan o'tgan foydalanuvchilar soni: {user_count}")

@dp.message(F.text == "Foydalanuvchilar ro'yxati 📋")
async def all_user(message: Message):
    # Barcha foydalanuvchilarni olib kelamiz
    users = db.get_all_users()
    
    if users:
        response_text = "Foydalanuvchilar ro'yxati:\n\n"
        for user in users:
            response_text += f"Telegram ID: <code>{user[0]}</code>, Full Name: <code>{user[1]}</code>\n"
        await message.answer(response_text, parse_mode="HTML")
    else:
        await message.answer("Bazada hali hech qanday foydalanuvchi yo'q.")


@dp.startup()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Tabriklaymiz 🎉 \nBotimiz ishga tushdi ")

@dp.shutdown()
async def bot_start():
    db.close()  # Baza ulanishini yopamiz
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Bot to'xtadi ❗️")

    
async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
