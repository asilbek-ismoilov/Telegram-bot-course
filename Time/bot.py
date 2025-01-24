import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import time
from state import Time

TOKEN = ""
ADMIN_ID = 0

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum {full_name}, botga hush kelibsiz"
    await message.answer(text)

@dp.message(Command("time"))
async def get_time(message: Message):
    formatted_time = time.strftime("%H : %M : %S | %d.%m.%Y")
    await message.answer(formatted_time)


@dp.message(Command("send_time"))
async def get_send_time(message: Message, state: FSMContext):
    await message.answer("Vaqtni kiriting ! :\nM: 20:30:15")
    await state.set_state(Time.time)

@dp.message(F.text, Time.time)
async def send_time(message: Message):

    while True:
        if time.strftime('%H:%M:%S') == message.text:
            await message.answer("Vaqt tugadi 🕐")
            print("Ishladi ✅")
            break
        else:
            continue


@dp.startup()
async def bot_start():
    await bot.send_message(ADMIN_ID, "Tabriklaymiz 🎉 \n\nBot ishga tushdi 😊")

@dp.shutdown()
async def bot_start():
    await bot.send_message(ADMIN_ID, "Bot to'xtadi ❗️")
     

async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
