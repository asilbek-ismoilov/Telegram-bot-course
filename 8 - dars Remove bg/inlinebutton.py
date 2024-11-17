from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

colors_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Oq", callback_data="white"), InlineKeyboardButton(text="Qora", callback_data="black")],
        [InlineKeyboardButton(text="Sariq", callback_data="yellow"), InlineKeyboardButton(text="Qizil", callback_data="red")],
        [InlineKeyboardButton(text="Ko'k", callback_data="blue"), InlineKeyboardButton(text="Yashil", callback_data="green")],
    ]
)
