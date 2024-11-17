import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.types import Message, CallbackQuery
from removebg import bg_add_pic, remove_bg, remove_bg_color
from keyboardbutton import menu
from states import BagPic, RemoveBg, BagColor
from inlinebutton import colors_button

TOKEN = ""
ADMIN_ID = []

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\n"
    await message.reply(text=text, reply_markup=menu)

# start Add bg fon 
#-------------------

@dp.message(F.text == "Fonga rasm qo'yish")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Orqa fon uchun rasim kiriting")
    await state.set_state(BagPic.background_pic)

@dp.message(F.photo, BagPic.background_pic)
async def bag_picture(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id

    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    await state.update_data(bg_url = photos_url)
    await state.set_state(BagPic.photo)
    await message.answer("Rasm kiriting")

@dp.message(F.photo, BagPic.photo)
async def picture(message:Message, state:FSMContext):
    data = await state.get_data()
 
    bg_url = data.get("bg_url")

    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    rasm = bg_add_pic(bg_url, photos_url)
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        
    await state.clear()

#-------------------
# finish Add bg fon 


# start remove bg  
#-------------------
@dp.message(F.text == "Fonni olib tashlash")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Fonni olib tashlash uchun rasim kiriting")
    await state.set_state(RemoveBg.removebg)

@dp.message(F.photo, RemoveBg.removebg)
async def picture(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg(photos_url)
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
        await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))
    
    await state.clear()

#-------------------
# finish remove bg 

# start add color bg
#-------------------

@dp.message(F.text == "Fonga rang berish")
async def bag_pic(message:Message, state:FSMContext):
    await message.answer("Orqa fonga rang kiritish uchun rasim kiriting")
    await state.set_state(BagColor.bagcolor)

@dp.message(F.photo, BagColor.bagcolor)
async def photo(message:Message, state:FSMContext):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url)
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)


# black
@dp.callback_query(F.data=="black")
async def black_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "black")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# red
@dp.callback_query(F.data=="red")
async def red_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg_color(photos_url, "red")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

#-------------------
# finish add color bg


@dp.startup()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Tabriklaymiz 🎉 \nBotimiz ishga tushdi ")

@dp.shutdown()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Bot to'xtadi ❗️")

async def main() -> None:
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
