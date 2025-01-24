from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from baza import computers_info

# 1 - usul
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Phone"), KeyboardButton(text="Laptop")],
        [KeyboardButton(text="About us")] 

    ],
    resize_keyboard=True,
    input_field_placeholder = "Menu dan biring bosing 🔘 ..."
)

# Telefon

phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☎️ Telefon raqamni kiriting", request_contact=True)],

    ],
    resize_keyboard=True,
    input_field_placeholder = "Telefon raqam kiriting ✍️ ..."
)


# 2 - usul


computers = list(computers_info.keys())

computer_button = ReplyKeyboardBuilder() 

for computer in computers:
    computer_button.add(KeyboardButton(text=computer)) 

computer_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

computer_button.adjust(3, repeat=True)

computer_button = computer_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Choise computer..."
)
