from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish 📝"), KeyboardButton(text="Foydalanuvchi soni 📊")],
        [KeyboardButton(text="Foydalanuvchilar ro'yxati 📋")]
        
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)