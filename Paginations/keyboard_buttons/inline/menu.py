from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

numbers = list(range(1, 51))

def get_number_menu(page=0):
    # Sahifa 4 tadan qilib bo'linadi
    numbers_per_page = 10
    start = page * numbers_per_page # 0 * 10 = 0 | 1 * 10 = 10
    end = start + numbers_per_page # 0 + 10 = 10 | 10 + 10 = 20
    sliced_numbers = numbers[start:end] # 0 : 10 | 10 : 20

    keyboard = []

    # Sonlarni qo'shamiz
    for number in sliced_numbers:
        keyboard.append([InlineKeyboardButton(text=str(number), callback_data=str(number))])

    # ⬅️ va ➡️ tugmalari
    navigation_buttons = [
        InlineKeyboardButton(text="⬅️", callback_data=f"left:{page}"),
        InlineKeyboardButton(text="➡️", callback_data=f"right:{page}")
    ]
    keyboard.append(navigation_buttons)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
