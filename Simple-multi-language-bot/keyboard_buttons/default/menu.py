import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def load_buttons():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
texts = load_buttons()


def menu(language):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=texts[language]["menu"]["button_1"]),
                KeyboardButton(text=texts[language]["menu"]["button_2"]),
            ]
            
        ],
       resize_keyboard=True,
       input_field_placeholder="Menudan birini tanlang"
    )
    return menu   

