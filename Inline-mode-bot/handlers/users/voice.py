from aiogram.types import Message, InlineQuery, InlineQueryResultCachedVoice, InlineQueryResultCachedAudio
from loader import dp, db
from aiogram import F
from aiogram.filters import or_f

# @dp.message(or_f(F.voice, F.audio))
# async def voice_handler(message: Message):
#     if message.voice:
#         file_id = message.voice.file_id
#         text = f"Voice ID: <code>{file_id}</code>"
#         await message.answer(text, parse_mode="HTML")
#         await message.answer_voice(file_id)
    
#     elif message.audio:
#         file_id = message.audio.file_id
#         text = f"Audio ID: <code>{file_id}</code>"
#         await message.answer(text, parse_mode="HTML")
#         await message.answer_audio(file_id)

# -----------------------------------------------------------------------
# Voice

# @dp.inline_query() 
# async def inline_voice(inline_query: InlineQuery): 
#     results = [ 
#         InlineQueryResultCachedVoice( 
#             id="1", 
#             voice_file_id="AwACAgQAAxkBAAIrH2fIPJHtCZG_kXxPYvE0LJkq1t1nAAKoAgACCsLMUMFEw42HDQIhNgQ",
#             title="Maqtov yorlig'i",
#             description="Inilne modul"
#         )
#     ] 

#     await inline_query.answer(results=results)


# -----------------------------------------------------------------------
# Audio

# @dp.inline_query() 
# async def inline_audio(inline_query: InlineQuery): 
#     results = [ 
#         InlineQueryResultCachedAudio( 
#             id="1", 
#             audio_file_id="CQACAgIAAxkBAAIrImfIPOvIXxQrCuyeIQffm2Xf9xXXAALvPAACsgypSUgAAYGydhqZtzYE",
#             title="Bu audio",
#         )
#     ] 

#     await inline_query.answer(results=results)

# -----------------------------------------------------------------------
# SQLite

# @dp.inline_query()
# async def inline_voice_search(inline_query: InlineQuery):
#     title = inline_query.query

#     voices = db.search_voices_title(title)

#     results = [
#         InlineQueryResultCachedVoice(
#             id=f"{voice[0]}",         # `id`
#             voice_file_id=voice[2],   # `voice_file_id`
#             title=voice[1]            # `name`
#         ) for voice in voices[:5]
#     ]
#     await inline_query.answer(results=results)
