import time 
from aiogram import F
from loader import bot,db,dp,ADMINS
from aiogram.types import Message
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts
from states.help_stt import Voice
from aiogram.fsm.context import FSMContext
from keyboard_buttons.default import admin_keyboard


@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)

@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

# ----------------------------------------------------------------------

@dp.message(F.text == "Ovoz qo'shish", IsBotAdminFilter(ADMINS))
async def add_voice(message:Message, state:FSMContext):
    await message.answer(text="➕ Qo'shish \nOvoz nomini kiriting !")
    await state.set_state(Voice.name)

@dp.message(F.text, Voice.name, IsBotAdminFilter(ADMINS))
async def add_voice_name(message:Message, state:FSMContext):
    name = message.text
    await state.update_data(name = name)
    await message.answer(text="Ovozni yuboring !")
    await state.set_state(Voice.voice)

@dp.message(lambda message: message.voice or message.audio, Voice.voice, IsBotAdminFilter(ADMINS))
async def add_voice_file(message:Message, state:FSMContext):
    data = await state.get_data()
    name = data.get("name")

    if message.audio: 
        voice = message.audio.file_id
        print(f"audio - {voice}")
        
    elif message.voice: 
        voice = message.voice.file_id
        print(f"voice - {voice}")

    db.add_voice(name=name, voice_file_id=voice)
    await message.answer(text="Ovoz muvaffaqiyatli qo'shildi !")
    await state.clear()
