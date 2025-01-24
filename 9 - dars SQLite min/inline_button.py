from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="iPhone", callback_data="iphone"), InlineKeyboardButton(text="Samsung", callback_data="samsung"),],
        [InlineKeyboardButton(text="Xiaomi", callback_data="xiaomi"), InlineKeyboardButton(text="Google Pixel", callback_data="google_pixel"),],
        [InlineKeyboardButton(text="Honor", callback_data="honor")]
    ]
)   


saved = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Buyurtma qilish !", callback_data="reg")],
    ]
)
