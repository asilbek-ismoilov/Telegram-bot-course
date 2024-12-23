from aiogram.types import Message
from loader import dp, db
from aiogram.filters import CommandStart
from keyboard_buttons.default.kb import max_menu_button

@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz", reply_markup=max_menu_button)
    except:
        await message.answer(text="Assalomu alaykum", reply_markup=max_menu_button)
