import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile

dp = Dispatcher()

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(F.text)
async def text_message(message: Message):
    text = message.text
    await message.answer("Sizning yuborgan xabaringiz: " + text)

# Document uchun handler
@dp.message(F.document)
async def document_message(message: Message):
    document = message.document
    await message.answer_document(document.file_id, caption="Sizning yuborgan hujjatingiz")

# Video uchun handler
@dp.message(F.video)
async def video_message(message: Message):
    video = message.video
    await message.answer_video(video.file_id, caption="Sizning yuborgan videongiz")

# Foto uchun handler
@dp.message(F.photo)
async def photo_message(message: Message):
    photo = message.photo[-1]  # Oxirgi foto varianti eng yaxshi sifatda
    await message.answer_photo(photo.file_id, caption="Sizning yuborgan fotosuratingiz")

# Audio uchun handler
@dp.message(F.audio)
async def audio_message(message: Message):
    audio = message.audio
    await message.answer_audio(audio.file_id, caption="Sizning yuborgan audiongiz")

# Location uchun handler
@dp.message(F.location)
async def location_message(message: Message):
    location = message.location
    await message.answer(f"Sizning yuborgan joylashuvingiz: ({location.latitude}, {location.longitude})")

# Animation uchun handler
@dp.message(F.animation)
async def animation_message(message: Message):
    animation = message.animation
    await message.answer_animation(animation.file_id, caption="Sizning yuborgan animatsiyangiz")

# Video Note uchun handler
@dp.message(F.video_note)
async def video_note_message(message: Message):
    video_note = message.video_note
    await message.answer_video_note(video_note.file_id)

# Contact uchun handler
@dp.message(F.contact)
async def contact_message(message: Message):
    contact = message.contact
    await message.answer(f"Sizning yuborgan kontakt: {contact.full_name}, Telefon: {contact.phone_number}")

# Game uchun handler
@dp.message(F.game)
async def game_message(message: Message):
    await message.answer("Siz o'yin yubordingiz.")

# Dice uchun handler
@dp.message(F.dice)
async def dice_message(message: Message):
    dice = message.dice
    await message.answer(f"Siz kubik tashladingiz va {dice.value} chiqdi!")

# Voice uchun handler
@dp.message(F.voice)
async def voice_message(message: Message):
    voice = message.voice
    await message.answer_voice(voice.file_id, caption="Sizning yuborgan ovozingiz")

# Media Group uchun handler
@dp.message(F.media_group)
async def media_group_message(message: Message):
    await message.answer("Siz media-guruh yubordingiz")

# Poll uchun handler
@dp.message(F.poll)
async def poll_message(message: Message):
    poll = message.poll
    await message.answer(f"Siz yuborgan so'rovnoma: {poll.question}")

# Sticker uchun handler
@dp.message(F.sticker)
async def sticker_message(message: Message):
    sticker = message.sticker
    await message.answer_sticker(sticker.file_id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
