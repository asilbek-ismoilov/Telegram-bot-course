import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import Registor 

TOKEN = ""
ADMIN_ID =  0

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, botga hush kelibsiz"
    await message.answer(text)

@dp.message(Command("reg"))
async def register(message: Message, state:FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun ma'limotlarni kiriting !  \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

# ISM start
@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text   
    await state.update_data(ism = ism)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")

@dp.message(Registor.ism)
async def register_first_name_del(message:Message, state:FSMContext):
    await message.answer(text= "Ismimgizni to'g'ri kiriting!")
    await message.delete()

# ISM finish

# FAMILIYA start
@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text   
    await state.update_data(familiya = familiya)
    await state.set_state(Registor.yosh)
    await message.answer("Yoshingizni kiriting")
# FAMILIYA finish

@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text   
    await state.update_data(yosh = yosh)
    await state.set_state(Registor.tel)
    await message.answer("Telefon raqamni kiriting")

@dp.message(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.tel)
async def register_tel(message: Message, state:FSMContext):
    tel = message.text   
    await state.update_data(tel = tel)
    await state.set_state(Registor.email)
    await message.answer("Emailni kiriting")

@dp.message(F.text.regexp(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"), Registor.email)
async def register_email(message: Message, state:FSMContext):
    email = message.text   
    await state.update_data(email = email)
    await state.set_state(Registor.kurs)
    await message.answer("Kursni nomini kiriting")

@dp.message(F.text, Registor.kurs)
async def register_kurs(message: Message, state:FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    familiya = data.get("familiya")
    yosh = data.get("yosh")
    tel = data.get("tel")
    email = data.get("email")
    kurs = message.text  

    text = f"Ism : {ism} \nFamiliya : {familiya} \nYosh : {yosh} \nTel : {tel} \nEmail : {email} \nKurs : {kurs}"
    await message.answer("Siz ro'yxatdan o'tdingiz")
    await bot.send_message(chat_id= ADMIN_ID, text=text)
    await state.clear()
    

@dp.startup()
async def bot_start():
    await bot.send_message(ADMIN_ID, "Botimiz ishga tushdi !")

@dp.shutdown()
async def bot_start():
    await bot.send_message(ADMIN_ID, "Bot to'xtadi !")


async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
