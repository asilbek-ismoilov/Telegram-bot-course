import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, input_file, InputFile
from cat import cat_img 

# cat_gif , cat_tag_text 

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(Command("cat"))
async def cat(message: Message):
    image = cat_img()
    if image:
        await message.answer_document(document=input_file.BufferedInputFile(file=image, filename="cat.png"))
        # await message.answer_document(document=InputFile(image_content, filename="cat.png"))

# @dp.message(Command("cat"))
# async def cat(message: Message):
#     image = cat_gif()
#     if image:
#         await message.answer_document(document=input_file.BufferedInputFile(file=image, filename="cat.gif"))

# @dp.message(Command("cat"))   
# async def cat(message: Message):
#     image = cat_tag_text("smile", "Hello world")
#     if image:
#         await message.answer_document(document=input_file.BufferedInputFile(file=image, filename="cat.png"))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())