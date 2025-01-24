import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import Registor

TOKEN = ""

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Wikipediya botga hush kelibsiz"
    await message.answer(text)

@dp.message(Command("reg"))
async def register(message: Message, state:FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun ma'limotlarni kiriting !  \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text   
    await state.update_data(ism = ism)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")

@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text   
    await state.update_data(familiya = familiya)
    await state.set_state(Registor.yosh)
    await message.answer("Yoshingizni kiriting")

@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text   
    await state.update_data(yosh = yosh)
    await state.set_state(Registor.kurs)
    await message.answer("Kursni nomini kiriting")

@dp.message(F.text, Registor.kurs)
async def register_kurs(message: Message, state:FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    familiya = data.get("familiya")
    yosh = data.get("yosh")
    kurs = message.text  

    text = f"Ism : {ism} \nFamiliya : {familiya} \nYosh : {yosh} \nKurs : {kurs}"
    await message.answer("Siz ro'yxatdan o'tdingiz")

    await bot.send_message(chat_id=000000, text=text)
    await state.clear()
    
async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())