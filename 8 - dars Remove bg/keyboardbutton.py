from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Fonga rasm qo'yish"), KeyboardButton(text="Fonni olib tashlash"), KeyboardButton(text="Fonga rang berish")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)