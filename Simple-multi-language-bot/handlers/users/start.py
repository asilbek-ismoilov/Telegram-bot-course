import json
from loader import dp,db
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from states.help_stt import ChooseLanguage
from keyboard_buttons.default.menu import menu
from aiogram.types import Message, CallbackQuery
from keyboard_buttons.inline.menu import language

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()


@dp.message(CommandStart())
async def start_command(message:Message, state:FSMContext):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id

    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id, language=None) 
    except:
        pass
    text = "Select language 🇺🇸 | Tilni tanlang 🇺🇿 | Выберите язык 🇷🇺"
    await message.answer(text, reply_markup=language)
    await state.set_state(ChooseLanguage.language)

@dp.callback_query(ChooseLanguage.language)    
async def choose_language(call:CallbackQuery, state:FSMContext):
    await call.message.delete()

    language = call.data
    user_id = call.from_user.id

    text=texts[language]["start"]
    db.update_user(telegram_id=user_id, language=language)

    await call.message.answer(text=text, reply_markup=menu(language))
    await state.clear()

