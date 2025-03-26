from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

saved = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Buyurtma qilish !", callback_data="reg")],
    ]
)
