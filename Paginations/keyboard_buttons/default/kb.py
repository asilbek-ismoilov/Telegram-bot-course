from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

max_menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Paginations")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Tanlang .. "
)
