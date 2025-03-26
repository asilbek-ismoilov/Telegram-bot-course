import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = ""
ADMIN_ID = 00

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz"
    await message.answer(text, protect_content=True)

@dp.message(Command("link"))
async def link(message: Message):
    # text = "Ushbu kanallarga obuna bo'ling:\n\n👉 [Kanallar ro'yxati](https://t.me/addlist/ihgx8XysoMZlZmIy)"
    # await message.answer(text, disable_web_page_preview=True)
    text = "Ushbu kanallarga obuna bo'ling: <a href='https://t.me/addlist/ihgx8XysoMZlZmIy'>Kanallar ro'yxati</a>"
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)

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
