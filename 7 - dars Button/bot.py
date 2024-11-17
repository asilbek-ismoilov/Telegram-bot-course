import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import Registor
from button import menu, send_contact, computer_button, computers
from baza import computers_info

TOKEN = ""
ADMIN_ID = 0

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state:FSMContext):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, botga hush kelibsiz"
    await message.answer(f"{text} \nRo'yxatdan o'ting va botdan to'liq foydalaning \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

# ISM start
@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text   
    await state.update_data(ism = ism)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")

@dp.message(Registor.ism)
async def register_ism_del(message:Message, state:FSMContext):
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

@dp.message(Registor.familiya)
async def register_familiya_del(message:Message, state:FSMContext):
    await message.answer(text= "Familiyani to'g'ri kiriting!")
    await message.delete()
# FAMILIYA finish

# YOSH start
@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text   
    await state.update_data(yosh = yosh)
    await state.set_state(Registor.tel)
    await message.answer("Telefon raqamni kiriting", reply_markup=send_contact)

@dp.message(Registor.yosh)
async def register_yosh_del(message:Message, state:FSMContext):
    await message.answer(text= "Yoshni to'g'ri kiriting!")
    await message.delete()
# YOSH finish

# PHONE start
@dp.message(F.contact | F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.tel)
async def register_tel(message: Message, state:FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
 
    await state.update_data(tel = phone)
    await state.set_state(Registor.email)
    await message.answer("Emailni kiriting")

@dp.message(Registor.tel)
async def register_tel_del(message:Message, state:FSMContext):
    await message.answer(text= "Telefonni to'g'ri kiriting!")
    await message.delete()
# PHONE finish

# Email start
@dp.message(F.text.regexp(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"), Registor.email)
async def register_email(message: Message, state:FSMContext):
    email = message.text   
    await state.update_data(email = email)
    await state.set_state(Registor.kurs)
    await message.answer("Kursni nomini kiriting")

@dp.message(Registor.email)
async def register_email_del(message:Message, state:FSMContext):
    await message.answer(text= "Emailni to'g'ri kiriting!")
    await message.delete()
# Email finish

# COURSE start
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
    await message.answer("Siz ro'yxatdan o'tdingiz", reply_markup=menu)
    await bot.send_message(chat_id= ADMIN_ID, text=text)
    await state.clear()
    
@dp.message(Registor.kurs)
async def register_kurs_del(message:Message, state:FSMContext):
    await message.answer(text= "Kurs nomini to'g'ri kiriting!")
    await message.delete()
# COURSE finish


# About
@dp.message(F.text=="💁🏻‍♂️ About us")
async def about_button(message: Message):
    text = "Biz sizga istalgan turdagi telefon yoki noutbuklarni sotib olishingizda yordam beramiz !"
    pic_url = "https://i.pinimg.com/originals/40/a9/c3/40a9c329dba2278c9775798067ebae2d.jpg"
    await message.answer_photo(pic_url, caption=text)
# endabout

# contact
@dp.message(F.text=="☎️ Contact admin")
async def about_button(message: Message):
    text = "Bot adminiga murojat qilish uchun: \nTel: +998 99 999 99 99"
    await message.answer(text)
# endcontact

@dp.message(F.text=="📍 Location")
async def location(message: Message):
    text = "Bizning savdo markazimizning kodi"
    lat = 40.102607
    lon = 65.37462
    await message.answer_location(lat, lon)
    await message.answer(text)

# latitude bilan longitude olish kodi 
# @dp.message(F.location)
# async def location(message: Message):
#     lat = message.location.latitude
#     lon = message.location.longitude

#     text = f"latitude:<code>{lat}</code>\n"
#     text += f"longitude:<code>{lon}</code>"

#     await message.answer(text, parse_mode="html")

@dp.message(F.text=="💻 Laptop")
async def my_computers(message:Message):
    text = "Noutbuk turini tugmalardan tanlang !"
    await message.answer(text,reply_markup=computer_button)

@dp.message(F.text.func(lambda computer: computer in computers))
async def computer_info(message:Message):
    info = computers_info.get(message.text)

    photo = info.get("photo")
    price = info.get("price")
    color = info.get("color")

    text = f"{message.text}\nprice: ${price}\ncolor:{color}\n...."

    await message.answer_photo(photo=photo,caption=text)


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
