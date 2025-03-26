import json
from aiogram import F
from loader import dp, db
from aiogram.types import Message, CallbackQuery
from keyboard_buttons.default.menu import menu
from keyboard_buttons.inline.menu import menu_line

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(lambda message: message.text in ["Sample button", "Namuna tugma", "Пример кнопки"])
async def test_message(message:Message):
    id = message.from_user.id
    language = db.select_language(id)[0]

    text = texts[language]["simple"] + "   ✨"

    await message.answer(text)

@dp.message(lambda message: message.text in ["Inline button", "Inline tugma", "Inline-кнопка"])
async def test_message(message:Message):
    id = message.from_user.id
    language = db.select_language(id)[0]

    text = texts[language]["simple"] + "   ⚡️"

    await message.answer(text, reply_markup=menu_line(language))

@dp.callback_query(F.data == "go")
async def test_message(call:CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    language = db.select_language(id)[0]

    text = texts[language]["simple"] + "   💥"

    await call.message.answer(text)

