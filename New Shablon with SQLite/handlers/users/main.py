from loader import dp, db, bot, ADMINS
from aiogram.types import Message, CallbackQuery
from aiogram import F
from keyboard_buttons.default.menu import computer_button
from states.help_stt import Computer
from aiogram.fsm.context import FSMContext
from keyboard_buttons.inline.menu import saved
from keyboard_buttons.default.menu import menu
from states.help_stt import Registor

@dp.message(F.text == "Orqaga qaytish 🔙")
async def orqaga(message: Message):
    await message.answer("Menu", reply_markup=menu)

@dp.message(F.text == "Laptop")
async def laptop(message:Message, state: FSMContext):
    await message.answer("Noutbuklardan birini tanlang", reply_markup=computer_button)
    await state.set_state(Computer.computer)

@dp.message(F.text, Computer.computer)
async def computer_info(message: Message, state: FSMContext):
    computer_name = message.text
    computers  = db.get_computers(computer_name) 


    name, photo, price, color = computers[0]     
    text = f"Nom : {name}\nRang : {color}\nNarxi : ${price}"
    
    await state.update_data(computer=name)
    await message.answer_photo(photo=photo, caption=text)


