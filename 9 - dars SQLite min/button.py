from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlite import get_all_computers_names

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Laptop")] 

    ],
    resize_keyboard=True,
    input_field_placeholder = "Menu dan biring bosing 🔘 ..."
)

computers = get_all_computers_names()

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

computer_button.adjust(3)

computer_button = computer_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Kompyuterni tanlang..."
)

phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqam yuborish", request_contact=True)],
    ],
    resize_keyboard=True,
)