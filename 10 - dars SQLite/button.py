from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish 📝")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Foydalanuvchilar ro'yxati 📋"), KeyboardButton(text="Foydalanuvchi soni 📊")],
        
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)