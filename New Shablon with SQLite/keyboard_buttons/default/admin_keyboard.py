from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
            KeyboardButton(text="Noutbuk ma'lumotlari"),
        ]
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

laptop = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Qo'shish"),KeyboardButton(text="Yangilash")],
        [KeyboardButton(text="Ko'rish"),KeyboardButton(text="O'chirish")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Menudan birini tanlang"
)

