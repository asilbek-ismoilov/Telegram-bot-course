import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext 
from state import Registor
from button import menu, computer_button, phone_button
from baza import computers_info, phones_info
from inline_button import menu_inline, saved

TOKEN = ""
ADMIN_ID = []

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum <b>{full_name}</b> 🙂, Online do'kon botga xush kelibsiz 🥳"
    await message.answer(text, parse_mode="HTML", reply_markup=menu)
    await message.answer("Botdan foydalanish uchun tugmalardan birini tanlang !")

#  ❗️❗️❗️ NOUTBUKLAR ❗️❗️❗️

@dp.message(F.text == "Laptop")
async def laptop(message: Message):
    await message.answer("Noutbuklardan birini tanlang", reply_markup=computer_button)

@dp.message(lambda message: message.text in computers_info.keys())
async def computer_info(message: Message, state:FSMContext):

    await state.clear()

    computer = message.text
    info = computers_info[computer]
    photo = info["photo"]
    price = info["price"]
    color = info["color"]

    await state.update_data(computer = computer)

    text = f"Nom : {computer} \nRang : {color} \nNarxi : ${price}"
    await message.answer_photo(photo=photo, caption=text, reply_markup=saved)

# ❗️❗️❗️ TELEFONLAR ❗️❗️❗️

@dp.message(F.text == "Phone")
async def phone(message: Message):
    await message.answer("Telefoni tanlang", reply_markup=menu_inline)
    
@dp.callback_query(lambda callback: callback.data in phones_info.keys())
async def handle_phone_selection(callback: CallbackQuery, state: FSMContext):
    
    await callback.answer(callback.data  )

    phone = callback.data  
    info = phones_info[phone]
    photo = info["photo"]
    price = info["price"]
    color = info["color"]

    # Telefon haqida ma'lumotni saqlash
    await state.update_data(phone=phone)

    text = f"Nom: {phone.capitalize()} \nRang: {color} \nNarxi: ${price}"
    await callback.message.answer_photo(photo=photo, caption=text, reply_markup=saved)
    await state.clear()


# ❗️❗️❗️ RO'YXATDAN O'TISH ❗️❗️❗️

@dp.callback_query(F.data == "reg")
async def register(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.answer("Ro'yxatdan o'tish")
    await call.message.answer("Ro'yxatdan o'ting ❗️\nIsmingizni kiriting ✍️ ...")
    await state.set_state(Registor.name)

# ISM start
@dp.message(F.text, Registor.name)
async def register_name(message: Message, state:FSMContext):
    name = message.text   
    await state.update_data(name = name)
    await state.set_state(Registor.surname)
    await message.answer("Familiyani kiriting")

@dp.message(Registor.name)
async def register_ism_del(message:Message, state:FSMContext):
    await message.answer(text= "Ismimgizni to'g'ri kiriting!")
    await message.delete()
# ISM finish

# FAMILIYA start
@dp.message(F.text, Registor.surname)
async def register_surname(message: Message, state:FSMContext):
    surname = message.text   
    await state.update_data(surname = surname)
    await state.set_state(Registor.phone)
    await message.answer("Telefoni raqamini kiriting", reply_markup=phone_button)

@dp.message(Registor.surname)
async def register_familiya_del(message:Message, state:FSMContext):
    await message.answer(text= "Familiyani to'g'ri kiriting!")
    await message.delete()
# FAMILIYA finish

# PHONE start 
@dp.message(F.contact | F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Registor.phone)
async def register_tel(message: Message, state:FSMContext):

    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
 
    data = await state.get_data()
    name = data.get("name")
    surname = data.get("surname")
    computer = data.get("computer")


    text = f"Ism : {name} \nFamiliya : {surname} \nTel : {phone} \nNoutbuk : {computer}"
    await message.answer("Siz ro'yxatdan o'tdingiz", reply_markup=menu)
    await bot.send_message(chat_id= ADMIN_ID[0], text=text)
    await state.clear()
    
@dp.message(Registor.phone)
async def register_phone_del(message:Message, state:FSMContext):
    await message.answer(text= "Telefon raqamini to'g'ri kiriting!")
    await message.delete()

# ❗️❗️❗️ RO'YXATDAN O'TISH TUGADI ❗️❗️❗️



@dp.message(F.text == "About us")
async def about_us(message: Message):
    await message.answer("Bu 🤖 bot sizga savdo boti sifatida xizmat qila oladi !")


@dp.message(F.text == "Orqaga qaytish 🔙")
async def orqaga(message: Message):
    await message.answer("Menu", reply_markup=menu)



# ❗️❗️❗️ BOT ISHGA TUSHDI ❗️❗️❗️


@dp.startup()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Tabriklaymiz 🎉 \n\nBot ishga tushdi 😊")

@dp.shutdown()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Bot to'xtadi ❗️")
        
async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
