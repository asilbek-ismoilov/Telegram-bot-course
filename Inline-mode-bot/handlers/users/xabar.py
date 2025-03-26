from aiogram.types import Message
from loader import dp, bot, ADMINS
from aiogram.filters import Command
from states.help_stt import Help
from aiogram.fsm.context import FSMContext

@dp.message(Command("xabar"))
async def help_commands(message:Message,state:FSMContext):
    await message.answer("Xabaringizni yozib ✍🏻 \nMurojatingiz 👤 adminga boradi !")
    await state.set_state(Help.help)

@dp.message(Help.help)
async def send_advert(message: Message, state: FSMContext):
    help_text = message.text
    from_chat_id = message.from_user.id

    text = f"📬 ... Botdan murojat keldi!\n\n📜 Xabar: {help_text}"
    await bot.send_message(chat_id=ADMINS[0], text=text)
    await bot.copy_message(chat_id=ADMINS[0], from_chat_id=from_chat_id, message_id=message.message_id)
    await message.answer("Sizning xabaringiz adminga yuborildi ✅")
    await state.clear()
