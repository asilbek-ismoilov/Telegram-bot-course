from loader import bot,db,dp,ADMINS
from aiogram.types import Message
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts
from aiogram.fsm.context import FSMContext
from keyboard_buttons.default import admin_keyboard
import time 
from aiogram import F
from states.help_stt import LaptopAdd

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
            await bot.copy_message(chat_id=user[0], from_chat_id=from_chat_id, message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(F.text=="Noutbuk ma'lumotlari",IsBotAdminFilter(ADMINS))
async def laptop_db(message:Message):
    await message.answer("Kerakli buttoni bosing !", reply_markup=admin_keyboard.laptop)

@dp.message(F.text == "Qo'shish",IsBotAdminFilter(ADMINS))
async def add_laptop(message:Message,state:FSMContext):
    await message.answer("Noutbuk nomini kiriting !")
    await state.set_state(LaptopAdd.name)

@dp.message(F.text, LaptopAdd.name ,IsBotAdminFilter(ADMINS))
async def laptop_name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data(name = name)
    await message.answer("Rasmini kiriting")
    await state.set_state(LaptopAdd.pic)

@dp.message(F.photo, LaptopAdd.pic,IsBotAdminFilter(ADMINS))
async def laptop_pic(message:Message,state:FSMContext):
    pic = message.photo[-1].file_id
    await state.update_data(pic = pic)
    await message.answer("Rangini kiriting !")
    await state.set_state(LaptopAdd.color)

@dp.message(F.text, LaptopAdd.color ,IsBotAdminFilter(ADMINS))
async def laptop_color(message:Message,state:FSMContext):
    color = message.text
    await state.update_data(color = color)
    await message.answer("Xotirasini kiriitng")
    await state.set_state(LaptopAdd.storage)

@dp.message(F.text, LaptopAdd.storage ,IsBotAdminFilter(ADMINS))
async def laptop_storage(message:Message,state:FSMContext):
    storage = message.text
    await state.update_data(storage = storage)
    await message.answer("Narxini kiriting !")
    await state.set_state(LaptopAdd.price)

@dp.message(F.text, LaptopAdd.price ,IsBotAdminFilter(ADMINS))
async def laptop_price(message:Message,state:FSMContext):

    data = await state.get_data()
    name = data.get("name")
    pic = data.get("pic")
    color = data.get("color")
    storage = data.get("storage")
    price = data.get("price")
    price = message.text
    db.add_laptop(name=name,pic=pic,color=color,storage=storage,price=price)
    text = f"Nomi: {name} \nRangi: {color} \nXotirasi: {storage} \nNarxi: ${price}"

    for admin in ADMINS:
        await bot.send_photo(chat_id=admin,photo=pic,caption=text)
        await bot.send_message(chat_id=admin,text="Noutbuk qo'shildi 🎉")
    await state.clear()

@dp.message(F.text == "Ko'rish",IsBotAdminFilter(ADMINS))
async def laptop_data_get(message:Message):
    all_laptops = db.laptop_data()
    print(all_laptops)
    for laptop in all_laptops:
        name, pic, storage, color, price = laptop
        text = f"Nomi: <code>{name}</code> \nRangi: {color} \nXotirasi: {storage} \nNarxi: ${price}"
        await message.answer_photo(photo=pic,caption=text, parse_mode="HTML")

    
    