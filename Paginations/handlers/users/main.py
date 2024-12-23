from loader import dp
from aiogram import F
from aiogram.types import Message, CallbackQuery
from keyboard_buttons.inline import menu

@dp.message(F.text == "Paginations")
async def info_numbers(message: Message):
    await message.answer("Bizning sonlar", reply_markup=menu.get_number_menu(page=0))

# Sahifalar orasida harakatlanish uchun tugmalarni boshqarish
@dp.callback_query(lambda call: call.data.startswith("left") or call.data.startswith("right"))
async def navigate_numbers(call: CallbackQuery):
    direction, current_page = call.data.split(":")
    current_page = int(current_page)

    # Harakatlanish logikasi
    if direction == "left" and current_page > 0:
        current_page -= 1
    elif direction == "right" and (current_page + 1) * 4 < len(menu.numbers):
        current_page += 1
    else:
         await call.message.answer("Bunday sahifa mavjid emas !")

    # Yangi menyuni jo'natamiz
    await call.message.edit_reply_markup(reply_markup=menu.get_number_menu(page=current_page))
