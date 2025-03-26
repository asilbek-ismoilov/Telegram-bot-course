import json
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def load_buttons():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
texts = load_buttons()

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Eng 🇺🇸", callback_data="en"), 
            InlineKeyboardButton(text="Uzb 🇺🇿", callback_data="uz"), 
            InlineKeyboardButton(text="Rus 🇷🇺", callback_data="ru"), 
        ]
    ]
)

def menu_line(language):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=texts[language]["line_menu"]["button_1"], callback_data="go"), 
            ]
        ]
    )
    return menu
