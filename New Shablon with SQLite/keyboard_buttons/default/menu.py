from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import db

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Laptop")] 

    ],
    resize_keyboard=True,
    input_field_placeholder = "Menu dan biring bosing 🔘 ..."
)

computers = [row[0] for row in db.laptop_name()]

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

computer_button.adjust(3)

computer_button = computer_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Kompyuterni tanlang..."
)
